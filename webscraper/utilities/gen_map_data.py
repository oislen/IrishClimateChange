import cons
import os
import logging
import pickle
import pandas as pd
import geopandas as gpd
from beartype import beartype
from typing import Union

@beartype
def gen_map_data(
    rep_counties_fpath:str=cons.rep_counties_fpath,
    ni_counties_fpath:str=cons.ni_counties_fpath,
    preaggregate_data_fpath:str=cons.preaggregate_data_fpath,
    map_data_fpath:str=cons.map_data_fpath
    ):
    """Generates counties map data for the bokeh map dashboard

    Parameters
    ----------
    rep_counties_fpath : str
        The file path to the republic of ireland counties .shp file on disk, default is cons.rep_counties_fpath,
    ni_counties_fpath : str
        The file path to northern irleand counties .shp file on disk, default is cons.ni_counties_fpath
    pre_agg_data_dict : str
        The file path to the preaggregated data on disk, default is cons.preaggregate_data_fpath
    map_data_fpath : str
        The file location to write the map data to disk, default is map_data_fpath

    Returns
    -------
    """
    logging.info("Loading rep / ni counties shape files ...")
    # load in county shape files
    rep_counties = (gpd.read_file(rep_counties_fpath)[["ENGLISH", "geometry"]].rename(columns={"ENGLISH": "county"}).to_crs(epsg=2157))
    ni_counties = gpd.read_file(ni_counties_fpath)[["county", "geometry"]].to_crs(epsg=2157)
    logging.info("Loading preaggregated data dictionary ...")
    # load preaggregated data
    with open(preaggregate_data_fpath, "rb") as f:
        pre_agg_data_dict = pickle.load(f)
    logging.info("Concatenating counties geopandas dataframes ...")
    # concatenate county shape files
    counties = gpd.GeoDataFrame(pd.concat([rep_counties, ni_counties], ignore_index=True), crs="EPSG:2157")
    logging.info("Simplifiying counties geometries ...")
    # simplify the granularity of the geometry column
    counties["geometry"] = counties["geometry"].simplify(tolerance=1000)
    logging.info("Standardising county names to title case ...")
    # clean up county column
    counties["county"] = (counties["county"].str.title().str.replace(pat="County ", repl="", regex=False))
    logging.info("Ordering results by county name ...")
    # sort data by county
    counties = counties.sort_values(by="county")
    logging.info("Calculating county level statistics ...")
    # create a dictionary to contain map data
    map_data_list = []
    # iterate over statistic and pre aggregated data
    for stat, pre_agg_data in pre_agg_data_dict.items():
        logging.info(f"{stat} ...")
        pre_agg_data['year'] = pre_agg_data["date"].dt.year.astype(str)
        # aggregate data to county level
        group_cols = ["county","year"]
        #group_cols = ["county"]
        agg_dict = {col: stat for col in cons.col_options}
        # filter data to be between 2010
        pre_agg_data = pre_agg_data.loc[(pre_agg_data['year'].astype(int) >= 2010), :]
        county_data = pre_agg_data.groupby(group_cols, as_index=False).agg(agg_dict)
        county_data['stat'] = stat
        map_data_list.append(county_data)
    map_data = pd.concat(objs=map_data_list,axis=0,ignore_index=True)
    # join county level data to map data
    map_geodata = gpd.GeoDataFrame(
        data=pd.merge(left=counties, right=map_data, on="county", how="left"),
        crs="EPSG:2157",
        )
    if os.path.exists(map_data_fpath):
        logging.info("Writing counties data to disk as pickle file ...")
        # pickle the preaggregated data dictionary to disk
        with open(map_data_fpath, "wb") as f:
            pickle.dump(map_geodata, f, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        raise ValueError(f"{map_data_fpath} does not exist")

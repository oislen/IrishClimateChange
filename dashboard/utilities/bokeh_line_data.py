# import relevant libraries
from beartype import beartype
import numpy as np
import pandas as pd
import pickle

# import custom modules
import cons
from bokeh.models import ColumnDataSource, CDSView, BooleanFilter
from utilities.time_data import time_data

@beartype
def bokeh_line_data(
    pre_agg_data_dict:dict
    ) -> dict:
    """Generates the data used in the bokeh line plot.

    Parameters
    ----------
    pre_agg_data_dict : dict
        The aggregated data to be transformed into aggregated bokeh data objects for visualisation

    Returns
    -------
    dict
        The aggregated bokeh data objects to visualise
    """
    # create dictionary to hold data results
    bokeh_line_data_dict = {}
    for stat, agg_data_dict in pre_agg_data_dict.items():
        stat_level_dict = {}
        for agg_level in cons.line_agg_level_options:
            tmp_level_dict = {}
            # generate time data aggregated by year
            agg_dict = {col: stat for col in cons.col_options}
            date_strftime = cons.date_strftime_dict[agg_level]
            if agg_level == "year":
                time_span = cons.linedash_year_timespan
            elif agg_level == "year-month":
                time_span = cons.linedash_yearmonth_timespan
            elif agg_level == "month":
                time_span = cons.linedash_month_timespan
            point_agg_data = time_data(
                data=agg_data_dict,
                agg_dict=agg_dict,
                time_span=time_span,
                counties=cons.counties,
                strftime=date_strftime,
            )
            # aggregate to county level
            #point_melt_data=pd.melt(frame=point_agg_data, id_vars=['county','date','date_str','index'], value_vars=cons.col_options, var_name='col', value_name='stat').dropna()
            #point_melt_agg_data = point_melt_data.groupby(by=['county','col'], as_index=False).agg({'date':list,'date_str':list, 'index':lambda series:tuple(series.to_list()), 'stat':list})
            #line_melt_agg_data = point_melt_agg_data.pivot(columns=['col'], index=['county','index'], values=['stat'])
            #line_melt_agg_data.columns = line_melt_agg_data.columns.get_level_values("col")
            #line_agg_data = line_melt_agg_data.reset_index()
            line_agg_dict = {col:list for col in point_agg_data.columns.drop('county')}
            line_agg_data = point_agg_data.replace({np.nan:None}).groupby(by=['county'], as_index=False).agg(line_agg_dict)
            # create bokeh data source
            point_datasource = ColumnDataSource(point_agg_data)
            line_datasource = ColumnDataSource(line_agg_data)
            # create filtered column data source views
            dataview_dict = {}
            for county in cons.counties:
                point_county_filter = [True if x == county else False for x in point_datasource.data["county"]]
                line_county_filter = [True if x == county else False for x in line_datasource.data["county"]]
                point_dataview = CDSView(filter=BooleanFilter(point_county_filter))
                line_dataview = CDSView(filter=BooleanFilter(line_county_filter))
                cfg_dict = {"point_dataview": point_dataview,"line_dataview": line_dataview,"color": cons.county_line_colors[county],}
                dataview_dict[county] = cfg_dict
            # update results dictionary
            tmp_level_dict["point_agg_data"] = point_agg_data
            tmp_level_dict["line_agg_data"] = line_agg_data
            tmp_level_dict["point_datasource"] = point_datasource
            tmp_level_dict["line_datasource"] = line_datasource
            tmp_level_dict["dataview_dict"] = dataview_dict
            stat_level_dict[agg_level] = tmp_level_dict
        bokeh_line_data_dict[stat] = stat_level_dict
    # pickle the bokeh line data dictionary to disk
    # with open(cons.bokeh_line_data_fpath, 'wb') as f:
    #    pickle.dump(bokeh_line_data_dict, f, protocol = pickle.HIGHEST_PROTOCOL)
    return bokeh_line_data_dict

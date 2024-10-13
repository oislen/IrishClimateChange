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
            agg_data = time_data(
                data=agg_data_dict,
                agg_dict=agg_dict,
                time_span=time_span,
                counties=cons.counties,
                strftime=date_strftime,
            )
            # create bokeh data source
            datasource = ColumnDataSource(agg_data)
            # create filtered column data source views
            dataview_dict = {}
            for county in cons.counties:
                dataview = ColumnDataSource(agg_data.loc[(agg_data['county'] == county), :])
                cfg_dict = {"dataview": dataview,"color": cons.county_line_colors[county],}
                dataview_dict[county] = cfg_dict
            # update results dictionary
            tmp_level_dict["agg_data"] = agg_data
            tmp_level_dict["datasource"] = datasource
            tmp_level_dict["dataview_dict"] = dataview_dict
            stat_level_dict[agg_level] = tmp_level_dict
        bokeh_line_data_dict[stat] = stat_level_dict
    # pickle the bokeh line data dictionary to disk
    # with open(cons.bokeh_line_data_fpath, 'wb') as f:
    #    pickle.dump(bokeh_line_data_dict, f, protocol = pickle.HIGHEST_PROTOCOL)
    return bokeh_line_data_dict

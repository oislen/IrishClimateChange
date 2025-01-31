# import relevant libraries
from beartype import beartype
import polars as pl
import numpy as np

# import custom modules
import cons
from bokeh.models import ColumnDataSource
from utilities.time_data import time_data

@beartype
def bokeh_line_data(
    pre_agg_data:pl.DataFrame,
    stat:str,
    agg_level:str,
    counties:list
    ) -> dict:
    """Generates the data used in the bokeh line plot.

    Parameters
    ----------
    pre_agg_data : pl.DataFrame
        The aggregated data to be transformed into aggregated bokeh data objects for visualisation
    stat : str
        The statistic being visualised on the dashboard.
    agg_level : str
        The aggregate level being visualised on the dashboard.
    counties : list
        The counties being visualised on the dashboard.

    Returns
    -------
    dict
        The aggregated bokeh data objects to visualise
    """
    # generate time data aggregated by year
    data = pre_agg_data.filter(pl.col("stat") == stat)
    agg_dict = [getattr(pl.col(col).replace({None:np.nan}), stat)().alias(col) for col in cons.col_options]
    date_strftime = cons.date_strftime_dict[agg_level]
    if agg_level == "year":
        time_span = cons.linedash_year_timespan
    elif agg_level == "year-month":
        time_span = cons.linedash_yearmonth_timespan
    elif agg_level == "month":
        time_span = cons.linedash_month_timespan
    agg_data = time_data(
        data=data,
        agg_dict=agg_dict,
        time_span=time_span,
        counties=counties,
        strftime=date_strftime,
    )
    # create filtered column data source views
    dataview_dict = {}
    for county in counties:
        dataview = ColumnDataSource(agg_data.filter(pl.col('county') == county).to_dict(as_series=False))
        cfg_dict = {"dataview":dataview, "color":cons.county_line_colors[county]}
        dataview_dict[county] = cfg_dict
    # update results dictionary
    bokeh_line_data_dict = {"agg_data":agg_data, "dataview_dict":dataview_dict}
    return bokeh_line_data_dict

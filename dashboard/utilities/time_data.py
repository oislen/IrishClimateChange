import datetime
import polars as pl
from typing import Union
from beartype import beartype

@beartype
def time_data(
    data:pl.DataFrame, 
    agg_dict:list, 
    time_span:Union[list, None]=None, 
    counties:Union[list, None]=None, 
    strftime:Union[str, None]=None
    ) -> pl.DataFrame:
    """Aggregates and filters Met Eireann for time series plot

    Parameters
    ----------
    data : polars.DataFrame
        The Met Eireann data to aggregate and filter
    agg_dict : list
        The column aggregation operations to perform on the Met Eireann data
    time_span : list
        A list, or iterable, containing the time series start date and end date as strings to filter for
    counties : list
        A list, or iterable, containing the counties to filter for
    strftime : string
        The strftime expression for converting the start date and end date strings from the time_span parameter into datetime objects for filtering

    Returns
    -------
    polars.DataFrame
        The aggregated and filtered Met Eireann time series data
    """
    agg_data = data.clone()
    agg_data = agg_data.with_columns(date_str = pl.col("date").dt.to_string(format=strftime))
    agg_data = agg_data.with_columns(date = pl.col("date_str").str.to_datetime(format=strftime))
    group_cols = ["county", "date", "date_str"]
    agg_data = agg_data.group_by(group_cols).agg(agg_dict)
    # if filtering date with respect to timespan
    if time_span != None:
        time_span_lb = pl.col("date") >= datetime.datetime.strptime(time_span[0], strftime)
        time_span_ub = pl.col("date") <= datetime.datetime.strptime(time_span[1], strftime)
        agg_data = agg_data.filter(time_span_lb & time_span_ub)
    # if filtering data with respect to counties
    if counties != None:
        agg_data = agg_data.filter(pl.col("county").is_in(counties))
    agg_data = agg_data.sort(by=["county","date"])
    agg_data = agg_data.with_columns(index=pl.struct("county","date").rank(method ="dense", descending=False).over(partition_by="county", order_by="date") - 1)
    #agg_data = agg_data.select(pl.all().replace({None:np.nan}))
    return agg_data

import datetime
import pandas as pd

def time_data(data, agg_dict, time_span = None, counties = None, strftime = None):
    """Aggregates and filters Met Eireann for time series plot

    Parameters
    ----------
    data : pandas.DataFrame
        The Met Eireann data to aggregate and filter
    agg_dict : dict
        The column aggregation operations to perform on the Met Eireann data
    time_span : list
        A list, or iterable, containing the time series start date and end date as strings to filter for
    counties : list
        A list, or iterable, containing the counties to filter for
    strftime : string
        The strftime expression for converting the start date and end date strings from the time_span parameter into datetime objects for filtering

    Returns
    -------
    pandas.DataFrame
        The aggregated and filtered Met Eireann time series data
    """
    agg_data = data.copy()
    agg_data['date_str'] = agg_data['date'].dt.strftime(strftime)
    agg_data['date'] = pd.to_datetime(agg_data['date_str'], format = strftime)
    group_cols = ['county', 'date', 'date_str']
    agg_data = agg_data.groupby(group_cols, as_index = False).agg(agg_dict)
    # if filtering date with respect to timespan
    if time_span != None:
        time_span_lb = (agg_data['date'] >= datetime.datetime.strptime(time_span[0], strftime))
        time_span_ub = (agg_data['date'] <= datetime.datetime.strptime(time_span[1], strftime))
        agg_data = agg_data.loc[time_span_lb & time_span_ub, :]
    # if filtering data with respect to counties
    if counties != None:
        agg_data = agg_data.loc[agg_data['county'].isin(counties)]
    agg_data = agg_data.reset_index(drop = True)
    agg_data['index'] = agg_data.groupby('county')['date'].rank(ascending = True).astype(int).subtract(1)
    return agg_data
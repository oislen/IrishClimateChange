# import relevant libraries
from bokeh.models import ColumnDataSource, CDSView, BooleanFilter

# import custom modules
from utilities.time_data import time_data

def bokeh_data(data, option):
    """"""
    # create dictionary to hold data results
    bokeh_data_dict = {}
    # generate time data aggregated by year
    date_strftime_dict = {'year':'%Y', 'year-month':'%Y-%m', 'month':'%m'}
    counties = ['dublin', 'wexford']
    agg_dict = {'maxtp':'mean', 'mintp':'mean', 'wdsp':'mean', 'sun':'mean', 'evap':'mean', 'rain':'mean'}
    date_strftime = date_strftime_dict[option]
    if option == 'year':
        time_span = ['2010', '2019']
    elif option == 'year-month':
        time_span = ['2010-01', '2019-12']
    elif option == 'month':
        time_span = ['01', '12']
    agg_data = time_data(data = data, agg_dict = agg_dict, time_span = time_span, counties = counties, strftime = date_strftime)
    # create bokeh data source
    datasource = ColumnDataSource(agg_data)
    # create filtered column data source views
    dataview_dict = {}
    line_colors = ['blue', 'orange']
    for idx, county in enumerate(counties):
        county_filter = [True if x == county else False for x in datasource.data['county']]
        dataview = CDSView(source = datasource, filters=[BooleanFilter(county_filter)])
        cfg_dict = {'dataview':dataview, 'color':line_colors[idx]}
        dataview_dict[county] = cfg_dict
    # update results dictionary
    bokeh_data_dict['agg_data'] = agg_data
    bokeh_data_dict['datasource'] = datasource
    bokeh_data_dict['dataview_dict'] = dataview_dict
    return bokeh_data_dict

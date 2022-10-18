# import relevant libraries
import cons
import pickle
from bokeh.models import ColumnDataSource, CDSView, BooleanFilter
from PreProcessData.gen_preaggregate_data import gen_preaggregate_data

# import custom modules
from utilities.time_data import time_data

def bokeh_line_data():
    """"""
    print('~~~ Generating bokeh line data ...')
    # load preaggregated data
    #with open(cons.preaggregate_data_fpath, "rb") as f:
    #    pre_agg_data_dict = pickle.load(f)
    pre_agg_data_dict = gen_preaggregate_data(return_data = True)
    # create dictionary to hold data results
    bokeh_line_data_dict = {}
    for stat, agg_data_dict in pre_agg_data_dict.items():
        stat_level_dict = {}
        for agg_level in cons.line_agg_level_options:
            tmp_level_dict = {}
            # generate time data aggregated by year
            agg_dict = {col:stat for col in cons.col_options}
            date_strftime = cons.date_strftime_dict[agg_level]
            if agg_level == 'year':
                time_span = ['2010', '2019']
            elif agg_level == 'year-month':
                time_span = ['2010-01', '2019-12']
            elif agg_level == 'month':
                time_span = ['01', '12']
            agg_data = time_data(data = pre_agg_data_dict[stat], agg_dict = agg_dict, time_span = time_span, counties = cons.counties, strftime = date_strftime)
            # create bokeh data source
            datasource = ColumnDataSource(agg_data)
            # create filtered column data source views
            dataview_dict = {}
            for county in cons.counties:
                county_filter = [True if x == county else False for x in datasource.data['county']]
                dataview = CDSView(source = datasource, filters=[BooleanFilter(county_filter)])
                cfg_dict = {'dataview':dataview, 'color':cons.county_line_colors[county]}
                dataview_dict[county] = cfg_dict
            # update results dictionary
            tmp_level_dict['agg_data'] = agg_data
            tmp_level_dict['datasource'] = datasource
            tmp_level_dict['dataview_dict'] = dataview_dict
            stat_level_dict[agg_level] = tmp_level_dict
        bokeh_line_data_dict[stat] = stat_level_dict
    # pickle the bokeh line data dictionary to disk
    #with open(cons.bokeh_line_data_fpath, 'wb') as f:
    #    pickle.dump(bokeh_line_data_dict, f, protocol = pickle.HIGHEST_PROTOCOL)
    return bokeh_line_data_dict

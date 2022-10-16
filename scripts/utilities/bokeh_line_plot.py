# import relevant libraries
from bokeh.plotting import figure
from bokeh.models import Span, DatetimeTickFormatter

# import custom modules
import cons

def bokeh_line_plot(bokeh_data_dict, col, stat, agg_level):
    """"""
    # extract out data for bokeh plot
    agg_data_dict = bokeh_data_dict[stat][agg_level]
    # create plot figure object
    plot = figure(toolbar_location='below', output_backend="webgl", **cons.FIG_SETTING)
    # create a horizontal line around the average
    stat_value = agg_data_dict['datasource'].to_df().agg({col:'mean'}).values[0]
    hline = Span(location=stat_value, line_dash='dashed', line_color='red', line_width=3, line_alpha=0.3, name='National Average')
    plot.renderers.extend([hline])

    #plot.x_range.min_interval = 1
    #plot.x_range.max_interval = 47.5
    #plot.xgrid.grid_line_color = None
    #plot.title.text_font_style="bold"
    #plot.title.text_font_size="22px"
    #plot.xaxis.major_label_text_font_size = "11pt"
    #plot.yaxis.major_label_text_font_size = "11pt"
    #plot.xaxis.major_label_orientation = math.pi/4

    # overlay timelines and points
    for county, cfg_dict in agg_data_dict['dataview_dict'].items():
        # add county line
        plot.scatter(x = 'date', y = col, color = cfg_dict['color'], source = agg_data_dict['datasource'], view = cfg_dict['dataview'], size = 8)
        plot.line(x = 'date', y = col, color = cfg_dict['color'], legend_label = county, source = agg_data_dict['datasource'], view = cfg_dict['dataview'], line_width  = 2)
        # create hover tools
        #plot.add_tools(HoverTool(renderers=[county_line], tooltips=[('Date', '@date'), ('Max Temperature', f'@{col}')], attachment='left'))
        # add dates to x-axis ticks
        plot.xaxis.major_label_orientation=0.75
        plot.xaxis[0].formatter = DatetimeTickFormatter(days=["%Y-%m-%d"])
    
    return plot
# import relevant libraries
from bokeh.plotting import figure
from bokeh.models import Span, DatetimeTickFormatter

# import custom modules
import cons

def bokeh_line_plot(bokeh_data_dict):
    """"""
    # create plot figure object
    plot = figure(toolbar_location='below', output_backend="webgl", **cons.FIG_SETTING)
    # create a horizontal line around the average
    hline = Span(location=bokeh_data_dict['datasource'].to_df()['maxtp'].mean(), line_dash='dashed', line_color='red', line_width=3, line_alpha=0.3, name='National Average')
    plot.renderers.extend([hline])

    #plot2.x_range.min_interval = 1
    #plot2.x_range.max_interval = 47.5
    #plot2.xgrid.grid_line_color = None
    #plot2.title.text_font_style="bold"
    #plot2.title.text_font_size="22px"
    #plot2.xaxis.major_label_text_font_size = "11pt"
    #plot2.yaxis.major_label_text_font_size = "11pt"
    #plot2.xaxis.major_label_orientation = math.pi/4

    # overlay timelines and points
    for county, cfg_dict in bokeh_data_dict['dataview_dict'].items():
        # add county line
        plot.scatter(x = 'date', y = 'maxtp', color = cfg_dict['color'], source = bokeh_data_dict['datasource'], view = cfg_dict['dataview'], size = 8)
        plot.line(x = 'date', y = 'maxtp', color = cfg_dict['color'], legend_label = county, source = bokeh_data_dict['datasource'], view = cfg_dict['dataview'], line_width  = 2)
        # create hover tools
        #plot.add_tools(HoverTool(renderers=[county_line], tooltips=[('Date', '@date'), ('Max Temperature', '@maxtp')], attachment='left'))
        # add dates to x-axis ticks
        plot.xaxis.major_label_orientation=0.75
        plot.xaxis[0].formatter = DatetimeTickFormatter(days=["%Y-%m-%d"])
    
    return plot
import cons
from bokeh.models import LinearColorMapper, ColorBar, HoverTool
from bokeh.plotting import figure


def bokeh_map_plot(bokeh_map_data_dict):
    """"""
    # define a blue color palette
    palette = ("lightblue", "steelblue")
    # instantiate LinearColorMapper that linearly maps numbers in a range, into a sequence of colors.
    color_mapper = LinearColorMapper(palette=palette, low = bokeh_map_data_dict['nonmiss_map_data']['maxtp'].min(), high = bokeh_map_data_dict['nonmiss_map_data']['maxtp'].max())
    # create color bar.
    color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8, width=500, height=25, border_line_color=None, location=(0, 0), orientation='horizontal', major_label_text_font_size="18px")
    # create underlying figure object
    map_plot = figure(toolbar_location='below', output_backend="webgl",  **cons.FIG_SETTING)
    map_plot.axis.visible = False
    map_plot.xgrid.grid_line_color = None
    map_plot.ygrid.grid_line_color = None
    map_plot.x_range.min_interval = 1
    map_plot.x_range.max_interval = 70
    map_plot.title.text_font_style="bold"
    map_plot.title.text_font_size="22px"
    # add patches to render states with no aggregate data
    misscounties = map_plot.patches('xs', 'ys', source=bokeh_map_data_dict['missgeosource'], fill_color='white', **cons.MAP_SETTINGS)
    # add patches to render states with aggregate data
    nonmisscounties = map_plot.patches('xs', 'ys', source=bokeh_map_data_dict['nonmissgeosource'], fill_color={'field': 'maxtp','transform': color_mapper}, **cons.MAP_SETTINGS)
    # create hover tool for states with no aggregate data
    map_plot.add_tools(HoverTool(renderers=[misscounties], tooltips=[('County Name', '@county'), ('County Value', 'NA')], attachment='left'))
    # create hover tool for states with aggregate data
    map_plot.add_tools(HoverTool(renderers=[nonmisscounties], tooltips=[('County Name', '@county'), ('County Value', '@maxtp')], attachment='left'))
    map_plot.add_layout(color_bar, 'below')
    return map_plot

# import relevant libraries
import math
from bokeh.plotting import figure
from bokeh.models import Span, DatetimeTickFormatter, HoverTool, Legend

# import custom modules
import cons


def bokeh_line_plot(bokeh_data_dict, col, stat, agg_level, selection):
    """Generates the data used in the bokeh map plot.

    Parameters
    ----------
    bokeh_data_dict : dict
        A dictionary of bokeh aggregated data objects to construct the interactive bokeh line plot with
    col : str
        The climate measure category to plot in the interactive bokeh line plot
    stat : str
        The aggregated statistic to plot in the interactive bokeh line plot
    agg_level : str
        The aggregated statistic sub level to plot in the interactive bokeh line plot
    selection : list
        The selection of counties to construct lines for in the interactive bokeh line plot

    Returns
    -------
    bokeh.plotting.figure
        The interactive bokeh line plot
    """
    # extract out data for bokeh plot
    agg_data_dict = bokeh_data_dict[stat][agg_level]
    # create plot figure object
    plot = figure(toolbar_location="below", output_backend="webgl", **cons.FIG_SETTING)
    # create a horizontal line around the average
    datasource = agg_data_dict["datasource"]
    stat_value = datasource.to_df().agg({col: "mean"}).values[0]
    hline = Span(
        location=stat_value,
        line_dash="dashed",
        line_color="red",
        line_width=3,
        line_alpha=0.3,
        name="National Average",
    )
    plot.renderers.extend([hline])

    # remove grid lines
    plot.xgrid.grid_line_color = None
    plot.ygrid.grid_line_color = None
    # add dates to x-axis ticks
    # remap x-axis tick labels
    axis_data_dict = (
        datasource.to_df()[["index", "date_str"]]
        .drop_duplicates()
        .sort_values(by="index")
        .set_index("index")
        .to_dict()["date_str"]
    )
    plot.xaxis.ticker = list(axis_data_dict.keys())
    plot.xaxis.major_label_overrides = axis_data_dict
    plot.xaxis.major_label_orientation = 0.75
    # plot.xaxis[0].formatter = DatetimeTickFormatter(days=["%Y-%m-%d"])

    plot.x_range.min_interval = 1
    plot.x_range.max_interval = 47.5
    plot.title.text_font_style = "bold"
    plot.title.text_font_size = "22px"
    plot.xaxis.major_label_text_font_size = "11pt"
    plot.yaxis.major_label_text_font_size = "11pt"
    plot.xaxis.major_label_orientation = math.pi / 4

    legend_it = []

    # overlay timelines and points
    for county, cfg_dict in agg_data_dict["dataview_dict"].items():
        if county in selection:
            # add county line
            county_point = plot.scatter(
                x="index",
                y=col,
                color=cfg_dict["color"],
                source=datasource,
                view=cfg_dict["dataview"],
                size=8,
            )
            county_line = plot.line(
                x="index",
                y=col,
                color=cfg_dict["color"],
                source=datasource,
                view=cfg_dict["dataview"],
                line_width=2,
            )
            # create hover tools
            plot.add_tools(
                HoverTool(
                    renderers=[county_point],
                    tooltips=[
                        ("County", "@county"),
                        (f"{agg_level}".title(), "@date_str"),
                        ("Value", f"@{col}"),
                    ],
                    attachment="left",
                )
            )
            legend_it.append((county, [county_line]))

    legend = Legend(items=legend_it)
    legend.click_policy = "mute"
    plot.add_layout(legend, "right")

    return plot

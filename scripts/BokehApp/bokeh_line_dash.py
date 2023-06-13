import pickle
from bokeh.models import Select, CheckboxGroup, Div, Button
from bokeh.layouts import column, row

# import custom modules
import cons
from PreProcessData.gen_preaggregate_data import gen_preaggregate_data
from BokehApp.bokeh_line_data import bokeh_line_data
from BokehApp.bokeh_line_plot import bokeh_line_plot


def bokeh_line_dash(load_data_dict=True):
    """Generates the bokeh line dashboard

    Parameters
    ----------
    load_data_dict : bool
        Whether to load the preaggregated file from disk, or generate it scratch, default is True

    Returns
    -------
    bokeh.layouts.row
        The interactive bokeh line dashboard
    """
    if load_data_dict:
        with open(cons.preaggregate_data_fpath, "rb") as handle:
            pre_agg_data_dict = pickle.load(handle)
    else:
        pre_agg_data_dict = gen_preaggregate_data(return_data=True)
    # generate bokeh data for line plot
    bokeh_line_data_dict = bokeh_line_data(pre_agg_data_dict)
    # create bokeh plot
    line_plot = bokeh_line_plot(
        bokeh_line_data_dict,
        col=cons.col_default,
        stat=cons.stat_default,
        agg_level=cons.line_agg_level_default,
        selection=cons.counties,
    )

    # create call back function for bokeh dashboard interaction
    def callback_line_plot(attr, old, new):
        # extract new selector value
        agg_level = line_agg_level_selector.value
        col = line_col_selector.value
        stat = line_stat_selector.value
        selection = list()
        for i in line_county_checkboxgroup.active:
            selection.append(cons.counties[i])
        # update bokeh plot
        line_plot = bokeh_line_plot(
            bokeh_line_data_dict,
            col=col,
            stat=stat,
            agg_level=agg_level,
            selection=selection,
        )
        # reassign bokeh plot to bokeh dashboard
        dashboard_line.children[1] = line_plot

    def callback_checkboxgroup_selectall():
        line_county_checkboxgroup.active = list(range(len(cons.counties)))

    def callback_checkboxgroup_clearall():
        line_county_checkboxgroup.active = []

    # set up selectors for bokeh line plot
    line_agg_level_selector = Select(
        title="Aggregate Level:",
        value=cons.line_agg_level_default,
        options=cons.line_agg_level_options,
        width=130,
        height=60,
        aspect_ratio=10,
    )
    line_col_selector = Select(
        title="Column:",
        value=cons.col_default,
        options=cons.col_options,
        width=130,
        height=60,
        aspect_ratio=10,
    )
    line_stat_selector = Select(
        title="Statistic:",
        value=cons.stat_default,
        options=cons.stat_options,
        width=130,
        height=60,
        aspect_ratio=10,
    )
    line_county_checkboxgroup = CheckboxGroup(
        labels=cons.counties, active=list(range(len(cons.counties))), width=130
    )
    line_county_selectall_button = Button(label="Select All", width=130)
    line_county_clearall_button = Button(label="Clear All", width=130)
    line_agg_level_selector.on_change("value", callback_line_plot)
    line_col_selector.on_change("value", callback_line_plot)
    line_stat_selector.on_change("value", callback_line_plot)
    line_county_checkboxgroup.on_change("active", callback_line_plot)
    line_county_selectall_button.on_click(callback_checkboxgroup_selectall)
    line_county_clearall_button.on_click(callback_checkboxgroup_clearall)

    # structure dashboard line plot
    space_div = Div(width=30, height=30)
    widgets_line = column(
        line_agg_level_selector,
        space_div,
        line_col_selector,
        space_div,
        line_stat_selector,
        space_div,
        line_county_selectall_button,
        line_county_clearall_button,
        line_county_checkboxgroup,
    )
    dashboard_line = row(widgets_line, line_plot)

    return dashboard_line

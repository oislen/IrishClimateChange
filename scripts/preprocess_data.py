from utilities.gen_master_data import gen_master_data
from utilities.preaggregate_data import preaggregate_data
from utilities.bokeh_line_data import bokeh_line_data
from utilities.bokeh_map_data import bokeh_map_data

if __name__ == '__main__':
    # generate master data file
    gen_master_data()
    # generate the preaggregate data
    preaggregate_data()
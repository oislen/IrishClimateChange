from PreProcessData.gen_master_data import gen_master_data
from PreProcessData.preaggregate_data import preaggregate_data
from PreProcessData.gen_counties_data import gen_counties_data

if __name__ == '__main__':
    # generate master data file
    gen_master_data()
    # generate the preaggregate data
    preaggregate_data()
    # generate counties data
    gen_counties_data()
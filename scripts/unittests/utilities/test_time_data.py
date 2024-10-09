import os
import sys
import random
import pandas as pd
import unittest
import numpy as np
import cons
from unittests.gen_unittest_data import gen_unittest_data
from utilities.time_data import time_data

random.seed(42)
np.random.seed(42)

stat = 'mean'
agg_dict = {col: stat for col in cons.col_options}
# generate unittest data
data = gen_unittest_data()
obs_time_data = time_data(data=data, agg_dict=agg_dict)
exp_data_shape = (6, 12)
exp_data_columns = ['county', 'date', 'date_str', 'maxtp', 'mintp', 'gmin', 'soil', 'wdsp', 'sun', 'evap', 'rain', 'index']

class Test_time_data(unittest.TestCase):
    """"""

    def setUp(self):
        self.obs_time_data = obs_time_data
        self.exp_data_shape = exp_data_shape
        self.exp_data_columns = exp_data_columns

    def test_type(self):
        self.assertEqual(type(self.obs_time_data), pd.DataFrame)

    def test_shape(self):
        self.assertEqual(self.obs_time_data.shape,self.exp_data_shape)

    def test_columns(self):
        self.assertEqual(self.obs_time_data.columns.to_list(), self.exp_data_columns)

if __name__ == "__main__":
    unittest.main()

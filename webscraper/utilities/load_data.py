
import re
import os
import pandas as pd
import cons

def load_data(fpath, stations_fpath=cons.stations_fpath):
    """
    """
    # extract stationid
    station_id = int(re.findall(pattern="dly([0-9]+).csv", string=os.path.basename(fpath))[0])
    # load file lines
    with open(fpath) as file:
        lines = [line.rstrip().lower() for line in file]
    # split into rows
    split_lines = [row.split(',') for row in lines]
    # generate dataframe
    n_cols = len(split_lines[-1])
    data_lines = [line for line in split_lines if len(line) == n_cols]
    dataframe = pd.DataFrame(data_lines[1:], columns = data_lines[0])
    # subset required rows and columns
    sub_cols = dataframe.columns[dataframe.columns.isin(['date'] + cons.col_options)]
    row_filter = dataframe['date'].str.contains('20[1-2]+')
    dataframe = dataframe.loc[row_filter, sub_cols]
    # convert numeric columns
    numeric_cols = ['maxtp', 'mintp', 'igmin', 'gmin', 'sun', 'rain', 'cbl', 'wdsp', 'hm', 'ddhm', 'hg', 'soil', 'pe', 'evap', 'smd_wd', 'smd_md', 'smd_pd', 'glorad']
    for col in numeric_cols:
        if col in dataframe.columns:
            dataframe[col] = dataframe[col].apply(lambda x: x.strip()).replace('', None).astype(float)
    # subset return columns
    cols = dataframe.columns[~dataframe.columns.isin(['ind'])]
    dataframe = dataframe[cols]
    dataframe['station_id'] = station_id
    stations_data = pd.read_csv(stations_fpath).rename(columns={'name':'station'})
    dataframe = pd.merge(left=dataframe, right=stations_data, on='station_id', how='inner').rename(columns={'station_id':'id'})
    dataframe["county"] = dataframe["county"].str.title()
    dataframe["date"] = pd.to_datetime(dataframe["date"], format='%d-%b-%Y')
    return dataframe

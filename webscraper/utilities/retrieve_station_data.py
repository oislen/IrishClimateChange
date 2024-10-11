import logging
from utilities.url_retrieve import url_retrieve

def retrieve_station_data(stations, scraped_data_dir, data_level="dly"):
    """
    """
    # iterate over each station and pull daily level data using using stationid
    resp_log =[]
    for idx, row in stations.iterrows():
        logging.info(f"{idx} {row['county']} {row['station_id']} {row['name']}")
        resp = url_retrieve(stationid=row['station_id'], scraped_data_dir=scraped_data_dir, data_level=data_level)
        logging.info(resp)
        resp_log.append(resp)
    return resp_log
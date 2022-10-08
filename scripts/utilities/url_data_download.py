# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 18:43:30 2020

@author: oislen
"""

# load relevant libraries
import urllib.request
import zipfile
from os import path

def url_data_download(links_dict, data_dir):

    """
    """
    
    arch_dir = path.join(data_dir, 'archive')
        
    for fstem, url in links_dict.items():
    
        print('Downloading data ...')
    
        # define hyper link to download all psra data
        fname = '{}.zip'.format(fstem)
        out_fpath = path.join(arch_dir, fname)
        print(url)
        urllib.request.urlretrieve(url, out_fpath)
        
        print('Unzipping file ...')
        
        # unzip download
        with zipfile.ZipFile(out_fpath, 'r') as zip_ref:
            zip_ref.extractall(path.join(data_dir, fstem))
            
    return 0
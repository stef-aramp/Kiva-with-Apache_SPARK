#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 01:03:52 2018

@author: stephanosarampatzes
"""

import pandas as pd
import re
# csv: the file to be converted
#parquet: the file name of parquet file

def Parquer1(csv, parquet):
    
    # load csv file
    file = pd.read_csv(csv)
    # save to parquet
    file.to_parquet(parquet)
    
    return("Conversion Done! Ready to load '.parquet' files...")

# replace white spaces in column names
def Parquer2(csv, parquet):
    
    # load csv file
    file = pd.read_csv(csv)
    columns = list(file.columns)
    columns = [re.sub(' ', '_', item) for item in columns]
    file.columns = columns
    # save to parquet
    file.to_parquet(parquet)
    
    return("Conversion Done! Ready to load '.parquet' files...")

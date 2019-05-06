#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 11:52:15 2019

@author: Reza
"""

import pandas as pd
import os

path = "datasets/"
files = os.listdir(path)

dfs = []
for file in files:
    filename = file.split("_")
    dfs.append(filename[0])
    exec(dfs[-1] + '= pd.read_csv(path + file)')

print("Name of the dataframes created: ", *dfs, sep="\n")

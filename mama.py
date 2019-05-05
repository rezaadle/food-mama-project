#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 11:52:15 2019

@author: Reza
"""

import pandas as pd
import numpy as np
import os

general_path = "/Users/Reza/Courses/foodMama/"
folder = "datasets"
path = general_path + folder
files = os.listdir(path)

dfs = []
for file in files:
    filename = file.split("_")
    dfs.append(filename[0])
    exec(dfs[-1] + '= pd.read_csv(folder + "/" + file)')

exec("print(" + dfs[1] + ".head())")


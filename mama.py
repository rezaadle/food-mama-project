#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 11:52:15 2019

@author: Reza
"""

def preprocessing(dataframes):
    ''' foods table '''
    # Create a copy of table and then drop unnecessary columns, 
    # replace index with "id", and try to fill the missing data. 
    df_0 = dataframes[0].copy()
    df_0.drop(["created_at","updated_at"], axis=1, inplace=True)
    df_0.set_index("id", inplace=True)

    # Fill availability cell with one of its children data (here with the 1st one)
    ancestry_id = df_0[df_0.availability.isnull()].index
    child_ids = df_0[df_0.ancestry == str(ancestry_id[0])].index
    df_0.loc[ancestry_id[0], ["availability"]] = df_0.loc[child_ids[0], ["availability"]]

    # Fill the category_id with the value of "semoule"
    id_num = df_0[df_0.category_id.isnull()].index
    df_0.loc[id_num[0], ["category_id"]] = df_0[df_0.name == "semoule"]["category_id"].values[0]

    # Change the ancestry value with the subcategory id number
    sub_cat = df_0[df_0.ancestry == "510/404"]["ancestry"]
    df_0.loc[sub_cat.index, "ancestry"] = sub_cat.values[0].split("/")[1]

    # Repeat the same procedure for other values
    df_0.loc[[211,361], "ancestry"] = "512"
    df_0.loc[[560,526], "ancestry"] = "508"

    # Change the "NaN" value in ancestry column with "1" (to be considered 
    # as a root position) for the foods line with at least one child in the table.
    # And those that don't have any (parent/child) relation with "0".
    id_list = df_0[df_0.ancestry.isnull()].index
    for i in id_list:
        if len(df_0[df_0.ancestry == str(i)]) != 0:
            df_0.loc[i, "ancestry"] = "1"
        else:
            df_0.loc[i, "ancestry"] = "0"

    ''' items table '''
    df_2 = dataframes[1].copy()
    df_2.drop(["Quantity"], axis=1, inplace=True)
    df_2.columns = ['id', 'recipe-ingredient', 'name_df_0', 'title_df_1', 'ingredients_df_1', 'origin_df_1']
    df_2.set_index("id", inplace=True)
        
    ''' recipes table '''
    df_1 = dataframes[2].copy()
    df_1.drop(["recommendable","status"], axis=1, inplace=True)
    df_1.set_index("id", inplace=True)

    # Add the Mama web link recipes for the missing values in the "link" column
    foodmama_path = "https://www.foodmama.fr/df_1/"
    index_list = df_1[df_1.link.isnull()].index
    for i in index_list:
        df_1.loc[i, ["link"]] = foodmama_path + str(i)
    
    # Replace "NaN" values with "unknown" rating
    rating_list = df_1[df_1.rating.isnull()].index
    df_1.loc[rating_list, ["rating"]] = "unknown"

    return df_0, df_1, df_2

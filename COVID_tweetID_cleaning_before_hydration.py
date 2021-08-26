# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 16:39:14 2021
This script copys multiple csv files from multiple folders into one folder. Then copys the csv content and
save them to a text file. Directly combine the csv content into a bigger csv file cannot preserve the format.
In the end, append the content in text file one after another.
@author: xiaoh
"""
import json,os, glob
import shutil
import pandas as pd


dir = r"C:\Users\xiaoh\Box\Twitter\Data"
target_dir = r'C:\Users\xiaoh\Box\Twitter\all_csv'
os.chdir(target_dir)

# copy csv files in each month's folder to a target folder
# for folder in os.listdir(dir):
#     for filename in os.listdir(dir + '\\' + folder):
#         shutil.copy(dir + '\\' + folder + '\\' + filename, target_dir)

# access the content of all tweet files and save them to a text file to avoid format change if
# directly copy csv content and combine them
with open (r"C:\Users\xiaoh\Box\Twitter\all_tweets.txt",'a') as in_file:
    for folder in os.listdir(dir):
        for filename in os.listdir(dir + '\\' + folder):
            text = open(filename,'r')
            text = ' '.join([i for i in text]).replace(",", " ")
            in_file.write(text)

# # combine all csv files         
# extension = 'csv'
# all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# #combine all csv files in the list
# combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
# #export to csv
# combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
 
        
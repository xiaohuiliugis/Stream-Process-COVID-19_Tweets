import numpy as np
import pandas as pd
import re
import warnings
import json

#Visualisation
import matplotlib
import matplotlib.pyplot as plt

import seaborn as sns
from IPython.display import display
# 
from mpl_toolkits.basemap import Basemap
from wordcloud import WordCloud, STOPWORDS

import nltk 
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from nltk import tokenize
import pandas.util.testing as tm

matplotlib.style.use('ggplot')
pd.options.mode.chained_assignment = None
warnings.filterwarnings("ignore")

import os
import glob
directory = r'C:\data\covid\COVID_analysis\0327_0416_geotweets'
test_dir = r'C:\data\covid\COVID_analysis\0327_0416_geotweets\test'

try:
    with open(os.path.join(directory, '0327_0416_geo.txt'),'w') as out_file:
        for filename in os.listdir(directory):
            input_file = open(os.path.join(directory, filename),'r')
            for line in input_file:
                out_file.write(line)   
except BaseException as e:
    print (e)

        # Close the input file
input_file.close()
# after directly combining the list of dictionary in each text file, the output file take on the following format:
# [
#     {...     },
#     {...     }
# ][
#     {...     },
#     {...     }
# ]
# Need to mannually replace 
# }
# ][
# with }, using Find "}\r\n][" replace with "},"

                

     
     


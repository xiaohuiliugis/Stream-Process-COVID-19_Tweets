'''
Reference: https://towardsdatascience.com/twitter-sentiment-analysis-based-on-news-topics-during-covid-19-c3d738005b55
Used IBM’s Watson Tone Analyzer to label the tweets with 5 sentiment types, which provide  2500 API calls for free each month. 
Each API call limit to 1000 sentences. So the tweets were put in seperate text files used this text file splitter (https://textfilesplitter.com/)


'''

from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json,os


version = '2020-05-31'
ibm_apikey = "_Q_5d-Ih05QqhfesaZIgssNN3nUKWL-Xa2HD1P6Jz_YP"
ibmUrl = 'https://api.us-east.tone-analyzer.watson.cloud.ibm.com/instances/fd1cb448-3dc6-447e-a5c8-d9c78cb14571'

authenticator = IAMAuthenticator(ibm_apikey)
tone_analyzer = ToneAnalyzerV3(
    version = version,
    authenticator=authenticator
)

tone_analyzer.set_service_url(ibmUrl)

directory = r'C:\data\covid\COVID_analysis\ToneAnalyze\text\separate_text'
# input_file = r'C:\data\covid\COVID_analysis\ToneAnalyze\text\black_4.txt'
outdir = r'C:\data\covid\COVID_analysis\ToneAnalyze\text\result'

# errors = 'ignore' handles special character error: UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 1574: character maps to <undefined>
# file = open(filename, errors='ignore')

for filename in os.listdir(directory):
    input_file = open(os.path.join(directory, filename),'r',encoding="utf8", errors='ignore')
    text =""
    for line in input_file:
        text = text + line
       
    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()

    with open(os.path.join(outdir,filename),'w') as json_file:
        json.dump(tone_analysis,json_file,indent =4, sort_keys = True)
    print(json.dumps(tone_analysis, indent=2))

    #Close the input file
    input_file.close()
    json_file.close()  
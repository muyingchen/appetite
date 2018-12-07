import pytrends
import pandas as pd
import numpy as np
import os

from datetime import datetime, timedelta
from pytrends.request import TrendReq

def google_trends_five_years(inventory='strawberries'):
    """
    Google trends API scripts to collect daily google trends for the past five years on INVENTORY
    in the Bay Area (geo='US-CA-807')

    Result is saved to a csv file. 
    """

    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        csv_path = os.path.join(os.getcwd(), 'backend', 'data')
        keyword = inventory
        start = '12/01/2012'
        end = end='01/01/2018'
        past_five_years = pd.date_range(start=start, end=end, freq='M')
        past_five_years[0].date() + timedelta(days = 1)
        
        for i in range(len(past_five_years) - 1):
            start_time = past_five_years[i].date() + timedelta(days = 1)
            end_time = past_five_years[i+1].date()
            time_frame = str(start_time) + " " + str(end_time)

            # call Google Trends API
            pytrends.build_payload([inventory], cat=0, timeframe=time_frame, geo='US-CA-807', gprop='')
            five_year_trend_temp = pytrends.interest_over_time()
            
            if i == 0:
                five_year_trend = five_year_trend_temp[keyword].to_frame().reset_index(level=['date'])
            else:
                five_year_trend = five_year_trend.append(five_year_trend_temp[keyword].to_frame().reset_index(level=['date']))
        
        # save it to csv file under "../appetite/backend/data" directory
        file_name = inventory + "_google_trends_five_years.csv"
        five_year_trend.to_csv(os.path.join(csv_path, file_name))
        
        return "Finished collecting five-year Google Trends data"
    except:
        return "Exception raised"


def google_trends_ten_years(inventory='strawberries'):
    """
    Google trends API scripts to collect daily google trends for the past ten years on INVENTORY
    in the Bay Area (geo='US-CA-807')

    Result is saved to a csv file. 
    """

    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        csv_path = os.path.join(os.getcwd(), 'backend', 'data')
        keyword = inventory
        start = '12/01/2007'
        end = end='01/01/2018'
        past_ten_years = pd.date_range(start=start, end=end, freq='M')
        past_ten_years[0].date() + timedelta(days = 1)

        for i in range(len(past_ten_years) - 1):
            start_time = past_ten_years[i].date() + timedelta(days = 1)
            end_time = past_ten_years[i+1].date()
            time_frame = str(start_time) + " " + str(end_time)

            # call Google Trends API
            pytrends.build_payload([inventory], cat=0, timeframe=time_frame, geo='US-CA-807', gprop='')
            five_year_trend_temp = pytrends.interest_over_time()
            if i == 0:
                five_year_trend = five_year_trend_temp[keyword].to_frame().reset_index(level=['date'])
            else:
                five_year_trend = five_year_trend.append(five_year_trend_temp[keyword].to_frame().reset_index(level=['date']))

        # save it to csv file under "../appetite/backend/data/" directory
        file_name = inventory + "_google_trends_ten_years.csv"
        five_year_trend.to_csv(os.path.join(csv_path, file_name))
        
        return "Finished collecting ten-year Google Trends data"
    except:
        return "Exception raised"

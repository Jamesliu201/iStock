import os
import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt



def get_realtime_data(stock_symbol):

    api_key = os.getenv('JQ2IPQUPV4M9QIIB')

    if not api_key:
        raise ValueError("No api key bruh")

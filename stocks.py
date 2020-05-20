import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'T36JINI37R8P8H67'
ts = TimeSeries(key = api_key, output_format='pandas')
data, meta_data = ts.get_in
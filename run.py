import numpy as np
import pandas as pd
from datetime import datetime as dt, timedelta as tmd

from warnings import filterwarnings
filterwarnings('ignore')

from importlib import reload
import data_collector.xAPIConnector
reload(data_collector.xAPIConnector)
from data_collector.xAPIConnector import *


import data_collector.DataLoader
reload(data_collector.DataLoader)
from data_collector.DataLoader import *

import data_collector.config
reload(data_collector.config)
from data_collector.config import user_id, pwd

if __name__ == '__main__':
  symbols = ['BITCOIN', 'ETHEREUM']
  start, interval = '2024-12-01 00:00:00', '5min'

  dl = DataLoader(user_id, pwd)
  data = dl.getData(symbols=symbols, start_date=start, interval=interval)
  

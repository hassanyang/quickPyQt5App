import os

import ipaddress
import os
import re
import time
from datetime import datetime
from common import *

import pandas as pd
import typer
from dateutil.relativedelta import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from IPy import *

# from openpyxl import load_workbook
# from openpyxl.utils import get_column_letter

cur = os.path.abspath(os.path.curdir)

css = os.path.join(cur, "standard.qss")
opdir = os.path.join(cur, "output")
if not os.path.exists(opdir):
    os.mkdir(opdir)
qsfile = os.path.join(cur, "setting.ini")
if not os.path.exists(qsfile):
    open(qsfile, 'a').close()

mtoday = datetime.strftime(datetime.now(), "%d/%m/%Y")
# m1month = datetime.strftime(datetime.now() + relativedelta(months=+1),"%d/%m/%Y")
# m3month = datetime.strftime(datetime.now() + relativedelta(days=+89),"%d/%m/%Y")
m1year = datetime.strftime(datetime.now() + relativedelta(days=+360), "%d/%m/%Y")
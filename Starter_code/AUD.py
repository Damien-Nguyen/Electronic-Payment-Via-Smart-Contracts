import pandas as pd
import numpy as np
import random
import matplotlib
import math
from statsmodels.tsa.stattools import adfuller
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
import xgboost as xgb
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor, plot_tree
import hvplot.pandas
import holoviews as hv
hv.extension('bokeh')
import panel as pn
from scipy.stats import t
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
import seaborn as sns
from scipy.optimize import minimize
#custom
import streamlit as st
import requests
import matplotlib.pyplot as plt





# Get AUD exchange rates against different currencies
def get_exchange_rates():
    # Request exchange rates from the API
    url = 'https://v6.exchangerate-api.com/v6/810397d1298e47e03b9e80ac/latest/AUD'

    response = requests.get(url)
    data = response.json()

    return data

a = get_exchange_rates()
ab = pd.DataFrame.from_dict(a)
col_to_keep = ['conversion_rates']
ab = ab[col_to_keep]
ab2 = ab.T
cleaned = pd.DataFrame()
cleaned['AUDUSD'] = ab2['USD']
cleaned['AUDGBP'] = ab2['GBP']
cleaned['AUDCAD'] = ab2['CAD']
cleaned['AUDEUR'] = ab2['EUR']
cleaned['AUDNZD'] = ab2['NZD']
cleaned['AUDCNY'] = ab2['CNY']

cleaned2 = cleaned.copy()
cleaned2.columns = ['US-Dollar','Pounds','Canada','Euro','NZ','China']

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Current Exchange Rates Dashboard - AUD Base for the DRJ Coin")

st.write(cleaned)

st.subheader("The DRJ Coin is Pegged to the AUD")


cleaned2.plot.bar()


# Display the plot using Streamlit
st.pyplot()


import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import plotly.express as px

Electricity = pd.read_csv('dataset/Electricity.csv')
# ETTh1 = pd.read_csv('ETTh1.csv')
# ETTh2 = pd.read_csv('ETTh2.csv')
# ETTm1 = pd.read_csv('ETTm1.csv')
# ETTm2 = pd.read_csv('ETTm2.csv')
# Exchange = pd.read_csv('exchange_rate.csv')
# traffic = pd.read_csv('traffic.csv')
# weather = pd.read_csv('weather.csv')
print(Electricity.head())

px.line(Electricity.sort_values(["date"]), x='date', y='OT',title = "Electricity" ).write_html("electricity_plot.html")  # 保存为 HTML 文件
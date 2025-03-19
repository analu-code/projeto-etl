import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import sys, os
sys.path.append(os.path.abspath("src"))
from src.csv_to_valid import main
from dash import dashboard
from analysis import profiling

df = pd.read_csv('data.csv')
profile = ProfileReport (df, title="Profiling Report")
#profile.to_file("output.html")

tab1, tab2, tab3 = st.tabs(["Validador", "Análise Exploratória", "Dashboard"])

with tab1:
    main()

with tab2:
    profiling()

with tab3:
    dashboard()
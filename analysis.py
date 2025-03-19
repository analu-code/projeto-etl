import pandas as pd
from ydata_profiling import ProfileReport
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

def profiling():
    if "preview" not in st.session_state: 
            st.session_state.preview = True

    st.title("Análise de Dados de Campanhas")
    st.write("Upload do arquivo CSV para análise")

    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv", key="upload_analysis")
    if uploaded_file is not None:
        st.session_state.file_uploaded = True
        df = pd.read_csv(uploaded_file)

        if st.session_state.preview:
            st.write("Preview dos dados:")
            st.dataframe(df.head())

        if st.button("Analisar dados"):
            st.session_state.preview = False
            st.rerun()
        if st.session_state.file_uploaded and not st.session_state.preview:
            profile = ProfileReport(df, title="Profiling Report")
            st_profile_report(profile)
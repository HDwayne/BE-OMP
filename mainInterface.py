import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

st.title('ATMOSPHERE')
st.caption('This is a string that explains something above.')

with st.sidebar:
    dataType = st.radio(
        "Please select how you' like to import your data.",
        ('Stored data (to be uploaded)', 'Live data from a website'))
    
    if dataType == 'Stored data (to be uploaded)':
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            # To read file as bytes:
            bytes_data = uploaded_file.getvalue()
            st.write(bytes_data)

            # To convert to a string based IO:
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            st.write(stringio)

            # To read file as string:
            string_data = stringio.read()
            st.write(string_data)

            # Can be used wherever a "file-like" object is accepted:
            dataframe = pd.read_csv(uploaded_file)
            st.write(dataframe)
    
    else:
        txt = st.text_input('Please enter the address.')
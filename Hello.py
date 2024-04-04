import streamlit as st

st.title("Welkom bij de analyseapp van Waterpolo Insight")
st.text("Voer hier je .CSV bestand in")

if st.button("Dit is een klikbare knop"):
        st.write("Je hebt op de knop geklikt")
else:
        st.write("Je hebt nog niet op de knop geklikt")
st.button("Reset", type="primary") 

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")

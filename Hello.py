import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Welkom bij de analyseapp van Waterpolo Insight")
st.text("Voer hier je .CSV bestand in")

if st.button("Dit is een klikbare knop"):
        st.write("Je hebt op de knop geklikt")
else:
        st.write("Je hebt nog niet op de knop geklikt")
st.button("Reset", type="primary") 


# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)
url = "https://docs.google.com/spreadsheets/d/1MNbnI5pV7LVZvGWAr9rvy0efqehJWdVEpI_tnw52iJM/edit#gid=0"
df = conn.read(spreadsheet=url)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
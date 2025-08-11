import streamlit as st
import time

st.set_page_config(
    page_title="Teams",
    page_icon="⚽",
    layout="wide"
)

time.sleep(0.5)

df_data = st.session_state["data"]


clubes = df_data["Club"].unique()
club = st.sidebar.selectbox("Clube", clubes)

df_filtred = df_data[(df_data["Club"] == club)].set_index("Name")

st.image(df_filtred.iloc[0] ["Club Logo"])
st.markdown(f"## {club}")

columns = ["Age", "Photo","Flag","Overall","Value(£)","Wage(£)","Joined",
           "Height(cm.)","Weight(lbs.)",
           "Contract Valid Until","Release Clause(£)",]

st.dataframe(df_filtred[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d", min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f", 
                                                    min_value=0, max_value=df_filtred["Wage(£)"].max()),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country"),
             })








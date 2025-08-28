import streamlit as st
import plotly.express as px
import pandas as pd
student={
    "Name":["Alice","Bob","Charlie","Derek","Elina"],
    "Age":[20,21,19,22,20],
    "City":["New York","Los Angeles","Chicago","Houston","Phoenix"],
    "Total":[85,90,78,88,92]
}
df=pd.DataFrame(student)
st.dataframe(df)
fig=px.bar(df,x="Name",y="Total",color="City",text="Total",title="Student Total Marks")
st.plotly_chart(fig)
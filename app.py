import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title="Industrial KPI Dashboard", layout="wide")

st.title("📊 Industrial Production Dashboard")

# Fake data
np.random.seed(42)
data = pd.DataFrame({
    "Time": pd.date_range(start="2024-01-01", periods=100, freq="h"),
    "Production": np.random.randint(80, 120, 100),
    "Defects": np.random.randint(0, 10, 100),
    "Downtime": np.random.randint(0, 5, 100)
})

# Sidebar filters
st.sidebar.header("Filters")
selected_range = st.sidebar.slider("Select Time Range", 0, 99, (0, 99))
filtered_data = data.iloc[selected_range[0]:selected_range[1]]

# KPIs
total_production = data["Production"].sum()
total_defects = data["Defects"].sum()
defect_rate = (total_defects / total_production) * 100
avg_downtime = data["Downtime"].mean()

# Display KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Production", total_production)
col2.metric("Total Defects", total_defects)
col3.metric("Defect Rate (%)", round(defect_rate, 2))
col4.metric("Avg Downtime", round(avg_downtime, 2))

# Charts
st.subheader("Production Over Time")
st.line_chart(filtered_data.set_index("Time")["Production"])

st.subheader("Defects Over Time")
st.line_chart(data.set_index("Time")["Defects"])

st.subheader("Downtime Distribution")
st.bar_chart(data["Downtime"])
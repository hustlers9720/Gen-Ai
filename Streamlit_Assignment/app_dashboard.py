import streamlit as st

st.title("Simple Sales Dashboard") # this is use to give the title of the dashboard

months = ["January", "February", "March", "April"] # this is use to create a list of months that we will use in select box to show the sales data of each month

sales = { # this is use to create a dictionary of sales data for each month
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

selected_month = st.selectbox("Select Month", months) # this is use to create a select box and we pass the list of months in that select box and we store the selected month in the selected_month variable 

st.metric(label=f"{selected_month} Sales", value=sales[selected_month]) # this is use to show the sales data of the selected month in the form of metric and we pass the label as the selected month and value as the sales data of that selected month

st.bar_chart(list(sales.values())) # this is use to show the sales data of all months in the form of bar chart and we pass the list of
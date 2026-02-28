import streamlit as st

# Sidebar Inputs
product_name = st.sidebar.text_input("Product Name") # by this we take the input of the product name

category = st.sidebar.selectbox( # by this we have taken the category of the product in form of selct box
    "Category",
    ["Electronics", "Clothing", "Books", "Home", "Sports"]
)

price = st.sidebar.number_input("Price", min_value=0.0) # by this we have taken the price of the product in form of number input and we have set the minimum value to 0.0

add_product = st.sidebar.button("Add Product") # by this we have created a button in sidebar and when we click on that button then it will add the product and show the details of the product

# Button Click Logic
if add_product:
    st.success("Product added successfully!") # this is use to show the success message when button is clicked and product is added successfully

    st.write("Product Details:") # this is use to show the details of the product when button is clicked
    st.write("Product Name:", product_name)
    st.write("Category:", category)
    st.write("Price:", price)
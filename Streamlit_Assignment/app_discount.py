import streamlit as st

product_price = st.number_input("Enter the price of the product") # we have take the input as number that is the price of the product
discount_percentage = st.slider("Enter the discount percentage", 0, 100, 0) # we take the discount percentage as in form of a slider

discounted_price = st.button("Calculate Discounted Price") # this is the button upo which we have to calculate the dicount price

if discounted_price:
    discount_amount = (discount_percentage / 100) * product_price
    final_price = product_price - discount_amount
    st.success(f"The discounted price is: {final_price}") # here if button click then in if conditoon it comes and successfully show the result of discounted price
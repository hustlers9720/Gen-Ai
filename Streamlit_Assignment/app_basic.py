import streamlit as st # by this we easily import streamlit library in our file

st.title("welcome to Streamlit") # this is use to give the title 
name = st.text_input("Enter Your Name") # this is use to take input from user and we store that input in the name variable

submit  = st.button("Greet Me") # this is use to create a button and we store the response in the submit variable 

if submit: # this is use to check if button is clicked or not if submit is true then it goes in if condition 
    st.write(f"Hello {name}") # this is use to display the message when button is clicked

import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

def calculate(operation, num1, num2):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        return num1 / num2

result = calculate(operation, num1, num2)
st.markdown(f"<h2 style='color: red; font-size: 24px;'>The result is: {result}</h2>", unsafe_allow_html=True)

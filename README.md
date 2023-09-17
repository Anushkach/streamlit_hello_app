# Simple Calculator Streamlit App
This Python script creates a simple calculator app using the Streamlit library. The app allows users to enter two numbers and choose an arithmetic operation (addition, subtraction, multiplication, or division). The app then calculates and displays the result of the selected operation.

## Code Explanation
1. Import the necessary module:

~~~
import streamlit as st
~~~
2. Add a title and input fields for the two numbers and the operation:
~~~
st.title("Simple Calculator")

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])
~~~
3. Define a function to perform the selected operation:
~~~
def calculate(operation, num1, num2):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        return num1 / num2
~~~
4. Call the calculate function and display the result with custom font color and size:
~~~
result = calculate(operation, num1, num2)
st.markdown(f"<h2 style='color: red; font-size: 24px;'>The result is: {result}</h2>", unsafe_allow_html=True)
~~~

## Running the App
To Run the streamlit app, execute the following command in the terminal
~~~json
streamlit run streamlit_app.py
~~~
This will launch a web browser with the calculator app, where you can enter the numbers and choose an operation to perform. The app will display the result of the calculation with the custom font color and size.

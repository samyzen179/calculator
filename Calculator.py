import streamlit as st

import math

st.header(":rainbow[Scientific Calculator]", divider="red")

sidebar = st.sidebar

sidebar.markdown("### Scientific Calculator")
sidebar.divider()

sidebar.subheader("About")
sidebar.write("This is a scientific calculator that help you to add, multiply, subtract, divide, find square roots of numbers, calculate power of a number and finding the area of a triangle")

st.markdown("Select what you want the ***:red[Scientific Calculator]*** to calculate or solve for you")

col1, col2, col3, col4 = st.columns(4)


if 'add_btn' not in st.session_state:
    st.session_state.add_btn = False

if 'mul_btn' not in st.session_state:
    st.session_state.mul_btn = False

if 'sub_btn' not in st.session_state:
    st.session_state.sub_btn = False

if 'div' not in st.session_state:
    st.session_state.div = False

if 'sqrt' not in st.session_state:
    st.session_state.sqrt = False

if 'pwr' not in st.session_state:
    st.session_state.pwr = False

if 'area' not in st.session_state:
    st.session_state.area = False

def set_state():
    st.session_state.add_btn = True
      

def set_state2():
    st.session_state.mul_btn = True
    st.session_state.add_btn = False

def set_state3():
    st.session_state.sub_btn = True
    st.session_state.add_btn = False
    st.session_state.mul_btn = False

def set_state4():
    st.session_state.div = True
    st.session_state.sub_btn = False
    st.session_state.add_btn = False
    st.session_state.mul_btn = False


def set_state5():
    st.session_state.div = False
    st.session_state.sqrt = True
    st.session_state.sub_btn = False
    st.session_state.add_btn = False
    st.session_state.mul_btn = False

def set_state6():
    st.session_state.div = False
    st.session_state.pwr = True
    st.session_state.sqrt = False
    st.session_state.sub_btn = False
    st.session_state.add_btn = False
    st.session_state.mul_btn = False

def set_state7():
    st.session_state.div = False
    st.session_state.area = True
    st.session_state.pwr = False
    st.session_state.sqrt = False
    st.session_state.sub_btn = False
    st.session_state.add_btn = False
    st.session_state.mul_btn = False


col1.button("*:red[Addition]*", on_click=set_state)
col2.button("*:blue[Division]*", on_click=set_state4)
col2.button("*:blue[Multiplication]*", on_click=set_state2)
col1.button("*:red[Subtraction]*", on_click=set_state3)
col3.button("*:orange[Square Root]*", on_click=set_state5)
col4.button("*:rainbow[Area of a triange]*", on_click=set_state7)
col3.button("*:orange[Exponential]*", on_click=set_state6)

if st.session_state['add_btn']:
    num1 = st.number_input("Input first number", step=1)
    num2 = st.number_input("Input second number", step=1)
    res = st.button("Add")
    if res:
        result = num1 + num2
        st.write(f"The sum of {num1} and {num2} = {result}")
        if st.button("Clear"):
            num1 = st.empty
            num2 = st.empty

elif st.session_state['mul_btn']:
    num1 = st.number_input("Input first number", step=1)
    num2 = st.number_input("Input second number", step=1)
    res = st.button("Multiply")
    if res:
        result = num1 * num2
        st.write(f"The product of {num1} and {num2} = {result}")
        if st.button("Clear"):
            num1 = st.empty
            num2 = st.empty

elif st.session_state['sub_btn']:
    num1 = st.number_input("Input first number", step=1)
    num2 = st.number_input("Input second number", step=1)
    res = st.button("Subtract")
    if res:
        result = num1 - num2
        st.write(f"{num1} minus {num2} = {result}")
        if st.button("Clear"):
            num1 = st.empty
            num2 = st.empty

elif st.session_state['div']:
    num1 = st.number_input("Input the number you want to divide", step=1)
    num2 = st.number_input("Input the divisor", step=1)
    res = st.button("Divide")
    if res:
        result = num1 / num2
        st.write(f"{num1} divided by {num2} = {result}")
        if st.button("Clear"):
            num1 = st.empty
            num2 = st.empty

elif st.session_state['sqrt']:
    num1 = st.number_input("Input the number", step=1)
    res = st.button("Find the square root")
    if res:
        result = math.sqrt(num1)
        st.write(f"The square root of {num1} = {result}")
        if st.button("Clear"):
            num1 = st.empty

elif st.session_state['pwr']:
    num1 = st.number_input("Input the number", step=1)
    num2 = st.number_input("Input the power", step=1)
    res = st.button("Solve")
    if res:
        result = num1 ** num2
        st.write(f"{num1} exponential {num2}= {result}")
        if st.button("Clear"):
            num1 = st.empty
            num2 = st.empty

elif st.session_state['area']:
    num1 = st.number_input("Input the base of the triangle", step=1)
    num2 = st.number_input("Input the height of the triangle", step=1)
    res = st.button("Solve")
    if res:
        result = (num1 * num2) / 2
        st.write(f"The area of the triangle with {num1} as the base and  {num2} as the height = {result}")
        if st.button("Clear"):
            num1 = st.empty
            num2 = st.empty

else:
    st.empty()



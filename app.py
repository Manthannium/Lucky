import streamlit as st

st.title('Get your Lucky number :sunglasses:')
st.header('Enter your name')
name = st.text_input('')

def calculate():
    n = len(name)
    sum = 0
    for i in range(n):
        if name[i].isalpha():
            sum = sum + ord(name[i].upper()) - 64
        elif name[i].isdigit():
            sum = sum + ord(name[i].upper()) - 48
        else:
            sum = sum + 0

    while sum > 9:
        m = 0
        while sum > 0:
            m = m + (sum%10)
            sum = sum//10
        sum = m

    welcome = "Hello " + name + "!"
    st.success(welcome)
    st.write('Your lucky number is ', int(sum))

if st.button("Calculate result"):
    calculate()


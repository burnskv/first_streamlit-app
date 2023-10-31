import streamlit
import pandas

streamlit.title ('My Parents Healthy Diner')

streamlit.header ('Breakfast Menu')
streamlit.text('🥣  Omega 2 and Porridge')
streamlit.text(' 🥗 Rocket, Kale and Spinach Tart')
streamlit.text(' 🐔 Hard-Boiled free-range egg')
streamlit.text('  🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)

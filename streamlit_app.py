import streamlit
import pandas

streamlit.title ('My Parents Healthy Diner')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list =  my_fruit_list.set_index('Fruit')

streamlit.multiselect ("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)

streamlit.header ('Breakfast Menu')
streamlit.text('🥣  Omega 2 and Porridge')
streamlit.text(' 🥗 Rocket, Kale and Spinach Tart')
streamlit.text(' 🐔 Hard-Boiled free-range egg')
streamlit.text('  🥑🍞 Avocado Toast')



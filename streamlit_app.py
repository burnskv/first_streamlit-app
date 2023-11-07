import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title ('My Parents Healthy Diner')

streamlit.header ('Breakfast Menu')
streamlit.text('🥣  Omega 2 and Porridge')
streamlit.text(' 🥗 Rocket, Kale and Spinach Tart')
streamlit.text(' 🐔 Hard-Boiled free-range egg')
streamlit.text('  🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list =  my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect ("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?

# streamlit.dataframe(fruityvice_normalized)

streamlit.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

def get_fruityjuice_data(this_fruit_choice):
      fruityjuice_response = requests.get("https://fruityjuice.com/api/fruit/" + this_fruit_choice)
      fruityjuice_normalized = pandas.json_normalize(fruityjuice_response.json())
      return fruityjuice_normalized


streamlit.header ('Fruityvice Fruit advice!')

try:
  fruit_choice = streamlit.text_input('What furit would you like information about?')
  if not fruit_choice:
       streamlit.error("please select a fruit to get information.") 
  else:
       back_from_function = get_fruityjuice_data(fruit_choice)
       # fruityvice_respons = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
       # fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
       streamlit.dataframe(back_from_function)

except URLError as e:
      streamlit.error()
  

# fruit_add = streamlit.text_input('What fruit would you like to add?')
# streamlit.write('Thanks for adding ', fruit_add)
# my_cur.execute("insert into fruit_load_list values ('from streamlit')")

# Importamos stramlit, creamos el título, la cabecera y los textos
import streamlit

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥗 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Importamos pandas y añadimos la lista
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# #New Sección para mostrar la respuesta de la API de fruityvice
import requests
# streamlit.write('Thanks for adding ', fruit_choice)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    #streamlit.text(fruityvice_response.json()) ELIMINAMOS LA LINEA
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    # write your own comment - what does this do?
    return fruityvice_normalized
  
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
  else:
      back_from_funtion = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_funtion)
except URLError as e:
  streamlit.error()
  
streamlit.stop()
import snowflake.connector

streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
         return my_cur.fetchall()
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)


def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
     my_cur.execute("insert into fruit_load_list values ('from streamlit
     return "Thanks for adding " + new_fruit
            
add my_fruit = streamlit.text_input( 'What fruit would you like to add?')     
if streamlit.button('Add a Fruit to the List'):
  my cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back from function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)

#from urllib.error import URLError

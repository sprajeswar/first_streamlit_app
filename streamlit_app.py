import streamlit

#streamlit.title('My another trial in Streamlit!!!')
#streamlit.header("This is header")
#streamlit.text('🥣line 1')
#streamlit.text('🥗line 2')
#streamlit.text('🐔line 3')
#streamlit.text('🥑line 3')
#streamlit.text('🍞line 3')
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.multiselect("Pick some fruites: ", list(my_fruit_list.index))
fruits_selected = streamlit.multiselect("Pick some fruites: ", list(my_fruit_list.index), ["Apple", "Banana"])
fruits_to_show = my_fruit_list.loc(fruits_selected)
streamlit.dataframe(fruits_to_show)
streamlit.dataframe(my_fruit_list)

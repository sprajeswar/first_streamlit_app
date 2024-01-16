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
streamlit.multiselect("Pick some fruites: ", list(my_fruit_list.index), ['Apple', 'Banana', 'some'])
streamlit.dataframe(my_fruit_list)

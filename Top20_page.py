import streamlit as st
import pickle
import numpy as np




popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))



def show_top_20():
        st.header("Top 20 Books :")

        book_data_image = list(popular_df["Image-URL-M"])
        book_data_title = list(popular_df["Book-Title"])


 

        col1, col2, col3, col4, col5 = st.columns(5)

        for i in range(0,20,5):
             
            with col1:
                st.image( book_data_image[i])
                st.text(book_data_title[i])
               
            with col2:
                st.image( book_data_image[i+1])
                st.text(book_data_title[i+1])
                
            with col3:           
                st.image( book_data_image[i+2])
                st.text(book_data_title[i+2])
               
            with col4:
                st.image( book_data_image[i+3])
                st.text(book_data_title[i+3])
              
            with col5:
                st.image( book_data_image[i+4])
                st.text(book_data_title[i+4])
              

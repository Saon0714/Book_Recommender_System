import streamlit as st
import pickle
import numpy as np




popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))



def show_top_20():
        st.header("Top 20 Books :")

        book_data_list = list(popular_df["Image-URL-M"])

 

        col1, col2, col3, col4, col5 = st.columns(5)

        for i in range(0,20,5):
             
            with col1:
                st.image( book_data_list[i])
               
            with col2:
                st.image( book_data_list[i+1])
                
            with col3:           
                st.image( book_data_list[i+2])
               
            with col4:
                st.image( book_data_list[i+3])
              
            with col5:
                st.image( book_data_list[i+4])
              
import streamlit as st
import pickle
import numpy as np




popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

def recommend(book_name):
    # index fetch
    index = np.where(pt.index==book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[1:6]
    
    titles = []
    authors = []
    images = []
    for i in similar_items:
        title = []
        author = []
        image = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        title.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        author.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        image.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        titles.append(title)
        authors.append(author)
        images.append(image)
    
    return titles, authors, images


def show_recommendations():
    st.title("Book Recommender System")

    books_list = sorted(list(pt.index))
    book_name = st.selectbox("Select a Book--", books_list)



    ok = st.button("Similar Books")

    if ok:
        titles, authors, images = recommend(book_name)

        st.subheader(book_name)
        img_list = books[books["Book-Title"]==book_name]["Image-URL-M"]
        img = list(img_list)[0]
        st.image(img)
        st.subheader(f"The Books similar to {book_name} are:")

        col1, col2, col3, col4, col5 = st.columns(5)

        
        with col1:
            st.image(images[0])
            st.text(titles[0][0])
            # st.text(authors[0])
        with col2:
            st.image(images[1])
            st.text(titles[1][0])
            # st.text(authors[1])
        with col3:           
            st.image(images[2])
            st.text(titles[2][0])
            # st.text(authors[2])
        with col4:
            st.image(images[3])
            st.text(titles[3][0])
            # st.text(authors[3])
        with col5:
            st.image(images[4])
            st.text(titles[4][0])
            # st.text(authors[4])

import pickle
import streamlit as st
import requests
import pandas as pd
import numpy as np

pt=pickle.load(open('pt.pkl','rb'))
books=pickle.load(open('books.pkl','rb'))
similarity_scores=pickle.load(open('similarity_scores.pkl','rb'))

def recommend(book_name):
    # index fetch
    index = np.where(pt.index==book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])),key=lambda x:x[1],reverse=True)[0:6]
    
    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        data.append(item)
    
    return data


st.title("Book Reccomendation System")
selected_book_name=st.selectbox("Search Your Book", pt.index.to_list())

if st.button('Recommend'):
    results=recommend(selected_book_name)

    st.header("Your Book")
    bcol1,bcol2,bcol3 = st.columns(3)
    with bcol1:
        st.image(results[0][2])
        st.write(results[0][0])
        st.write("-"+results[0][1])

    st.header("Related Books")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(results[1][2])
        st.write(results[1][0])
        st.write("-"+results[1][1])
    
    with col2:
        st.image(results[2][2])
        st.write(results[2][0])
        st.write("-"+results[2][1])
    
    with col3:
        st.image(results[3][2])
        st.write(results[3][0])
        st.write("-"+results[3][1])
    
    with col4:
        st.image(results[4][2])
        st.write(results[4][0])
        st.write("-"+results[4][1])
    
    with col5:
        st.image(results[5][2])
        st.write(results[5][0])
        st.write("-"+results[5][1])
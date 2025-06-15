import streamlit as st
import pickle
import pandas as pd
import requests


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id= movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


st.header('Movie Recommender System')
movies_list = pickle.load(open('movies_dict.pkl', 'rb'))
movies= pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))


selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)


if st.button('Show Recommendation'):
    recommended_movies = recommend(selected_movie)
    for i in recommended_movies:
        st.write(i)
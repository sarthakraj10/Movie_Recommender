import streamlit as st
import pickle
import pandas as pd
import requests as req
import gdown
import time
from requests.exceptions import RequestException, ConnectionError
from dotenv import load_dotenv
import os

# ---------------- Load environment variables ----------------
load_dotenv()
tmdb_api_keys = os.getenv('tmdb_API_KEYS')

# ---------------- Download pickle files if not present ----------------





# ---------------- Load pickle files ----------------
movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ---------------- Fetch posters and IMDb links ----------------
def fetch_posters(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api_keys}&language=en-US'

    for attempt in range(3):  # retry up to 3 times
        try:
            res = req.get(url, timeout=10)
            res.raise_for_status()
            data = res.json()

            if 'success' in data and data['success'] is False:
                return (
                    "https://via.placeholder.com/150?text=No+Poster",
                    "https://www.imdb.com"
                )

            poster_url = (
                'https://image.tmdb.org/t/p/w185' + data['poster_path']
                if data.get('poster_path')
                else "https://via.placeholder.com/150?text=No+Poster"
            )
            imdb_url = (
                'https://www.imdb.com/title/' + data['imdb_id']
                if data.get('imdb_id')
                else "https://www.imdb.com"
            )
            return poster_url, imdb_url

        except (ConnectionError, RequestException) as e:
            print(f"⚠️ Attempt {attempt+1} failed: {e}")
            time.sleep(2)

    # Fallback if all attempts fail
    return (
        "https://via.placeholder.com/150?text=No+Poster",
        "https://www.imdb.com"
    )

# ---------------- Recommend movies ----------------
def recommend_movie(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    posters = []
    imdb_page = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        poster_link, imdb_link = fetch_posters(movie_id)
        posters.append(poster_link)
        imdb_page.append(imdb_link)

    return recommended_movies, posters, imdb_page

# ---------------- Streamlit UI ----------------
st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox(
    'Which movie do you like?', movies['title'].values
)

if st.button("Recommend"):
    names, posters, imdb_pages = recommend_movie(selected_movie_name)

    columns = st.columns(5)
    for i, col in enumerate(columns):
        with col:
            st.text(names[i])
            st.markdown(
                f'<a href="{imdb_pages[i]}" target="_blank">'
                f'<img src="{posters[i]}" alt="{names[i]}" style="width:100%;">'
                '</a>',
                unsafe_allow_html=True
            )

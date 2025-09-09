import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        data = requests.get(url)
        data.raise_for_status()
        data = data.json()
        poster_path = data.get('poster_path', '')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        return "https://via.placeholder.com/500x750?text=No+Image"
    except:
        return "https://via.placeholder.com/500x750?text=Error+Loading+Image"

def recommend(movie):
    try:
        # Convert the movies dictionary to a DataFrame
        movies_df = pd.DataFrame(movies)
        
        # Find the index of the selected movie
        index = movies_df[movies_df['title'] == movie].index[0]
        
        # Get similarity scores
        distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])
        
        recommended_movie_names = []
        recommended_movie_posters = []
        
        for i in distances[1:6]:
            movie_id = movies_df.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies_df.iloc[i[0]].title)
        
        return recommended_movie_names, recommended_movie_posters
    except Exception as e:
        st.error(f"Error in recommendation: {str(e)}")
        return [], []

st.header('Movie Recommender System')

# Load data with error handling
try:
    # Assuming movies is stored as a dictionary in the pickle file
    movies = pickle.load(open('movies_dict.pkl', 'rb'))
    
    # If movies is a dictionary, convert it to DataFrame
    if isinstance(movies, dict):
        movies_df = pd.DataFrame(movies)
    else:
        movies_df = movies
        
    similarity = pickle.load(open('similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Data files not found. Please ensure movies_dict.pkl and similarity.pkl exist")
    st.stop()

# Get movie list from the DataFrame
movie_list = movies_df['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie)
    
    if names:
        cols = st.columns(5)
        for i, col in enumerate(cols):
            with col:
                st.text(names[i])
                st.image(posters[i])
    else:
        st.warning("No recommendations available for this movie.")
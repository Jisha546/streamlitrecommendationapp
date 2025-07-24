import streamlit as st
import pandas as pd
import random

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("movie_recommendations_small.csv")
    return df

df = load_data()

# Multilingual dictionary
translations = {
    'English': {
        'title': "🎬 Movie Recommendation App",
        'subtitle': "Curated picks based on your taste",
        'language': "🌐 Choose language:",
        'select_movie': "📥 Select a movie",
        'recommend': "🎯 Recommended for you:",
        'genre_filter': "🎭 Filter by Genre:",
        'rate_movie': "⭐ Rate this movie (0–5):",
    },
    'Spanish': {
        'title': "🎬 Aplicación de Recomendación de Películas",
        'subtitle': "Selecciones basadas en tu gusto",
        'language': "🌐 Elige idioma:",
        'select_movie': "📥 Selecciona una película",
        'recommend': "🎯 Recomendado para ti:",
        'genre_filter': "🎭 Filtra por género:",
        'rate_movie': "⭐ Califica esta película (0–5):",
    },
    'French': {
        'title': "🎬 Application de Recommandation de Films",
        'subtitle': "Suggestions basées sur vos goûts",
        'language': "🌐 Choisissez la langue:",
        'select_movie': "📥 Sélectionnez un film",
        'recommend': "🎯 Recommandé pour vous:",
        'genre_filter': "🎭 Filtrer par genre:",
        'rate_movie': "⭐ Notez ce film (0–5):",
    }
}

# Language selection
lang = st.selectbox("🌐 Choose language / Elige idioma / Choisissez la langue", list(translations.keys()))
t = translations[lang]

st.title(t['title'])
st.caption(t['subtitle'])

# Genre selection
all_genres = sorted(set(genre.strip() for sublist in df['genre'].dropna().str.split('|') for genre in sublist))
selected_genre = st.selectbox(t['genre_filter'], ["All"] + all_genres)

# Movie selection
movie_list = df['title'].dropna().unique()
selected_movie = st.selectbox(t['select_movie'], sorted(movie_list))

# Filter by genre
if selected_genre != "All":
    df_filtered = df[df['genre'].str.contains(selected_genre, case=False, na=False)]
else:
    df_filtered = df

# Show Recommendations
st.subheader(t['recommend'])
recommended = df_filtered[df_filtered['title'] != selected_movie].sample(n=2)
for i, row in recommended.iterrows():
    st.write(f"👉 {row['title']}")

# Movie Rating
st.subheader(t['rate_movie'])
rating = st.slider(f"⭐ {selected_movie}", 0.0, 5.0, 3.0, 0.5)
st.success(f"You rated **{selected_movie}** {rating} ⭐")


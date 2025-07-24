import pandas as pd
import streamlit as st

# Load movie data
df = pd.read_csv("movies.csv")

# Website title
st.title("🎬 Movie Recommender")
st.write("Tell me what you're in the mood for (genre, vibe, keyword) and I'll suggest something cool!")

# Input box
user_input = st.text_input("What are you in the mood for? (e.g. thriller, romance, war, chill)", "")

# When user types something
if user_input:
    user_input = user_input.lower()
    matches = df[df['genre'].str.lower().str.contains(user_input) | df['description'].str.lower().str.contains(user_input)]
    
    if not matches.empty:
        st.subheader("🔍 Based on your interests, we recommend:")
        for i, row in matches.iterrows():
            st.markdown(f"**{row['title']}**  \n*{row['genre']}*  \n→ _{row['description']}_  \n")
    else:
        st.warning("😔 No exact matches found. Try different keywords!")
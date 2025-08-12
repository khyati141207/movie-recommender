import pandas as pd
import streamlit as st

# Load movie data
df = pd.read_csv("movies.csv")

# Website title
st.title("🎬 Movie Recommender")
st.write("Tell me what your mood/preference and I'll suggest something!\nPS:Website had updated data till July 2025")

# Rename columns for consistency if needed
df.columns = [col.strip().lower() for col in df.columns]
df.rename(columns={
    'small description': 'description',
    'platforms on which it is available': 'available on'
}, inplace=True)

# Input boxes
user_input1 = st.text_input("keyword 1", "")
user_input2 = st.text_input("keyword 2", "")
user_input3 = st.text_input("language", "")
matches = pd.DataFrame()  # empty by default

# when user types something, choosing the right movies
if user_input1 and user_input2:
    user_input1 = user_input1.lower()
    user_input2 = user_input2.lower()
    
    matches = df[
    (df['genre'].str.lower().str.contains(user_input1) | df['description'].str.lower().str.contains(user_input1)) &
    (df['genre'].str.lower().str.contains(user_input2) | df['description'].str.lower().str.contains(user_input2))
]

if user_input2 and user_input3:
    user_input2 = user_input2.lower()
    user_input3 = user_input3.lower()
    
    matches = df[
    (df['genre'].str.lower().str.contains(user_input2) | df['description'].str.lower().str.contains(user_input2)) &
    (df['genre'].str.lower().str.contains(user_input3) | df['description'].str.lower().str.contains(user_input3) | df['language'].str.lower().str.contains(user_input3))
]

if user_input1 and user_input3:
    user_input1 = user_input1.lower()
    user_input3 = user_input3.lower()
    
    matches = df[
    (df['genre'].str.lower().str.contains(user_input1) | df['description'].str.lower().str.contains(user_input1)) &
    (df['genre'].str.lower().str.contains(user_input3) | df['description'].str.lower().str.contains(user_input3) | df['language'].str.lower().str.contains(user_input3))
]

elif user_input1:
    user_input1 = user_input1.lower()
    matches = df[
        df['genre'].str.lower().str.contains(user_input1) |
        df['description'].str.lower().str.contains(user_input1)
    ]

elif user_input2:
    user_input2 = user_input2.lower()
    matches = df[
        df['genre'].str.lower().str.contains(user_input2) |
        df['description'].str.lower().str.contains(user_input2)
    ]
elif user_input3:
    user_input3 = user_input3.lower()
    matches = df[
        df['language'].str.lower().str.contains(user_input3) |
        df['genre'].str.lower().str.contains(user_input3) |
        df['description'].str.lower().str.contains(user_input3)
        ]

# Printing results
if not matches.empty:
    st.subheader("🔍 Based on your inputs, we recommend you these:")
    for _, row in matches.iterrows():
        st.markdown(
            f"**🎞️ {row['title']}**  \n"
            f"*Genre:* {row['genre']}  \n"
            f"*Description:* _{row['description']}_  \n"
            f"*Rating:* {row['rating']}  \n"
            f"*Available on:* {row['available on']}  \n"
            f"*Language:* {row['language']}   \n"
            f"*Run time:* {row['duration']}   \n"
            "---"
        )
else:
    st.warning("No exact matches found. Try different keywords!")

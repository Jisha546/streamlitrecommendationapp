import streamlit as st
import pandas as pd

# Load your data
recommendation_df = pd.read_csv("user_recommendations.csv")

# Set page config
st.set_page_config(page_title="Recommendation Dashboard", layout="wide")

# Title and intro
st.title("📊 Recommendation Dashboard")
st.markdown("""
Explore personalized item recommendations based on predicted ratings.
Select a user ID to view the items recommended for them.
""")

# User selection
user_list = recommendation_df['user_id'].unique()
selected_user = st.selectbox("Choose a user:", user_list)

# Filter data for selected user
user_data = recommendation_df[recommendation_df['user_id'] == selected_user]

# Show data
st.subheader(f"📌 Top Recommendations for {selected_user}")
st.dataframe(user_data.sort_values(by="predicted_rating", ascending=False))

# Optional: simple bar chart
st.bar_chart(user_data.set_index("item_id")["predicted_rating"])

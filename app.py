# app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Recommendation App", layout="centered")
st.title("🎯 Personalized Recommendation System")

# Upload predictions file
uploaded_file = st.file_uploader("📁 Upload your predictions CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("✅ File uploaded successfully!")
    st.write("### Sample Data Preview:")
    st.dataframe(df.head())

    # User selection
    users = df['user_id'].unique().tolist()
    selected_user = st.selectbox("👤 Select a User ID", users)

    # Filter top recommendations for selected user
    user_data = df[df['user_id'] == selected_user]

    if not user_data.empty:
        st.markdown("### 🎯 Recommended Items")

        # Sliders
        top_n_count = st.slider("Show Top N Recommendations", 1, 10, 5)
        min_rating = st.slider("Minimum predicted rating", 0.0, 5.0, 3.5, 0.1)

        filtered_data = user_data[user_data["predicted_rating"] >= min_rating]
        top_recommendations = filtered_data.sort_values(by="predicted_rating", ascending=False).head(top_n_count)

        st.dataframe(top_recommendations)

        # Chart
        st.write("### 📊 Visualization:")
        fig, ax = plt.subplots()
        sns.barplot(x='predicted_rating', y='item_id', data=top_recommendations, ax=ax, palette="viridis")
        ax.set_xlabel("Predicted Rating")
        ax.set_ylabel("Item ID")
        st.pyplot(fig)

        # Download button
        st.download_button(
            label="📥 Download recommendations as CSV",
            data=top_recommendations.to_csv(index=False),
            file_name=f"{selected_user}_recommendations.csv",
            mime="text/csv"
        )

        # Feedback
        st.markdown("### 📢 Give Feedback")
        st.text_area("How useful were these recommendations?")
    else:
        st.warning("No recommendations found for the selected user.")
else:
    st.info("Please upload a CSV file to get started.")

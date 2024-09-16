import streamlit as st
import pandas as pd
from data_preparation import load_and_preprocess_data
from embedding_generation import load_model
from query_processing import load_faiss_index, process_query

@st.cache_resource
def load_resources():
    df = load_and_preprocess_data('Hotel_dataset.csv')
    model = load_model()
    index = load_faiss_index('hotel_embeddings.index')
    return df, model, index

def main():
    st.title("Hotel Recommendation System")

    df, model, index = load_resources()

    user_query = st.text_input("Enter your hotel preferences:", "I want to book a hotel in New Delhi with 35 rooms and alcohol availability.")

    if st.button("Search"):
        results = process_query(model, index, user_query, df)
        
        st.subheader("Top 5 Recommended Hotels:")
        for _, hotel in results.iterrows():
            st.write(f"**{hotel['Hotel Name']}**")
            st.write(f"Location: {hotel['City']}, {hotel['State']}")
            st.write(f"Category: {hotel['Category']}")
            st.write(f"Alcohol: {hotel['Alcohol']}")
            st.write(f"Total Rooms: {hotel['Total Rooms']}")
            st.write("---")

if __name__ == "__main__":
    main()

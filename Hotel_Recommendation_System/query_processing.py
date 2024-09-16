import faiss
import numpy as np
import pandas as pd

def load_faiss_index(file_path):
    return faiss.read_index(file_path)

def process_query(model, index, query, df, k=2):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k=k)
    return df.iloc[I[0]]

if __name__ == "__main__":
    from data_preparation import load_and_preprocess_data
    from embedding_generation import load_model
    
    df = load_and_preprocess_data('Hotel_dataset.csv')
    model = load_model()
    index = load_faiss_index('hotel_embeddings.index')
    
    user_query = "I want to book a hotel in New Delhi with 35 rooms and alcohol availability."
    results = process_query(model, index, user_query, df)
    print(results)

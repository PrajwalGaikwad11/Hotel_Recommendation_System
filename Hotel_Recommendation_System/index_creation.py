import faiss
import numpy as np

def create_faiss_index(embeddings_np):
    embedding_dimension = embeddings_np.shape[1]
    index = faiss.IndexFlatL2(embedding_dimension)
    index.add(embeddings_np)
    return index

def save_faiss_index(index, file_path):
    faiss.write_index(index, file_path)

if __name__ == "__main__":
    from data_preparation import load_and_preprocess_data
    from embedding_generation import load_model, generate_embeddings, embeddings_to_numpy
    
    df = load_and_preprocess_data('Hotel_dataset.csv')
    model = load_model()
    embeddings = generate_embeddings(model, df['text_data'].tolist())
    embeddings_np = embeddings_to_numpy(embeddings)
    
    index = create_faiss_index(embeddings_np)
    save_faiss_index(index, 'hotel_embeddings.index')
    print("FAISS index created and saved.")

from sentence_transformers import SentenceTransformer
import numpy as np

def load_model(model_name='sentence-transformers/all-MiniLM-L6-v2'):
    return SentenceTransformer(model_name)

def generate_embeddings(model, text_data):
    return model.encode(text_data, convert_to_tensor=True)

def embeddings_to_numpy(embeddings):
    return embeddings.cpu().detach().numpy()

if __name__ == "__main__":
    from data_preparation import load_and_preprocess_data
    
    df = load_and_preprocess_data('Hotel_dataset.csv')
    model = load_model()
    embeddings = generate_embeddings(model, df['text_data'].tolist())
    embeddings_np = embeddings_to_numpy(embeddings)
    print(f"Embeddings shape: {embeddings_np.shape}")

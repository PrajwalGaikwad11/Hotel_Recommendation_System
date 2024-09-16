# 🏨 Hotel Recommendation System using RAG

## Overview
Welcome to the **Hotel Recommendation System**, powered by **Retrieval-Augmented Generation (RAG)**! This project is designed to help users find their ideal hotel based on personalized preferences like city, number of rooms, alcohol availability, and more. 🚀

Our system uses cutting-edge **FAISS** for efficient similarity searches, combined with a sleek, user-friendly **Streamlit** interface. Whether you're booking a luxury stay or a budget-friendly option, we've got you covered!

## Key Features
✨ **Data Preparation**: Hotel details are combined into a single, comprehensive text input—covering hotel name, location, category, rooms, and alcohol availability.  
✨ **Embeddings Generation**: We use `sentence-transformers/all-MiniLM-L6-v2` to generate dense embeddings from the hotel data for accurate recommendations.  
✨ **FAISS Indexing**: Efficiently stores embeddings for ultra-fast similarity-based retrieval.  
✨ **K-Means Clustering**: Retrieves top hotel recommendations that best match the user query.  
✨ **Streamlit UI**: Simple, interactive UI that makes finding the perfect hotel a breeze.

## Installation Guide

### Prerequisites
Ensure that **Python 3.8+** is installed before proceeding.

1. **Clone the Repository** 📂
   ```bash
   git clone https://github.com/PrajwalGaikwad11/hotel-recommendation-system.git

2. **Navigate to the project directory** 🚶

   ```bash
      cd hotel-recommendation-system

3. **Install the dependencies**📦

   ```bash
      pip install -r requirements.txt

4. **Run the Scripts Sequencially** (data_preparation.py-> embedding_generation.py-> index_creation.py-> query_processing.py-> aap.py)⚙️

   ```bash
      python {script_name}.py

5. **Run the Streamlit UI**💻 
   
   ```bash
      Streamlit run app.py

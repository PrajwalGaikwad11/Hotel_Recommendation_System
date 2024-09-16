# Hotel Recommendation System using RAG

## Overview
This project is a hotel recommendation system built using **Retrieval-Augmented Generation (RAG)**. The system is designed to help users find hotels based on their specific preferences such as city, number of rooms, alcohol availability, and more. The app uses **FAISS** for efficient similarity search, and **Streamlit** for an interactive user interface.

## Features
- **Data Preparation**: Combines hotel features (name, location, category, rooms, alcohol availability) into a single text input.
- **Embeddings Generation**: Uses the `sentence-transformers/all-MiniLM-L6-v2` model to generate embeddings for hotel data.
- **FAISS Indexing**: Efficient storage of embeddings for fast similarity-based retrieval.
- **Query Processing**: User enters a query, and the system retrieves top hotel recommendations using K-Means clustering.
- **Streamlit UI**: Interactive UI for querying and displaying results.

## Installation

### Prerequisites
Ensure you have Python 3.8+ installed on your system.

1. Clone the repository:

   ```bash
   git clone https://github.com/prajwal_Gaikwad/hotel-recommendation-system.git

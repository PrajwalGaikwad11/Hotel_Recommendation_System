import pandas as pd

def load_and_preprocess_data(file_path):
    # Load the CSV file
    df = pd.read_csv(file_path)
    
    # Combine relevant features into a single text input
    df['text_data'] = df['Hotel Name'] + " located in " + df['City'] + ". Category: " + df['Category'] + ". Alcohol: " + df['Alcohol'] + ". Total rooms: " + df['Total Rooms'].astype(str)
    
    return df

def save_metadata(df, output_file):
    df[['State', 'City', 'Category', 'Alcohol', 'Hotel Name', 'Address', 'Total Rooms']].to_csv(output_file, index=False)

if __name__ == "__main__":
    df = load_and_preprocess_data('Hotel_dataset.csv')
    print(df.head())
    print(df['text_data'].head())
    save_metadata(df, 'hotel_metadata.csv')

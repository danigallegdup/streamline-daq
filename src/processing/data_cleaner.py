import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)
    # Example preprocessing: handle missing values, standardize columns
    df = df.dropna()
    df['tag_label'] = df['tag_label'].map({'signal': 1, 'background': 0})
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == "__main__":
    clean_data('data/raw/ATLAS-top-tagging/your_dataset.csv', 'data/processed/cleaned_dataset.csv')

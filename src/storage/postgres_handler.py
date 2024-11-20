import psycopg2
import pandas as pd

def store_data_to_postgres(file_path):
    conn = psycopg2.connect("dbname=streamline user=postgres password=password")
    cursor = conn.cursor()
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO atlas_data (jet_pt, jet_eta, momentum_ratio, tag_label)
            VALUES (%s, %s, %s, %s)
            """,
            (row['jet_pt'], row['jet_eta'], row['momentum_ratio'], row['tag_label'])
        )
    conn.commit()
    conn.close()
    print("Data stored in PostgreSQL")

if __name__ == "__main__":
    store_data_to_postgres('data/processed/engineered_dataset.csv')

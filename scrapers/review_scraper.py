import pandas as pd

def load_reviews(csv_path):

    try:

        df = pd.read_csv(csv_path)

        print("CSV Columns:", df.columns.tolist())
        print(df.head())

        reviews = []

        first_column = df.columns[0]

        for review in df[first_column]:

            if pd.notna(review):

                reviews.append(
                    str(review).strip()
                )

        print("Loaded Reviews:", reviews)

        return reviews

    except Exception as e:

        print("CSV Loading Error:", e)

        return []
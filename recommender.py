import pandas as pd

class BookRecommender:
    def __init__(self, books_csv: str):
        # Load CSV and fill missing values
        self.df = pd.read_csv(books_csv).fillna("")
        # Ensure we can reference the necessary columns
        required_cols = ["Title", "Author", "Genre", "Mood", "Tags", "Notes", "Description"]
        for col in required_cols:
            if col not in self.df.columns:
                raise ValueError(f"Column '{col}' is missing from books.csv")
    
    def recommend(self, mood: str):
        # Return books matching mood (case-insensitive)
        mood = mood.lower()
        matched = self.df[self.df['Mood'].str.lower() == mood]
        
        # If no exact match, return top 5 books as fallback
        if matched.empty:
            matched = self.df.head(5)
        
        # Format output for frontend
        result = []
        for _, row in matched.iterrows():
            result.append({
                "Title": row["Title"],
                "Author": row["Author"],
                "Genre": row["Genre"],
                "Mood": row["Mood"],
                "Tags": row["Tags"],
                "Notes": row["Notes"],
                "Description": row["Description"]
            })
        return result

import os
import csv

# Create folder if it doesn't exist
folder_path = "datasets"
os.makedirs(folder_path, exist_ok=True)

# File path
file_path = os.path.join(folder_path, "ecommercereviews.csv")

# Data
reviews = [
   "Excellent quality and works exactly as expected.",
"Easy to use and very beginner-friendly.",
"Good value for the price compared to similar options.",
"Fast performance and reliable in daily use.",
"Customer support was helpful and responsive.",
"Clean design and overall pleasant experience.",
"The price feels a little high for the features offered.",
"Setup process was confusing at first.",
"Performance occasionally slows down during heavy use.",
"Some features are missing compared to competitors.",
"Customer support response time could be improved.",
"Durability seems average and could be better."
    
]

# Write CSV
with open(file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Header
    writer.writerow(["review"])
    
    # Rows
    for review in reviews:
        writer.writerow([review])

print(f"CSV file created at: {file_path}")
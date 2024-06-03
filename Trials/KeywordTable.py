import pandas as pd

# Path to the uploaded CSV file with highlighted work experience
csv_file_path = "/Users/utsavsharma/Desktop/RR/CleanedCSVs/highlighted_work_experience.csv"

# Load the CSV file
df = pd.read_csv(csv_file_path)

# Save the DataFrame as an HTML file
df.to_html("highlighted_work_experience.html")

print("Table saved as highlighted_work_experience.html. Open this file in a web browser to view the table.")

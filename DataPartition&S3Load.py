import csv
from collections import defaultdict

# Open the large CSV file
with open('large_file.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Create a dictionary to hold data for each date
    files_by_date = defaultdict(list)

    # Read each row and store it in the corresponding date file
    for row in reader:
        date = row['date_column']  # Change 'date_column' to your date column name
        files_by_date[date].append(row)

# Write out the smaller files
for date, rows in files_by_date.items():
    with open(f'{date}.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

#aws s3 cp /path/to/files s3://your-bucket-name --recursive

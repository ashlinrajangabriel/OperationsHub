import os
import csv

def split_csv(file_path, output_path, max_file_size):
    # Initialize variables
    file_number = 1
    current_size = 0
    header = None

    # Open the large CSV file
    with open(file_path, 'r', encoding='utf-8') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)  # Read the header row

        # Create the first output file
        output_file = open(os.path.join(output_path, f'split_{file_number}.csv'), 'w', encoding='utf-8', newline='')
        csvwriter = csv.writer(output_file)
        csvwriter.writerow(header)  # Write the header to the first file

        # Iterate over the rows in the large file
        for row in csvreader:
            row_str = ','.join(row) + '\n'  # Convert row to string
            row_size = len(row_str.encode('utf-8'))

            # Check if adding this row would exceed the max file size
            if current_size + row_size > max_file_size:
                # Close current file and start a new one
                output_file.close()
                file_number += 1
                output_file = open(os.path.join(output_path, f'split_{file_number}.csv'), 'w', encoding='utf-8', newline='')
                csvwriter = csv.writer(output_file)
                csvwriter.writerow(header)  # Write the header to the new file
                current_size = 0

            # Write the row and update the current size
            csvwriter.writerow(row)
            current_size += row_size

        output_file.close()

# Usage
split_csv('path/to/large_file.csv', 'path/to/output_directory', 50 * 1024 * 1024)  # 50 MB

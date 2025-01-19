import json
import csv

# Load the JSON data from the provided file
input_file_path = r"C:\Users\benbr\OneDrive\HAM Licence\Anki\ANKIV2\questions.json"
output_csv_path = r"C:\Users\benbr\OneDrive\HAM Licence\Anki\ANKIV2\questions.csv"
image_index_path = r"C:\Users\benbr\OneDrive\HAM Licence\Anki\ANKIV2\image_index.csv"

# Load JSON data
with open(input_file_path, 'r') as file:
    data = json.load(file)

# Load image index data
image_index = {}
with open(image_index_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # for each row, loop through each element in the row, except the first element, and map that element to the image filename
        for i in range(len(row)-1):
            image_index[row[i+1]] = row[0]

# Prepare CSV data with the required format
csv_data = [["Title Number", "Question Number", "Title", "Question", "Choice1", "Choice2", "Choice3", "Choice4", "Answer", "Image Filename"]]

title_number = 1
for section in data:
    title = section['Title']
    question_number = 1
    for question in section['Questions']:
        key = f"{title_number}.{question_number}"
        image_filename = image_index.get(key, "")  # Get the image filename if it exists, otherwise empty string
        row = [ 
            title_number,
            question_number,
            title,
            question['Question'],
            question['Choices'][0],
            question['Choices'][1],
            question['Choices'][2],
            question['Choices'][3],
            question['Answer'],
            image_filename
        ]
        csv_data.append(row)
        question_number += 1
    title_number += 1

# Write the CSV file
with open(output_csv_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

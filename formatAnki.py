import csv

def format_anki_questions(input_file, output_file, qtype=2, include_header=True):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = ['Question', 'Title', 'QType', 'Choice1', 'Choice2', 'Choice3', 'Choice4', 'Choice5', 'Answer', 'Sources', 'Extra 1', 'Tags']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        if include_header:
            writer.writeheader()
        
        for row in reader:
            title_number = row['Title Number']
            question_number = row['Question Number']
            question = row['Question']
            image_filename = row['Image Filename']
            
            if image_filename:
                question = f'{title_number}.{question_number} {question}<br><img src="{image_filename}">'
                # question = f'{title_number}.{question_number} {question}<br><img src=""{image_filename}"">'
                # question = f'"{question}"'
            else:
                question = f'{title_number}.{question_number} {question}'
            
            answer = row['Answer']
            one_hot_answer = ['0', '0', '0', '0']
            one_hot_answer[int(answer)] = '1'
            formatted_answer = ' '.join(one_hot_answer)
            
            formatted_row = {
                'Question': question,
                'Title': row['Title'],
                'QType': qtype,
                'Choice1': row['Choice1'],
                'Choice2': row['Choice2'],
                'Choice3': row['Choice3'],
                'Choice4': row['Choice4'],
                'Choice5': '',
                'Answer': formatted_answer,
                'Sources': '',
                'Extra 1': '',
                'Tags': row['Title']
            }
            
            writer.writerow(formatted_row)

def csv_to_txt(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
            open(output_file, mode='w', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        for row in reader:
            outfile.write('\t'.join(row) + '\n')


format_anki_questions('questions.csv', 'formatted_questions.csv', qtype=2, include_header=False)
csv_to_txt('formatted_questions.csv', 'formatted_questions.txt')
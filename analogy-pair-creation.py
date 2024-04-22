import os

def process_files_in_folder(folder_path):
    file_pairs = []
    first_pair_found = False
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if not line.startswith('#'):
                        line = line.strip().split(' ')[1].strip()
                        # print(line)
                        if not first_pair_found:
                            first_line = line
                            first_pair_found = True
                        else:
                            file_pairs.append(first_line + "::" + line)
    return file_pairs

testing_folder_path = 'D:\\MS\\COMP545\\project\\Investigating the Arithmetic of Visual Embeddings\\SemEval-2012-Gold-Ratings\\Testing'
training_folder_path = 'D:\\MS\\COMP545\\project\\Investigating the Arithmetic of Visual Embeddings\\SemEval-2012-Gold-Ratings\\Training'

testing_file_pairs = process_files_in_folder(testing_folder_path)
training_file_pairs = process_files_in_folder(training_folder_path)


all_pairs = []
all_pairs.extend(testing_file_pairs)
all_pairs.extend(training_file_pairs)

file_path = "Analogy-pairs.txt"

with open(file_path, 'w') as file:
    file.write(all_pairs)




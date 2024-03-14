import os
import glob
import re
import os
import requests
from bs4 import BeautifulSoup


def get_image_urls(query, num_images):
    search_url = f"https://www.google.com/search?q={query}&tbm=isch&hl=en"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_urls = []

    for img in soup.find_all('img'):
        if len(image_urls) == num_images:
            break
        if img.get('src'):
            image_urls.append(img.get('src'))

    return image_urls


def download_images(image_urls, save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url)
            file_path = os.path.join(save_dir, f"image_{i}.jpg")
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {file_path}")
        except Exception as e:
            print(f"Error downloading image: {e}")


def get_images(search_text, directory, num_images):
    image_urls = get_image_urls(search_text, num_images)
    download_images(image_urls, directory)


def process_file(file_path, folder_path):
    # with open(file_path, 'r') as file:
    #     for line in file:
    #         if not line.startswith('#'):
    #             parts = line.split()
    #             if len(parts) >= 2:
    #                 num, text = parts[0], ' '.join(parts[1:])
    #                 if 'king' in text.lower() or 'queen' in text.lower():
    #                     print(f"Found in: {folder_path}/{file_path}")

    concatenated_text = ""
    lines_read = 0
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith('#'):
                parts = line.split()
                if len(parts) >= 2:
                    num, text = parts[0], ' '.join(parts[1:])
                    concatenated_text += text.strip().replace(":", '_').replace('"', '') + "__"
                    lines_read += 1
                    if lines_read >= 2:
                        break

    if concatenated_text:
        folder_name = os.path.basename(file_path).split('.')[0]
        new_folder_path = os.path.join("Dataset", folder_name)
        os.makedirs(new_folder_path, exist_ok=True)
        sub_folder_path = os.path.join(new_folder_path, concatenated_text)
        os.makedirs(sub_folder_path, exist_ok=True)
        words = re.split(r'_|__', concatenated_text)
        for word in words:
            sub_sub_folder_path = os.path.join(sub_folder_path, word)
            get_images(word, sub_sub_folder_path, 50)


def process_folder(folder_path):
    for file_path in glob.glob(os.path.join(folder_path, '*.txt')):
        process_file(file_path, folder_path)
        

    for sub_folder in os.listdir(folder_path):
        sub_folder_path = os.path.join(folder_path, sub_folder)
        if os.path.isdir(sub_folder_path):
            process_folder(sub_folder_path)
            


# Path to the main 'data' folder
data_folder = 'SemEval-2012-Gold-Ratings'

# Process Training and Testing folders
for sub_folder in ['Training', 'Testing']:
    sub_folder_path = os.path.join(data_folder, sub_folder)
    process_folder(sub_folder_path)

# Investigating-the-Arithmetic-of-Visual-Embeddings

Image Dataset : https://drive.google.com/drive/folders/1S5zIpY8Tqayh_ln810Xa1CQ0LJsEug2i?usp=drive_link

## Description of files:
| File      | Description |
| ----------- | ----------- |
| Analogy-pairs.txt      | list of word pairs used in our study       |
| analogy-pair-creation.py  | Python script used for pre-processing of analogy pairs         |
| dataset-creation.py | Python script for creation of the image dataset   |
| evaluate-arithmetic-properties.ipynb | Helper functions for evaluating arithmetic properties |
| experiments.ipynb | Contains the experiments performed using different models |
| image_downloader.ipynb | script used to download images for the dataset |


## Models used
1. CLIP: https://huggingface.co/sentence-transformers/clip-ViT-B-32
2. Word2Vec: https://huggingface.co/fse/word2vec-google-news-300
3. ResNet50: https://huggingface.co/microsoft/resnet-50

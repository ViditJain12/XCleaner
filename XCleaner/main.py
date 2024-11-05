import os
import shutil
import fitz
import docx
from transformers import pipeline
import pandas as pd
from PIL import Image

COMMON_TEXT_FORMATS = ["pdf", "txt", "docx", "csv"]
IMAGE_EXTENSIONS = ["jpg", "jpeg", "png", "gif"]

class XCleaner:
    def __init__(self, directory, labels):
        self.directory = directory
        self.labels = labels
        self.file_data = []
        self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        self.image_classifier = pipeline("image-classification")

    def store_content(self, filepath, filetype):
        if filetype == "txt":
            with open(filepath, 'r') as file:
                return file.read()
        elif filetype == "pdf":
            with fitz.open(filepath) as pdf:
                return " ".join(page.get_text() for page in pdf)
        elif filetype == "docx":
            doc = docx.Document(filepath)
            return "\n".join(para.text for para in doc.paragraphs)
        elif filetype == "csv":
            df = pd.read_csv(filepath)
            return df.to_string(index=False)

    def read(self):
        for filename in os.listdir(self.directory):
            filepath = os.path.join(self.directory, filename)
            if os.path.isfile(filepath):
                filetype = filename.split('.')[-1].lower()
                if filetype in COMMON_TEXT_FORMATS:
                    content = self.store_content(filepath, filetype)
                    self.file_data.append({"filename": filename, "content": content, "path": filepath})
                elif filetype in IMAGE_EXTENSIONS:
                    self.file_data.append({"filename": filename, "path": filepath, "type": "image"})
    
    def classify_and_organize(self):
        for file in self.file_data:
            if 'content' in file:  # Text file
                content = file['content']
                classification = self.classifier(content, candidate_labels=self.labels)
                predicted_label = classification['labels'][0]  # Top prediction
            else:  # Image file
                image = Image.open(file['path'])
                classification = self.image_classifier(image)
                predicted_label = classification[0]['label']  # Top prediction
            
            # Organize files by moving them into corresponding folders
            label_folder = os.path.join(self.directory, predicted_label)
            os.makedirs(label_folder, exist_ok=True)
            shutil.move(file['path'], label_folder)

if __name__ == "__main__":
    dir = input("Enter File Path: ")
    labels = input("Enter Labels for Classification (Eg- School Work Research): ")
    labels = labels.split()
    clean = XCleaner(dir, labels)
    clean.read()
    clean.classify_and_organize()
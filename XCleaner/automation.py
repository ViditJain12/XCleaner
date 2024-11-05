import os
import shutil
import logging

SOURCE_DIR = ""                 # Fill with source directory path
AUDIO_DEST_DIR = ""             # Fill with audio directory path
VIDEO_DEST_DIR = ""             # Fill with video directory path
IMAGE_DEST_DIR = ""             # Fill with image directory path
DOCUMENTS_DEST_DIR = ""         # Fill with documents directory path

IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

VIDEO_EXTENSIONS = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

AUDIO_EXTENSIONS = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac", ".oga", ".mid", ".midi", ".amr"]

DOCUMENT_EXTENSIONS = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".md", ".rtf", ".csv", ".tex", ".epub", ".txt"]

def unique(dest, name):
    filename, extension = os.path.splitext(name)
    counter = 1
    while os.path.exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name

def move_file(dest, entry, name):
    if os.path.exists(f"{dest}/{name}"):
        unique_name = unique(dest, name)
        oldName = os.path.join(dest, name)
        newName = os.path.join(dest, unique_name)
        os.rename(oldName, newName)
    shutil.move(entry, dest)

class CleanFiles():
    def when_changed(self):
        with os.scandir(SOURCE_DIR) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio(entry, name)
                self.check_video(entry, name)
                self.check_image(entry, name)
                self.check_documents(entry, name)
    
    def check_audio(self, entry, name):
        for extensions in AUDIO_EXTENSIONS:
            if name.endswith(extensions) or name.endswith(extensions.upper()):
                move_file(AUDIO_DEST_DIR, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_video(self, entry, name):
        for extensions in VIDEO_EXTENSIONS:
            if name.endswith(extensions) or name.endswith(extensions.upper()):
                move_file(VIDEO_DEST_DIR, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_image(self, entry, name):
        for extensions in IMAGE_EXTENSIONS:
            if name.endswith(extensions) or name.endswith(extensions.upper()):
                move_file(IMAGE_DEST_DIR, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_documents(self, entry, name):
        for extensions in DOCUMENT_EXTENSIONS:
            if name.endswith(extensions) or name.endswith(extensions.upper()):
                move_file(DOCUMENTS_DEST_DIR, entry, name)
                logging.info(f"Moved document file: {name}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    CleanFiles().when_changed()

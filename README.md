# AI-Driven File Organization Tool

An intelligent file organizer leveraging NLP and machine learning to classify and organize system files into user-defined categories. This tool automatically moves and categorizes files in a specified directory based on content analysis, making file management more intuitive and efficient.

## Project Overview

This project automates file organization by:
- Monitoring a specified directory for newly added files.
- Moving files into folders based on their types (audio, video, image, document).
- Using NLP to analyze the content of text files and machine learning models to assign them to appropriate, user-defined categories.
- Categorizing files in real-time, making it easy to keep directories well-organized without manual intervention.

Currently, this tool supports text file classification and is set to expand to other file types in the future.

## Features

- **Automated File Movement**: Moves audio, video, image, and document files into designated folders.
- **Text File Classification**: Uses a pre-trained NLP model to classify text files (PDF, TXT, DOCX, CSV) into categories defined by the user.
- **Image Classification**: Detects and classifies image files (JPEG, PNG, GIF) based on visual content.
- **Customizable Categories**: Users can specify custom categories to classify files according to their needs.
- **Organized Storage**: Files are moved into respective folders based on classifications, reducing clutter.

## Requirements

- Python 3.7+
- Libraries:
  - `os`
  - `shutil`
  - `fitz` (PyMuPDF)
  - `docx`
  - `transformers`
  - `pandas`
  - `PIL` (Pillow)

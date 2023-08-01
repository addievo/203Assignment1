from main import get_text_file, read_file, process_text, count_words, bubble_sort, sort_words, print_words
import os
import string
from collections import defaultdict
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/', methods=['GET', 'POST'])
def index():
    sorted_words = None
    if request.method == 'POST':
        # Get the file from the POST request
        file = request.files['file']

        # Check if a file was provided and if it has the correct extension
        if file and file.filename.endswith('.txt'):
            # Save the uploaded file to a secure location
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Process the file
            all_words = []
            for line in read_file(file_path):
                words = process_text(line)
                all_words.extend(words)
            word_counts = count_words(all_words)
            sorted_words = sort_words(word_counts)


    # For both GET and POST requests, render the form and results (if any)
    return render_template('index.html', sorted_words=sorted_words)


if __name__ == '__main__':
    app.run(debug=True)

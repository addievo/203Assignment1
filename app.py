from main import get_text_file, read_file, process_text, count_words, bubble_sort, sort_words, print_words
import os
import string
from collections import defaultdict
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
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

            # Render the results
            return render_template('results.html', sorted_words=sorted_words)

        # If no file was provided or if it had the wrong extension,
        # flash an error message and redirect the user back to the form
        else:
            flash('Please upload a .txt file.')
            return redirect(url_for('index'))

    # For GET requests, render the form
    else:
        return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)

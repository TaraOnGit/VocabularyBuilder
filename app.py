from flask import Flask, render_template, request
from fetchwords import FetchWords

app = Flask(__name__)
fw = FetchWords()

@app.route('/')
def index():
    wl = fw.word_list()
    return render_template('index.html', word_list = wl)

@app.route('/get_synonyms', methods=['get'])
def get_synonyms():
    word = request.args.get('words')
    print(word)

    syn = fw.get_synonyms(word)
    return render_template('index.html', syn = syn)

app.run(debug=True)
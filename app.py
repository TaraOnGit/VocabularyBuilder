from flask import Flask, render_template, request, jsonify
from fetchwords import FetchWords

app = Flask(__name__)
fw = FetchWords()

@app.route('/')
def index():
    return render_template('index.html', )

@app.route('/api/vocabulary')
def vocabulary():
    words_dic = fw.word_list()
    return jsonify(words_dic)


@app.route('/api/synonyms')
def synonyms():
    wl = fw.word_list()
    return render_template('synonym.html', word_list = wl)


@app.route('/get_synonyms', methods=['get'])
def get_synonyms():
    word = request.args.get('words')
    print(word)

    syn = fw.get_synonyms(word)
    return render_template('index.html', syn = syn)

app.run(debug=True)
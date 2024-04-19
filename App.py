# dont forget to pip install gensim and story
from flask import Flask, request, jsonify, render_template
from gensim.summarization import summarize
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gen_plot', methods=['POST'])
def gen_plot():
    data = request.json
    genre = data.get('genre', '')
    setting = data.get('setting', '')
    characters = data.get('characters', '')
    detail = float(data.get('level of detail', 0.5))
    story = gen_story(genre, setting, characters)

    plot = gen_plot_helper(story, detail)
    return render_template('index.html', plot = plot, genre = genre, setting = setting, characters = characters, level_of_detail = detail)

def gen_story(genre, setting, characters):
    # added to by chatgpt + mine  (because i am simply not this creative)
    beginnings = ["Once upon a time", "In the beginning", "In a land not far from Claremont of", "In the lively city of", "In the bustling city of"]
    plot_twists = ["surprisingly", "tragically", "amazingly", "unsurprisingly (sarcasm ofc)", "after a long long journey"]
    resolutions = ["they discovered the power of teamwork!", "they achieved their hopes and dreams", "they discovered the power of friendship", "they learned a very valuable lesson", "they found true love"]

    story = f"{random.choice(beginnings)} in a {setting}, there lived {characters}. "
    story += f"{random.choice(characters)}'s life took a turn when {random.choice(plot_twists)}. "
    story += f"Despite the challenges, {random.choice(characters)} persevered, and in the end, {random.choice(resolutions)}."

    return story

def gen_plot_helper(story, level_of_detail = 0.5):
    if level_of_detail < 1: 
        plot_summary = summarize(story, ratio = level_of_detail)
        plot = plot_summary
    else:
        plot = story
    
    return plot

if __name__ == '__main__':
    app.run(debug = True)
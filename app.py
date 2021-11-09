from flask import Flask, render_template, request
app = Flask(__name__)
from stories import story


@app.route('/')
def get_prompt():
    '''Generate form words in prompt'''

    prompts = story.prompts
    return render_template('questions.html', prompts=prompts)

@app.route('/story')
def get_text():
    '''Show story result'''
    
    text = story.generate(request.args)
    return render_template('stories.html', text=text)
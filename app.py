from flask import Flask, request, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story as test

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

# debug = DebugToolbarExtension(app)


@app.route('/story-form')
def form_function():
    return render_template("form.html", questions=test.prompts)


@app.route('/story', methods=["POST"])
def populate_story():
    story = test
    # story = Story(
    #     QUESTIONS,
    #     """Once upon a time in a long-ago {place}, there lived a
    #         large {adjective} {noun}. It loved to {verb} {plural_noun}."""
    # )
    values = request.form
    the_story = story.generate(values)
    return the_story

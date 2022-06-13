from flask import Flask, request, render_template, session, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension

from boggle import Boggle
app = Flask(__name__)
boggle_game = Boggle()

app.config['SECRET_KEY'] = "2222"
debug = DebugToolbarExtension(app)


@app.route('/')
def homepage():
    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    return render_template("index.html", board=board, highscore=highscore, nplays=nplays)

# PERHAPS GO OVER THIS? COMPLETELY FORGOT ANYTHING RELATED TO JSON/AXIOS/AJAX
@app.route('/check-word')
def check_word():
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})

@app.route("/post-secure", methods=["POST"])
def post_score():

    score = request.json["score"]
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)
    session['nplays'] = nplays + 1
    session['highscore'] = max(score, highscore)
    
    return jsonify(brokeRecord=score > highscore)
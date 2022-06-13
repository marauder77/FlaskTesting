from flask import Flask, request, render_template, redirect, flash, session
# from flask_debugtoolbar import DebugToolbarExtension

from boggle import Boggle
app = Flask(__name__)
boggle_game = Boggle()

app.config['SECRET_KEY'] = "2222"
# debug = DebugToolbarExtension(app)


@app.route('/')
def homepage():
    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    return render_template("index.html", board=board, highscore=highscore, nplays=nplays)
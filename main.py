from flask import Flask
from random import randint

app = Flask(__name__)

computer_int = randint(0, 9)

print(computer_int)


@app.route('/')
def home():
    return '<style>body {background-color: #191919}</style>' \
           '<h1 style="text-align: center; color:#eeeeee">Guess a number between 0 and 9</h1>' \
           '<p style="text-align: center"><img style="align: center" ' \
           'src="https://media.giphy.com/media/xUn3CftPBajoflzROU/giphy.gif" width=400px><p> '


@app.route('/<int:guess>')
def num_guess(guess):
    if guess < computer_int:
        return '<style>body {background-color: #191919}</style>' \
               '<h1 style="text-align: center; color:blue">Too low, try again!</h1>' \
               '<p style="text-align: center"><img style="align: center" ' \
               'src="https://media.giphy.com/media/41g6S55zT5h9RpxgW0/giphy.gif" width=400px><p> ' \
 \
 \
    elif guess > computer_int:
        return '<style>body {background-color: #191919}</style>' \
               '<h1 style="text-align: center; color:green">Too high, try again!</h1>' \
               '<p style="text-align: center"><img style="align: center" ' \
               'src="https://media.giphy.com/media/PR3585ZZSvcHO9pa76/giphy.gif" width=400px><p> '

    else:
        return '<style>body {background-color: #191919}</style>' \
               '<h1 style="text-align: center; color:yellow">You guessed correct!</h1>' \
               '<p style="text-align: center"><img style="align: center" ' \
               'src="https://media.giphy.com/media/xT0xezQGU5xCDJuCPe/giphy.gif" width=400px><p> '


if __name__ == "__main__":
    app.run(debug=True)

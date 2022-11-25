from flask import Flask, render_template, request
from simple_recommender import recommend

app = Flask(__name__)

@app.route('/')
def hello_fun():
    return render_template("main.html", title1="Cascabel")


@app.route('/recommendations')
def recommender():
    user_input_from_app = request.args
    print('Is this working? Rating for movie1',request.args['movie1'])
    top3_films = recommend(user_input_from_app)
    return render_template("recommender.html", films_var = top3_films)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

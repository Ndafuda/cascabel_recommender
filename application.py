from flask import Flask, render_template, request
from nmf_recommender import recommend_nmf, films
from simple_recommender import recommend
from convert_arg import convert_args_dict

app = Flask(__name__)

@app.route('/')
def hello_fun():
    return render_template("main_test.html", title1="Cascabel", films=films)


@app.route('/recommendations')
def recommender():
    title = request.args.getlist('title')
    rating = request.args.getlist('rating')
    user_input = convert_args_dict(title, rating)
    recs = recommend_nmf(user_input)
    print(recs)
    return render_template("recommender.html", recs = recs)

 
if __name__ == '__main__':
    app.run(debug=True, port=5000)

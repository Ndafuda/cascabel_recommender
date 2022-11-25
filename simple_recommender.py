import random

films = ["Burnt by the Sun",
"Pulp Fiction",
"Ghostbusters",
"Star Trek",
"Day after Tomorrow"
]


def recommend(user_input_dict):
    random.shuffle(films)
    # Using nmf_mode together with user_input_dict to give recommendations to user.
    return films[:3]

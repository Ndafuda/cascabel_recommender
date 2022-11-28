import random
from read_movies import films


def recommend(user_input_dict):
    random.shuffle(films)
    # Using nmf_mode together with user_input_dict to give recommendations to user.
    return films[:10]

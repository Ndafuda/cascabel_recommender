import pandas as pd
import random
from read_movies import films
import pickle
import numpy as np


def recommend_nmf(new_user_ratings, k=8):    
    """Filters and recommends the top k movies for any given input query based 
    on a trained NMF model.

    Parameters
    ----------
    query : dict
        A dictionary of movies already seen. Takes the form {"movie_A": 3, "movie_B": 3} etc
    model : pickle
        pickle model read from disk
    k : int, optional
        no. of top movies to recommend, by default 10
    """
    # 1. candiate generation
        # construct a user vector
    vector = {}
    for movie in films:
        if movie not in new_user_ratings:
            vector[movie] = [0]
        else:
            vector[movie] = [new_user_ratings[movie]]
    new_user_vector = pd.DataFrame(vector)
   
    # 2. scoring  ### calculate the score with the NMF model
    model = pickle.load(open("../my_nmf_model.sav", "rb"))
    P_new_user = model.transform(new_user_vector)
    Q = model.components_
    R_new_user = np.dot(P_new_user, Q)
    new_user_df = pd.DataFrame(R_new_user,
                                index=['new_user'],
                                columns=films)
        
    # 3. ranking  ### set zero score to movies allready seen by the user
    for movie in new_user_df.columns:
        if movie in new_user_ratings:
            new_user_df[movie] = 0
        df = pd.DataFrame(new_user_df)
    top_k_recommendations = df.T.sort_values(by='new_user', ascending=False).head(10) 

    # return the top-k highst rated movie ids or titles
    
    return list(top_k_recommendations.index[:k])
if __name__=='__main__':
    user_input_dict= {'(500) Days of Summer (2009)': 3,
                    '10 Things I Hate About You (1999)': 3,
                '101 Dalmatians (1996)': 3,
                'Shawshank Redemption': 2,
                'Lord of the Rings':5,
                    'Star Wars': 5}
    print(recommend_nmf(user_input_dict))

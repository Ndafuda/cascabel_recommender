def convert_args_dict(titles, ratings):
    a_dict = {}
    for title, rating in zip(titles, ratings):
        a_dict[title] = int(rating)

    return a_dict

if __name__ == '__main__':
    title = ['101 Dalmatians (1996)', '12 Angry Men (1957)', '13th Warrior, The (1999)']
    rating = ['2', '3', '5']
    print(convert_args_dict(title, rating))

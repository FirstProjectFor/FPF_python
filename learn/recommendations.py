import math

critics = {
    'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 3.5,
                  'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5, 'Superman Returns': 5.0,
                     'The Night Listener': 3.0, 'You, Me and Dupree': 3.5},
    'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                         'Superman Returns': 3.5, 'The Night Listener': 4.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                     'The Night Listener': 4.5, 'Superman Returns': 4.0,
                     'You, Me and Dupree': 2.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                     'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
                     'You, Me and Dupree': 2.0},
    'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                      'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
    'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}}

critics_translate = {}
for person in critics.keys():
    for item in critics[person].keys():
        critics_translate.setdefault(item, {})
        critics_translate[item][person] = critics[person][item]


def similar_distance(data, name1, name2):
    """
    计算用户之间的相似度距离
    :param data: 数据
    :param name1: 用户1
    :param name2: 用户2
    :return:
    """
    same_movie_name_dict = {}
    for m, s in data[name2].items():
        if m in data[name1]:
            same_movie_name_dict[m] = 1
    if len(same_movie_name_dict) == 0:
        return 0

    movie_set = set()
    [movie_set.add(m) for m, s in data[name1].items()]
    [movie_set.add(m) for m, s in data[name2].items()]

    distance = 0
    for movie in movie_set:
        score_1 = 0
        if movie in data[name1]:
            score_1 = data[name1][movie]
        score_2 = 0
        if movie in data[name2]:
            score_2 = data[name2][movie]
        distance = distance + math.pow((score_1 - score_2), 2)

    return 1 / (1 + math.sqrt(distance))


def top_matchers(data, person, top_n, similar_function):
    similar_distance_value = [(similar_function(data, person, name), name) for name, movies in data.items() if
                              name != person]
    similar_distance_value.sort(reverse=True)
    return similar_distance_value[0:top_n]


def get_recommendations(data, person):
    similar_tuple = top_matchers(data, person, len(data) - 1, similar_distance)
    similar_sum = {}
    score_sum = {}
    movies_set = set()
    for person, movies in data.items():
        for movie in movies.keys():
            movies_set.add(movie)

    for similar, name in similar_tuple:
        for m in movies_set:
            if m not in similar_sum:
                similar_sum[m] = 0
            if m not in score_sum:
                score_sum[m] = 0
            if m in data[name]:
                similar_sum[m] = similar_sum[m] + int(data[name][m]) * similar
                score_sum[m] = score_sum[m] + similar
    recommendation_score = []
    for m in movies_set:
        recommendation_score.append((similar_sum[m] / score_sum[m], m))
    recommendation_score.sort(reverse=True)
    return recommendation_score


print(top_matchers(critics, 'Lisa Rose', 5, similar_distance))
print(get_recommendations(critics, 'Lisa Rose'))
print(get_recommendations(critics_translate, 'Lady in the Water'))
print(get_recommendations(critics, 'Jack Matthews'))

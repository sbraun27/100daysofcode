from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve


def named_tuples():
    user = ("bob", "coder")
    print(f"{user[0]} is {user[1]}")

    User = namedtuple("User", "role")
    user = User(name="bob", role="coder")

    print(f"User name is {user.name} and he is a {user.role}.")


def default_dict():
    users = {"bob": "coder"}
    users["julian"]  # KeyError here can use dict.get() which returns None

    challenges = [("mike", 10), ("julian", 7), ("bob", 5),
                  ("mike", 11), ("julian", 8), ("bob", 6)]
    challenges_done = defaultdict(list)
    for name, challenge in challenges_done:
        challenges[name].append(challenge)

    print(challenges)


def counter(words):
    return Counter(words).most_common(5)


def deque_notes():
    lst = list(range(10000000))

    deq = deque(range(10000000))

    def insert_and_delete(ds):
        for _ in range(10):
            index = random.choice(range(100))
            ds.remove(index)
            ds.insert(index, index)

        return ds

    # Deque performs at a fraction of the time than a list


def get_movie_data():
    directors = defaultdict(list)
    movies = namedtuple("Movie", "title year score")

    urlretrieve(
        "https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv", "movies.csv")

    with open("movies.csv", "r", encoding="utf-8") as f:
        for line in csv.DictReader(f):
            try:
                director = line["director_name"]
                movie = line["movie_title"].replace("/xa0", "")
                year = int(line["title_year"])
                score = float(line["imdb_score"])
            except ValueError:
                continue

            directors[director].append(movies(movie, year, score))

    return directors


def get_most_common(dictionary, number_to_get=5):
    cnt = Counter()
    for director, data in dictionary.items():
        cnt[director] += len(data)

    return cnt.most_common(number_to_get)


if __name__ == "__main__":
    directors = get_movie_data()
    print(get_most_common(directors, 10))

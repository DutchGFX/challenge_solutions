import pandas as pd


def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    # find the user(s) who rated the most movies
    users_most = movie_rating.groupby("user_id").count().nlargest(1, "rating", "all")

    # get the name of the user
    user = users.set_index("user_id").loc[users_most.index].sort_values("name")["name"].iloc[0]

    # select from February, groupby, take average rating, take the max
    mask = (movie_rating["created_at"] >= "2020-02-01") & (movie_rating["created_at"] < "2020-03-01")
    movie_best = movie_rating[mask].groupby("movie_id").mean().nlargest(1, "rating", "all")
    movie = movies.set_index("movie_id").loc[movie_best.index].sort_values("title")["title"].iloc[0]

    # create and output DataFrame
    results = pd.DataFrame([user, movie], columns=["results"])
    return results

"""machine-learning Code that returns movies"""
import random

MOVIES = ['Karate Kid',
          'Toy Story 1',
          'Toy Story 2',
          'Toy Story 3',
          'Toy Story 4',
          'Star Wars 1',
          'Star Wars 2',
          'Star Wars 3',
          'Star Wars 4',
          'Star Wars 5',
          'Star Wars 6',
          'Jurassic Park',
          'Dawn of the Dead',
          'Home Alone']

def random_recommend(num):
    """Simple recommender that return N movies. Wow!
    """
    result = random.sample(MOVIES, k=num)
    return result

def nmf():
    ...

def deep_recommend():
    ...

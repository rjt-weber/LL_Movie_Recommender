"""machine-learning Code that returns movies"""
import random

MOVIES = ['Karate Kid',
          'Toy Story 1',
          'Toy Story 2',
          'Toy Story 3',
          'Mulan',
          'Star Wars 1',
          'Star Wars 2',
          'Star Wars 3',
          'Star Wars 4',
          'Star Wars 5',
          'Blair Witch Project',
          'Jurassic Park',
          'Dawn of the Dead',
          'Home Alone']

def random_recommend(num):
    """Simple recommender that return random movies. Wow!
    """
    result = random.choices(MOVIES, k=num, replace = False)
    return result

def best_recommender_ever():
    ...

def at_least_better_than_netflix():
    ...

"""machine-learning Code that returns movies"""
import random
import numpy as np

MOVIES = ['Toy Story 1',
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
          'Home Alone',
          'A Million ways to die in the west',
          'Blade Runner 2049',
          'Cats',
          'Dune',
          'Eurovision Song Contest: The Story Of Fire Saga',
          'Gattaca',
          'Green Mile',
          'Harry Potter and the deathly hallows ',
          'Hidden Figures',
          'High School Musical',
          'High School Musical 2',
          'Ice Age',
          'Inside Out',
          'Karate Kid (1984)',
          'Lord of the Rings -- The Fellowship of the Ring',
          'Lord of the Rings -- The Return of the King',
          'Lord of the Rings -- The Two Towers',
          'Matrix',
          'Memento',
          'Moana',
          'Red Joan',
          "Romy and Michelle's High School Reunion",
          'Se7en',
          'Sharknado',
          'Shoplifters',
          'Shutter Island',
          'Smiley Face',
          'Ted',
          'The Big Lebowksi',
          'The Big Lebowski',
          'The Body of Truth',
          'The Breakfast Club',
          'The Empire strikes back',
          'The Farewell',
          'The Notebook',
          'The Sixth Sense',
          'What happened to Monday']

ranges =list(np.arange(1, step=.02))

probs = random.sample(ranges, k=len(MOVIES))


def random_recommend(num):
    """Simple recommender that return random movies. Wow!
    """
    result = random.choices(MOVIES, k=num, weights=probs)
    return result

def nmf():
    ...

def deep_recommend():
    result = random.choices(MOVIES, k=num, replace = False)
    return result

def best_recommender_ever():
    ...

def at_least_better_than_netflix():
    ...

#####################################################################################################################################################
######################################################################## INFO #######################################################################
#####################################################################################################################################################

"""
    This script runs the challenge between the rat and the python program.
    It is given to you so that you can test your programs before submitting them.
    It performs two analyses: a quick average analysis and a formal 1 sample T test.
"""

#####################################################################################################################################################
###################################################################### IMPORTS ######################################################################
#####################################################################################################################################################

# Import PyRat
from pyrat import *

# External imports
import matplotlib.pyplot as pyplot
import scipy.stats
import numpy
import types
import tqdm
import sys
import os
import pathlib

# Import the greedy AI as the second program, your opponent
lab_commons_path = os.path.join(pathlib.Path(__file__).parent.resolve(), '../')
if lab_commons_path not in sys.path:
    sys.path.append(lab_commons_path) 
import lab_commons.AI.greedy as program_2

# Import Your AI as the first program
import your_AI as program_1

#####################################################################################################################################################
############################################################### VARIABLES & CONSTANTS ###############################################################
#####################################################################################################################################################

"""
    Number of games to make.
"""

NB_GAMES = 5 # 1000 # 5 if you want to test the script, 1000 if you want to run the challenge in real conditions.

#####################################################################################################################################################

"""
    Games configuration.
"""

MAZE_WIDTH = 7
MAZE_HEIGHT = 5
MUD_PERCENTAGE = 0.0
WALL_PERCENTAGE = 0.0
CELL_PERCENTAGE = 100.0
NB_CHEESE = 10

#####################################################################################################################################################
##################################################################### FUNCTIONS #####################################################################
#####################################################################################################################################################

def run_one_game ( seed:      int,
                   program_1: types.ModuleType,
                   program_2: types.ModuleType
                 ) ->         Dict[str, Any]:

    """
        This function runs a PyRat game, with no GUI, for a given seed and program, and returns the obtained stats.
        In:
            * seed:      Random seed used to create the game.
            * program_1: First program to use in that game.
            * program_2: Second program to use in that game.
        Out:
            * stats: Statistics output at the end of the game.
    """

    # Map the functions to the character
    players = [{"name": program_1.__name__,
                    "team": "1",
                    "preprocessing_function": program_1.preprocessing if "preprocessing" in dir(program_1) else None,
                    "turn_function": program_1.turn,
                    "postprocessing_function": program_1.postprocessing if "postprocessing" in dir(program_1) else None},
               {"name": program_2.__name__,
                    "team": "2",
                    "preprocessing_function": program_2.preprocessing if "preprocessing" in dir(program_2) else None,
                    "turn_function": program_2.turn,
                    "postprocessing_function": program_2.postprocessing if "postprocessing" in dir(program_2) else None}]

    # Customize the game elements
    config = {"maze_width": MAZE_WIDTH,
              "maze_height": MAZE_HEIGHT,
              "mud_percentage": MUD_PERCENTAGE,
              "cell_percentage": CELL_PERCENTAGE,
              "wall_percentage":WALL_PERCENTAGE,
              "nb_cheese": NB_CHEESE,
              "game_mode" : "sequential",
              "preprocessing_time" : 0.0,
              "turn_time" : 0.0,
              "render_mode": "no_rendering",
              "random_seed": seed}

    # Start the game
    game = PyRat(players, **config)
    stats = game.start()
    return stats
    
#####################################################################################################################################################
######################################################################## GO! ########################################################################
#####################################################################################################################################################

if __name__ == "__main__":

    # Run multiple games
    results = []
    for seed in tqdm.tqdm(range(NB_GAMES), desc="Game", position=0, leave=False):
        
        # Store score difference as result
        stats = run_one_game(seed, program_1, program_2)
        results.append(int(stats["players"][program_1.__name__]["score"] - stats["players"][program_2.__name__]["score"]))
        
    # Show results briefly
    print("#" * 20)
    print("#  Quick analysis  #")
    print("#" * 20)
    rat_victories = [score for score in results if score > 0]
    python_victories = [score for score in results if score < 0]
    nb_draws = NB_GAMES - len(rat_victories) - len(python_victories)
    print(program_1.__name__, "(rat)   <-  ", len(rat_victories), "  -  ", nb_draws, "  -  ", len(python_victories), "  ->  ", program_2.__name__, "(python)")
    print("Average score difference when %s wins:" % program_1.__name__, numpy.mean(rat_victories) if len(rat_victories) > 0 else "n/a")
    print("Average score difference when %s wins:" % program_2.__name__, numpy.mean(numpy.abs(python_victories))if len(python_victories) > 0 else "n/a")

    # More formal statistics to check if the mean of the distribution is significantly different from 0
    print("#" * 21)
    print("#  Formal analysis  #")
    print("#" * 21)
    test_result = scipy.stats.ttest_1samp(results, popmean=0.0)
    print("One sample T-test of the distribution:", test_result)

    # Visualization of histograms of score differences
    bins = range(min(results), max(results) + 2)
    pyplot.figure(figsize=(20, 10))
    pyplot.hist(results, ec="black", bins=bins)
    pyplot.title("Analysis of the game results in terms of victory margin")
    pyplot.xlabel("score(%s) - score(%s)" % (program_1.__name__, program_2.__name__))
    pyplot.xticks([b + 0.5 for b in bins], labels=bins)
    pyplot.xlim(bins[0], bins[-1])
    pyplot.ylabel("Number of games")
    pyplot.show()
    
#####################################################################################################################################################
#####################################################################################################################################################

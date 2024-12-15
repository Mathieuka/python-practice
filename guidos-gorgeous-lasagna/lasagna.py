"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 20

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.
def preparation_time_in_minutes(qty_of_layers):
    """Calculate the preparation time in minutes.

   :param qty_of_layers: int - the number of layers in the lasagna.
   :return: int - total preparation time (in minutes) based on 2 minutes per layer.

   Function that calculates the preparation time by multiplying the number of
   layers by the time it takes to prepare each layer (2 minutes).
    """
    return qty_of_layers * 2



#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(qty_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time in minutes.

    :param qty_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes) including preparation and baking.

    Function that sums the preparation time and the elapsed baking time to
    provide the total time spent on the lasagna so far.
    """
    return (qty_of_layers * 2) + elapsed_bake_time

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)

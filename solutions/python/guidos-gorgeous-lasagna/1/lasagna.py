"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    return EXPECTED_BAKE_TIME - elapsed_bake_time


# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time in minutes.
    
    :param number_of_layers : int - number of lasagna layers to prepare.
    :return: int - total preparation time(in minutes).
    
    This function takes number of layers you want add to the lasagna
    and return how many minutes you would spend making them, assuming each
    layer takes PREPARATION_TIME minutes to prepare.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Calculate total time spend cooking.
    
    :param number_of_layers: int - number of layers you prepared.
    :param elapsed_back_time: int- baking time is already.
    :return: int - total time (in minutes) spent cooking.

    This function sums up the preparation time and the baking time to give 
    the total time you have been in the kitchen cooking.
    """
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time

#  (you can copy and then alter the one from bake_time_remaining.)

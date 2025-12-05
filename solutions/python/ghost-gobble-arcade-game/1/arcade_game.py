"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active:bool, touching_ghost:bool)->bool:
    """Return True if Pac-Man can eat a ghost."""
    return power_pellet_active and touching_ghost

def score(touching_power_pellet:bool, touching_dot:bool)->bool:
    """Return True if Pac-Man scores by touching a pellet or a dot."""
    return touching_power_pellet or touching_dot
    
def lose(power_pellet_active:bool, touching_ghost:bool)->bool:
    """Return True if Pac-Man loses when touching a ghost without a power pellet."""
    return touching_ghost and not power_pellet_active

def win(has_eaten_all_dots:bool, power_pellet_active:bool, touching_ghost:bool)->bool:
    """Return True if Pac-Man wins by eating all dots without losing."""
    return has_eaten_all_dots and not lose(power_pellet_active,touching_ghost)

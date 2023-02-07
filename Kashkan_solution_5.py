#!/usr/bin/python3

class Warrior():
    """ 
    Class Warrior represents a warrior character in a game or similar setting.
    It has attributes name, maximum_health, and is_alive, which indicate the name of the warrior,
    the maximum health that the warrior can have, and whether the warrior is alive or not, respectively.

    """
    def __init__(self, name, maximum_health):
        """Initalizing an object with obligatory name and maximum_health parameters

        Args:
            name (str): Name of warrior
            maximum_health (int): Maximum health value of warrior.

        Raises:
            ValueError: If the given maximum health value is not an integer or is negative.

        """
        self.name = name
        if maximum_health >= 0 and isinstance(maximum_health, int):
        # let's presume we can create dead-already hero (a legend from a day gone)
            self._maximum_health = maximum_health
        else:
            raise ValueError("Invalid health value!")
        self._is_alive = self._maximum_health > 0      
            
    @property
    def maximum_health(self):
        """int: Getter of the maximum health value of the warrior."""
        return self._maximum_health
    
    @maximum_health.setter
    def maximum_health(self, value):
        """Set the maximum health value of the warrior.

        Args:
            value (int): The new maximum health value.

        Raises:
            ValueError: If the given value is not an integer.

        """
        if isinstance(value, int):
            self._maximum_health = value
        else:
            raise ValueError("Invalid health value!")
        self._is_alive = self._maximum_health > 0     
        
    @property
    def is_alive(self):
        """bool: Getter for _is_alive attribute, which indicates 
        whether the warrior is alive or not."""
        self._is_alive = self._maximum_health > 0
        return self._is_alive

        
    def __sub__(self, other):
        """Warriors fight each other, causing each warrior's maximum_health to decrement by 1.

        Args:
            other (Warrior): Another warrior to fight.

        Raises:
            TypeError: If the argument passed is not a Warrior object.

        """
        if isinstance(other, Warrior) is False:
            raise TypeError("Warriors can only figth each other")
        if self._is_alive is True and other._is_alive is True:
            self._maximum_health -=1
            other._maximum_health -=1
            self._is_alive = self._maximum_health > 0
            other._is_alive = other._maximum_health > 0
        else:
            return None              
    
            
    def __add__(self, other):
        """Combine two warriors into one, with their maximum health values summed.

        Args:
            other (Warrior): Another warrior to combine with.

        Returns:
            Warrior: A new warrior with the combined attributes of both warriors.

        """
        if self._is_alive is True and other._is_alive is True:
            return Warrior(self.name +" "+ other.name, self.maximum_health + other.maximum_health)
        else:
            return None
    
    
    def __str__(self):
        """Writes information about current warrior in format:
        Warrior(name="{name}", maximum_health={}, is_alive={})
        """
        # this kind of information is better served with __repr__()
        warrior_status = f'Warrior(name="{self.name}", maximum_health={self.maximum_health}, is_alive={self._is_alive})'
        return warrior_status

if __name__ == "__main__":
    # I have a pen...
    pen = Warrior("Pen", 2)
    str(pen)
    # I have an apple...
    apple = Warrior("Apple", 2)
    print(apple)
    # plop!
    print(apple + pen)
    # I have a pen, and a pineapple:
    pineapple = Warrior("Pineapple", 2)
    print(pineapple)
    # plop!
    child_of_love = pen + pineapple + apple + pen

    
    # P.S
    pineapple - apple
    print(pineapple)
    if pineapple.is_alive:
        print("Pine!")
    else:
        print("Ouch!")

    
        
    
              
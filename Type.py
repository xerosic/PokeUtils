from abc import ABC, abstractmethod

class PokemonType(ABC):
    """
    Abstract base class for all entities, this must not be instantiated
    directly! Inherit from it and override all of its methods instead
    """

    def __init__(self):
        self.name = self.__class__.__name__

    def __str__(self):
        return f"Type: {self.name}\n\nWeak to: {', '.join(str(x) for x in self.Weakness())}.\nNormal damage: {', '.join(str(x) for x in self.Normal())}.\nResist to: {', '.join(str(x) for x in self.Resistance())}.\nImmune to: {', '.join(str(x) for x in self.Immunity())}."

    @abstractmethod
    def Weakness(self):
        """
        Returns the type(s) from which this type receive double damage. Must be overridden
        """
        
        raise NotImplementedError

    @abstractmethod
    def Resistance(self):
        """
        Returns the type(s) from which this type receive less damage. Must be overridden
        """

        raise NotImplementedError

    @abstractmethod
    def Immunity(self):
        """
        Returns the type(s) from which this type receive no damage. Must be overridden
        """
        
        raise NotImplementedError
    
    @abstractmethod
    def Normal(self):
        """
        Returns the type(s) from which this type receive normal damage. Must be overridden
        """
        
        raise NotImplementedError

#
#       Sub-classes for the specific pokemon type
#

class Normal(PokemonType):
    
    """
    Class for the Normal type
    """

    def Weakness(self):
        return ["Fighting"]

    def Normal(self):
        return ["Steel", "Water", "Dark", "Dragon", "Fairy", "Fire", "Normal", "Psychic", "Poison", "Flying", "Electric", "Ice", "Rock", "Ground", "Bug", "Grass"]

    def Resistance(self):
        return ["No type"]

    def Immunity(self):
        return ["Ghost"]

class Fire(PokemonType):
    
    """
    Class for the Fire type
    """

    def Weakness(self):
        return ["Water", "Rock", "Ground"]

    def Normal(self):
        return ["Dark", "Dragon", "Electric", "Fighting", "Normal", "Psychic", "Ghost", "Poison", "Flying"]

    def Resistance(self):
        return ["Steel", "Bug", "Grass", "Fairy", "Fire", "Ice"]

    def Immunity(self):
        return ["No type"]

class Fighting(PokemonType):

    """
    Class for the Fighting type
    """

    def Weakness(self):
        return ["Fairy", "Psychic", "Flying"]

    def Normal(self):
        return ["Steel", "Water", "Dragon", "Electric", "Grass", "Fire", "Ice", "Fighting"]

    def Resistance(self):
        return ["Rock", "Bug", "Dark"]

    def Immunity(self):
        return ["No type"]

class Water(PokemonType):

    """
    Class for the Water type
    """

    def Weakness(self):
        return ["Electric", "Grass"]

    def Normal(self):
        return ["Dark", "Bug", "Dragon", "Fairy", "Fighting", "Normal", "Psychic", "Rock", "Ghost", "Ground", "Poison", "Flying"]

    def Resistance(self):
        return ["Steel", "Water", "Fire", "Ice"]

    def Immunity(self):
        return ["No type"]

class Flying(PokemonType):
    
    """
    Class for the Flying type
    """

    def Weakness(self):
        return ["Electric", "Ice", "Rock"]

    def Normal(self):
        return ["Steel", "Water", "Dark", "Dragon", "Fairy", "Fire", "Normal", "Psychic", "Ghost", "Poison", "Flying"]

    def Resistance(self):
        return ["Bug", "Grass", "Fighting"]

    def Immunity(self):
        return ["Ground"]

class Grass(PokemonType):
    
    """
    Class for the Grass type
    """

    def Weakness(self):
        return ["Bug", "Fire", "Ice", "Poison", "Flying"]

    def Normal(self):
        return ["Steel", "Dark", "Dragon", "Fairy", "Fighting", "Normal", "Psychic", "Rock", "Ghost"]

    def Resistance(self):
        return ["Water", "Electric", "Grass", "Ground"]

    def Immunity(self):
        return ["No type"]

class Poison(PokemonType):
    
    """
    Class for the Poison type
    """

    def Weakness(self):
        return ["Psychic", "Ground"]

    def Normal(self):
        return ["Steel", "Water", "Dark", "Dragon", "Electric", "Fire", "Ice", "Normal", "Rock", "Ghost", "Flying"]

    def Resistance(self):
        return ["Bug", "Fairy", "Grass", "Fighting", "Poison"]

    def Immunity(self):
        return ["No type"]

class Electric(PokemonType):
    
    """
    Class for the Electric type
    """

    def Weakness(self):
        return ["Ground"]

    def Normal(self):
        return ["Water", "Bug", "Dark", "Dragon", "Grass", "Fairy", "Fire", "Ice", "Fighting", "Normal", "Flying"]

    def Resistance(self):
        return ["Steel", "Electric", "Flying"]

    def Immunity(self):
        return ["No type"]

class Ground(PokemonType):
    
    """
    Class for the Ground type
    """

    def Weakness(self):
        return ["Water", "Grass", "Ice"]

    def Normal(self):
        return ["Steel", "Dark", "Bug", "Fairy", "Dragon", "Fire", "Psychic", "Normal", "Ghost", "Fighting", "Ground", "Flying"]

    def Resistance(self):
        return ["Rock", "Poison"]

    def Immunity(self):
        return ["Electric"]

class Psychic(PokemonType):
    
    """
    Class for the Psychic type
    """

    def Weakness(self):
        return ["Steel", "Bug", "Ghost"]

    def Normal(self):
        return ["Steel", "Water", "Dragon", "Electric", "Grass", "Fairy", "Fire", "Ice", "Normal", "Rock", "Ground", "Poison", "Flying"]

    def Resistance(self):
        return ["Fighting", "Psychic"]

    def Immunity(self):
        return ["No type"]

class Rock(PokemonType):
    
    """
    Class for the Rock type
    """

    def Weakness(self):
        return ["Steel", "Water", "Grass", "Fighting", "Ground"]

    def Normal(self):
        return ["Dark", "Bug", "Dragon", "Electric", "Fairy", "Ice", "Psychic", "Rock", "Ghost"]

    def Resistance(self):
        return ["Fire", "Normal", "Poison", "Flying"]

    def Immunity(self):
        return ["No type"]

class Ice(PokemonType):
    
    """
    Class for the Ice type
    """

    def Weakness(self):
        return ["Steel", "Fire", "Fighting", "Rock"]

    def Normal(self):
        return ["Water", "Dark", "Bug", "Dragon", "Electric", "Grass", "Fairy", "Normal", "Psychic", "Ghost", "Ground", "Poison", "Flying"]

    def Resistance(self):
        return ["Ice"]

    def Immunity(self):
        return ["No type"]

class Bug(PokemonType):
    
    """
    Class for the Bug type
    """

    def Weakness(self):
        return ["Fire", "Rock", "Flying"]

    def Normal(self):
        return ["Steel", "Water", "Dark", "Bug", "Dragon", "Electric", "Fairy", "Ice", "Normal", "Psychic", "Ghost", "Poison"]

    def Resistance(self):
        return ["Grass", "Fighting", "Ground"]

    def Immunity(self):
        return ["No type"]

class Dragon(PokemonType):
    
    """
    Class for the Dragon type
    """

    def Weakness(self):
        return ["Dragon", "Fairy", "Ice"]

    def Normal(self):
        return ["Steel", "Dark", "Fighting", "Bug", "Normal", "Psychic", "Rock", "Ghost", "Ground", "Poison", "Flying"]

    def Resistance(self):
        return ["Water", "Electric", "Grass", "Fire"]

    def Immunity(self):
        return ["No type"]

class Ghost(PokemonType):
    
    """
    Class for the Ghost type
    """

    def Weakness(self):
        return ["Dark", "Ghost"]

    def Normal(self):
        return ["Steel", "Water", "Dragon", "Electric", "Grass", "Fairy", "Fire", "Ice", "Psychic", "Rock", "Flying"]

    def Resistance(self):
        return ["Bug", "Poison"]

    def Immunity(self):
        return ["Fighting", "Normal", "Ground"]

class Dark(PokemonType):
    
    """
    Class for the Dark type
    """

    def Weakness(self):
        return ["Bug", "Fairy", "Fighting"]

    def Normal(self):
        return ["Steel", "Water", "Dragon", "Electric", "Grass", "Fire", "Ice", "Normal", "Rock", "Ground", "Poison", "Flying"]

    def Resistance(self):
        return ["Dark", "Ghost"]

    def Immunity(self):
        return ["Psychic"]

class Steel(PokemonType):
    
    """
    Class for the Steel type
    """

    def Weakness(self):
        return ["Fire", "Fighting", "Ground"]

    def Normal(self):
        return ["Water", "Dark", "Electric", "Ghost"]

    def Resistance(self):
        return ["Steel", "Bug", "Ice", "Normal", "Rock", "Psychic", "Flying", "Grass", "Fairy", "Dragon"]

    def Immunity(self):
        return ["Poison"]

class Fairy(PokemonType):
    
    """
    Class for the Fairy type
    """

    def Weakness(self):
        return ["Steel", "Poison"]

    def Normal(self):
        return ["Water", "Electric", "Grass", "Fairy", "Fire", "Ice", "Normal", "Psychic", "Rock", "Ghost", "Ground", "Flying"]

    def Resistance(self):
        return ["Dark", "Bug", "Fighting"]

    def Immunity(self):
        return ["Dragon"]
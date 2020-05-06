from unit import Player, Enemy
from helpers import clamp
from ability import Heal, Damage
from effect import Effect
from food import Food
from zone import Zone, Intro

introtext = "Welcome to Dean's Gains Adventure!\nYou will play as Dean, a man in desparate search of GAINS!\nOver the course of this adventure, you will progress through multiple zones filled with enemies, fighting your way past each one and consuming the food they drop to make GAINS."

pb = Food("Jar of peanut butter", 0, 1, 0)

none = Effect("None", "No effect")

kick = Damage("Kick", "A zero cost basic attack.", 1, 0)

player = Player("Player", 20, 20, 1, [kick], [])

trout = Enemy("Ellis", 5, 100, 1, [kick], [pb])

intro = Intro("Intro", introtext)

zone1 = Zone("The Squires Swamps", "You are now entering the Squires Swamps. Your first opponent is Trout!", [trout])

intro.intro()
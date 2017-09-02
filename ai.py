#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################################################
#
# Pure random A.I, you may NOT use it to win ;-)
#
########################################################################

import random
import numpy as np


class AI:
    """Pure random A.I, you may NOT use it to win ;-)"""

    def __init__(self):
        self.Actions = ["North", "East", "South", "West", "Stay"]
        self.Q = None
        self.lr = .8
        self.y = .95
        self.rList = []
        self.action = None
        self.state = None
        pass

    def process(self, game, state):
        if self.state != None:
            self.Q[int(state['hero']['gold']), self.action] = self.Q[int(state['hero']['gold']), self.action] + self.lr * ( self.reward(state, game) + self.y * np.max(self.Q[int(state['hero']['gold']),:]) - self.Q[int(self.state['hero']['gold']), self.action])
        else:
            self.Q = np.zeros([game.board_size * game.board_size, 5])
        self.state = state
        self.game = game

    def decide(self):
        self.rAll = 0
        a = np.argmax(self.Q[int(self.state['hero']['gold']), :] + np.random.randn(1, 5)
                      * (1. / (int(self.game.turn) + 1)))
        
        self.action = a
        return self.Actions[a]

        """Must return a tuple containing in that order:
          1 - path_to_goal :
                  A list of coordinates representing the path to your
                 bot's goal for this turn:
                 - i.e: [(y, x) , (y, x), (y, x)]
                 where y is the vertical position from top and x the
                 horizontal position from left.

          2 - action:
                 A string that will be displayed in the 'Action' place.
                 - i.e: "Go to mine"

          3 - decision:
                 A list of tuples containing what would be useful to understand
                 the choice you're bot has made and that will be printed
                 at the 'Decision' place.

          4- hero_move:
                 A string in one of the following: West, East, North,
                 South, Stay

          5 - nearest_enemy_pos:
                 A tuple containing the nearest enenmy position (see above)

          6 - nearest_mine_pos:
                 A tuple containing the nearest enenmy position (see above)

          7 - nearest_tavern_pos:
                 A tuple containing the nearest enenmy position (see above)"""

    def reward(self, state, game):
        if(self.state['hero']['pos'] == state['hero']['pos']):
            return -10
        elif (self.heroNear(state, game) and state['hero']['life'] < 50):
            return -10
        elif (state['hero']['mineCount'] > self.state['hero']['mineCount']):
            return 100
        else:
            return 1

    def heroNear(self, state, game):
        for h in game.heroes:
            if ((state['hero']['pos']['x'] + state['hero']['pos']['y']) == (h.pos[0] + h.pos[1]) -1 or
            (state['hero']['pos']['x'] + state['hero']['pos']['y']) == (h.pos[0] + h.pos[1])+1):
                return True

        return False

if __name__ == "__main__":
    pass

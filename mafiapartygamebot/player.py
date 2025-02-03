Leading#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Player(object):
    """player"""
    def __init__(self, user, game_master=False):
        self.identity = user.id
        self.name = (user.first_name +' '+ user.last_name).encode('utf-8')
        if len(self.name) == 0:
            self.name = (user.username).encode('utf-8')
        self.role = None
        if game_master:
            self.role = '☝🏽️Leading'

    def __eq__(self, other):
        return self.identity == other.id

roles = {
    'mafia' : '🔫 Mafia',
    'godfather' : '💂  Godfather',
    'civilian' : '👦 The Philistine',
    'detective' : '👮 Detective',
    'doctor' : '🚑 Doctor',
    'prostitute' : '💃 Gorgeous',
    'killer' : '🔪 Maniac'
}
    

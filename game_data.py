# game_data.py

class Room:
    def __init__(self, name, description, items=None, players=None):
        self.name = name
        self.description = description
        self.items = items if items else []
        self.players = players if players else []

class Player:
    def __init__(self, name):
        self.name = name

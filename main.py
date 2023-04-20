# Project members: Allison Reilly and Stefani Go

from flask import Flask, render_template  

class Game:
   def __init__(self, name, format, date):
      self.name = name
      self.format = format
      self.date = date
      self.developers = []
      self.tags = []
      self.details = []
      self.languages = []
      self.achievement = ""
      self.genre = ""
      self.price = 0.0
      self.similarityScore =0.0

class Container:
   def __init__(self):
      self.gameList = []
      with open('games.csv') as file:
        lines = file.readlines()

      count = 0
      for line in lines[1:]: # start at index 1 to skip header
         if count > 10:
            break

         gameName, format, date, developer, tags, details, languages, achievements, genre, price = line.strip().split(',')

         print(f"Game: {gameName}")
         print(f"Format: {format}")
         print(f"Released On: {date}")
         print(f"Developer: {developer}")
         print(f"Tags: {tags}")
         print(f"Details: {details}")
         print(f"Languages: {languages}")
         print(f"Achievements: {achievements}")
         print(f"Genre: {genre}")
         print(f"Price: {price}")

         print()

         count += 1

if __name__ == "__main__":

   myGames = Container()

   app = Flask('app')
   @app.route('/')
   def display():
      return render_template('index.html')
   app.run(host='0.0.0.0', port=8080)

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
      self.genre = []
      self.price = ""
      self.similarityScore =0.0

   def setDevelopers(self, developers):
      self.developers = developers.split(' | ')

   def setTags(self, tags):
      self.tags = tags.split(' | ')

   def setDetails(self, details):
      self.details = details.split(' | ')

   def setLanguages(self, languages):
      self.languages = languages.split(' | ')

   def setAchievement(self, achievement):
      if achievement == "":
         achievement = "NA"
      else:
         self.achievement = achievement

   def setGenre(self, genre):
      self.genre = genre.split(' | ')

   def setPrice(self, price):
      containsNum = any(chr.isdigit() for chr in price)
      if containsNum:
         self.price = price
      else:
         self.price = "$0.00"

   def printInfo(self):
      print(f"Game: {self.name}")
      print(f"Format: {self.format}")
      print(f"Released On: {self.date}")
      print(f"Developer(s): {self.developers}")
      print(f"Tag(s): {self.tags}")
      print(f"Detail(s): {self.details}")
      print(f"Languages(s): {self.languages}")
      print(f"Achievement: {self.achievement}")
      print(f"Genre: {self.genre}")
      print(f"Price: {self.price}")


class Container:
   def __init__(self):
      self.gameList = []
      with open('games.csv') as file:
        lines = file.readlines()

      count = 0
      for line in lines[1:]: # start at index 1 to skip header
         if count > 10:
            break

         gameName, format, date, developer, tags, details, languages, achievements, genre, price = line.strip().split(',')[:10] # only get the first 10 items

         temp = Game(gameName, format, date)

         temp.setDevelopers(developer)
         temp.setTags(tags)
         temp.setDetails(details)
         temp.setLanguages(languages)
         temp.setAchievement(achievements)
         temp.setGenre(genre)
         temp.setPrice(price)
         self.gameList.append(temp);
         temp.printInfo()

         print()

         count += 1
      
      print(f"The container has {len(self.gameList)} games.")

if __name__ == "__main__":

   myGames = Container()

   app = Flask('app')
   @app.route('/')
   def display():
      return render_template('index.html')
   app.run(host='0.0.0.0', port=8080)

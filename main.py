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
      self.similarityScore = 0.0

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
   
   def setSimilarityScore(self, format, date, developers, tags, details, genre):
      score = 0.0
      if self.format == format:
         score += 1.0
      for item in developers:
         if item in self.developers:
            score += 1.0
      for item in tags:
         if item in self.tags:
            score += 1.0
      for item in details:
         if item in self.details:
            score += 1.0
      for item in genre:
         if item in self.genre:
            score += 1.0
      self.similarityScore = score

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
      self.standardSortResults = []
      self.mergeSortResults = []

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

      return self.gameList
      
   def merge(arr, left, mid, right): # code from module 6 lecture slides
      n1 = mid - left + 1
      n2 = right - mid
      X = [0] * n1
      Y = [0] * n2

      for i in range(n1):
         X[i] = arr[left + i]
      
      for j in range(n2):
         Y[j] = arr[1 + mid + j]
   
      i, j = 0
      k = left

      while i < n1 and j < n2:
         if X[i] <= Y[j]:
            arr[k] = X[i]
            i += 1
         else:
            arr[k] = Y[j]
            j += 1
         k += 1

      while i < n1:
         arr[k] = X[i]
         i += 1
         k += 1
      
      while j < n2:
         arr[k] = Y[j]
         j += 1
         k += 1
      
   def findGame(self, searchKey):
      for game in self.gameList:
         if game.name == searchKey:
            return game

   def mergeSortHelper(arr, left, right): # code from module 6 lecture slides
      if left < right:
         mid = left + (right - left) // 2
         mergeSortHelper(arr, left, mid)
         mergeSortHelper(arr, mid + 1, right)
         merge(arr, left, mid, right)

   def mergeSort(self):
      results = []
      self.mergeSortResults = results

   def standardSort(self):
      # use standard sort method to sort objects by similarity score and store the results in a list in descending order
      self.standardSortResults = sorted(self.gameList, key = lambda x: x.similarityScore, reverse = True)
      for i in range(9):
         print(self.standardSortResults[i].name)
         print()


if __name__ == "__main__":

   myGames = Container()

   searchKey = input("Enter the name of a game: ")
   
   # if game is in container, get its properties
   if any(x for x in myGames if x.name == searchKey):
      # based on its properties, update the similarity scores of every game in the container
      target = myGames.findGame(searchKey)
      for game in myGames:
         game.setSimilarityScore(target.format, target.date, target.developers, target.tags, target.details, target.genre)
      # sort the games based on their similarity scores 
      myGames.mergeSort()
      myGames.standardSort()
   else:
      print(f"Oops! We don't have info on that game yet. Would you like to try again?")

   app = Flask('app')
   @app.route('/')
   def display():
      return render_template('index.html')
   app.run(host='0.0.0.0', port=8080)

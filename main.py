# Project members: Allison Reilly and Stefani Go

from flask import Flask, render_template  


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

app = Flask('app')
@app.route('/')
def display():
  return render_template('index.html')
app.run(host='0.0.0.0', port=8080)

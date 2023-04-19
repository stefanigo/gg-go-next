// Project members: Allison Reilly and Stefani Go
#include <iostream>
#include <regex>
#include <fstream>
#include <sstream>
#include "Container.h"
using namespace std;

int main()
{
  cout << "hello" << endl;
  string line;
  ifstream inFile("games(1).csv");
  getline(inFile, line);
  int count = 0;

  while (getline(inFile, line)) {
    istringstream stream(line);
    string gameName, format, date, developer, tags, details, languages, achievements, genre, price;

    // if (count > 10){

    //   break;
    // }

    getline(stream, gameName, ',');
    cout << "Game: " << gameName << endl;
    getline(stream, format, ',');
    cout << "Format: " << format << endl;
    getline(stream, date, ',');
    cout << "Released On: " << date << endl;
    getline(stream, developer, ',');
    cout << "Developer: " << developer << endl;
    getline(stream, tags, ',');
    cout << "Tags: " << tags << endl;
    getline(stream, details, ',');
    cout << "Details: " << details << endl;
    getline(stream, languages, ',');
    cout << "Languages: " << languages << endl;
    getline(stream, achievements, ',');
    cout << "Achievements: " << achievements << endl;
    getline(stream, genre, ',');
    cout << "Genre: " << genre << endl;
    getline(stream, price);
    cout << "Price: " << price << endl;

    cout << endl;

    count++;
}
  return 0;
}

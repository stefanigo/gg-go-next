// Project members: Allison Reilly and Stefani Go
#include <iostream>
#include <regex>
#include <fstream>
#include <sstream>
#include "Container.h"
using namespace std;

int main()
{
    string line;
    ifstream inFile("games.csv");
    getline(inFile, line);

    string data;
    while(getline(inFile, data))
    {
        istringstream stream(data);

        // Game Name
        string gameName;
        getline(stream, data, ',');
        gameName = data;
        cout << "Game: " << gameName << endl;

        // Game Format
        string format;
        getline(stream, data, ',');
        format = data;
        cout << "Format: " << format << endl;

        // Game Release Date
        string date;
        getline(stream, data, ',');
        date = data;
        cout << "Released On: " << date << endl;

        // Game Developer
        string developer;
        getline(stream, data, ',');
        developer = data;
        cout << "Developer: " << developer << endl;

        // Game Tags
        string tags;
        getline(stream, data, ',');
        tags = data;
        cout << "Tags: " << tags << endl;

        // Game Details
        string details;
        getline(stream, data, ',');
        details = data;
        cout << "Details: " << details << endl;

        // Game Languages
        string languages;
        getline(stream, data, ',');
        languages = data;
        cout << "Languages: " << languages << endl;

        // Game Genre
        string genre;
        getline(stream, data, ',');
        genre = data;
        cout << "Genre: " << genre << endl;

        // Game Price
        string price;
        getline(stream, data, ',');
        format = data;
        cout << "Price: " << price << endl;
    }

    return 0;
}

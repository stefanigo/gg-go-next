#pragma once
#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;

/* This file will contain our Container class and Game struct */

class Container
{
private:
    struct Game
    {
        string name;
        string format;
        string date;
        vector<string> developers;
        vector<string> tags;
        vector<string> details;
        vector<string> languages;
        string achievement;
        string genre;
        double price;
        double similarityScore;
    };

    map<double, Game*> graph;


public:
    Container() {};
    void insertGame(string name, string format, string date);
    void setDevelopers();
    void setTags();
    void setDetails();
    void setLanguages();
    void setAchievement();
    void setGenre();
    void setPrice();
    void setSimilarityScore();
};

void Container::insertGame(string name, string format, string date)
{
    Game* temp = new Game;

}
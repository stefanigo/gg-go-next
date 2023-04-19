#pragma once
#include <iostream>
#include <string>
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
        string achievements;
        string genre;
        double price;
    };

public:
    Container() {};
};
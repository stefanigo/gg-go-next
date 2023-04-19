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
        string developer;
        string publisher;
        string genre;
        string maturityRating;
        double price;
    };

public:
    Container() {};
};
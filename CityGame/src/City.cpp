#include "City.h"
#include "Empire.h"
#include <string>
#include <iostream>
using namespace std;

City::City()
{
    cout << "Enter your city name: ";
    cin >> CITY_NAME;
    POP = 100;
    FARMS = 0;
    FOOD = 0;
}

City::~City()
{

}

int City::grow_POP(){

   if(FOOD >= POP){
        POP += .2;
        FOOD -= POP; return POP;}
    else{
        if(POP < 20){
//remove self with loo
            delete this;
        }
        FOOD -= POP;
        POP -= .2;
        return POP;
    }
}
int City::check_POP(){
    return POP;
}

void City::ViewStats(){

    cout << "Population: " << POP << endl;
    cout << "Food: " << FOOD << endl;
    cout << "Farms: " << FARMS << endl;

}

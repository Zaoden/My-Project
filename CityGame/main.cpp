#include <iostream>
#include "Empire.h"
#include "City.h"

using namespace std;

void startGame();
void clearscreen(int x){ for(int i=0;i<x;i++)cout << endl;}

int main()
{
    startGame();
    Empire Player1;
    Player1.CreateCity();

    cout << "-----------MENUE-----------" << endl
         << "---------------------------" << endl
         << "---------------------------" << endl
         << "View Empire---------------1" << endl
         << "View Cities---------------2" << endl
         << "View Armies---------------3" << endl
         << "End Turn------------------4" << endl;

         int pick;
         cin >> pick;

         switch(pick){

     case 1:

     case 2:

     case 3:

     case 4:
        Player1.EMPIRE_TURN();
        break;
     default:
        cout << "NOT A CHOICE MY LORD" << endl;


         }





    return 0;
}





void startGame(){


cout << "CITIES-----" << endl
     << "-----------" << endl
     << "Start-----1" << endl
     << "-----------" << endl
     << "Exit------2" << endl
     << "-----------" << endl;
     int a;
     cin >> a;
     switch (a){

    case 1:
        clearscreen(50);
        break;

    case 2:
        break;
     }


}

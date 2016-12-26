#include "Empire.h"
#include <iostream>

Empire::Empire()
{
        std::string a;
        std::cout << "Give your empire a name " << std::endl;
        std::cin >> a;
        EmpireName= a;
        gold = 100;


        for (int a =0; a<20; a++)
        cityList[a] = 0;

        CreateCity();
}

void Empire:: print(){

    std::cout << EmpireName << std::endl;
    for (int a =0; a<20; a++){
        std::cout << cityList[a] << std::endl;
    }
}

void Empire::EMPIRE_TURN(){

    for(int i=0; i<20;){
        if(cityList[i]==0)
            i++;
        else{
            cityList[i]->grow_POP();
            i++;
        }
    }

}

void Empire:: CreateCity(){

for(int i = 0; i<1;)
    if (cityList[i] == 0){
                cityList[i] = new City;
                std::cout << cityList[i]->CITY_NAME << std::endl;
                break;
                }
    else{
        i++;
    }


}

void Empire::ViewCities(){

for (int i = 0; i<1;){

    if (cityList[i]==0)
        i++;
    else{
        cityList[i]->ViewStats();
        if((cityList[i]->check_POP())== 0)
            cityList[i] = 0;
    }
}


}


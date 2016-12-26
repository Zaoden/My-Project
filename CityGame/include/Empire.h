#ifndef EMPIRE_H
#define EMPIRE_H
#include "City.h"
#include <string>


class Empire
{
    public:
        Empire();
        void CreateCity();
        void print();
        void EMPIRE_TURN();
        int gold;
        void ViewCities();

    protected:

    private:

        City *cityList[20];
        std::string EmpireName;


};

#endif // EMPIRE_H

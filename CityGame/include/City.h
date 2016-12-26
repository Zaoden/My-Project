#ifndef CITY_H
#define CITY_H
#include <string>


class City
{
    public:
        std::string CITY_NAME;
        City();
        ~City();
    int grow_POP();
    void NAME_CITY();
    int check_POP();
    void ViewStats();

    protected:

    private:
        int POP;
        int FARMS;
        int FOOD;
        int LOCATION(int x, int y);
};




#endif // CITY_H

#include "map_writer.h"
#include <iostream>
using namespace std;







map_writer::map_writer()
{

    int ystop;
    int xstop;

    int x=10;
    int y=10;
    for(ystop=0;ystop<=10;ystop++) {

        for(xstop=0;xstop<=10;xstop++) {

            Map[xstop][ystop][1]=0;
            }

    }


    Map[2][5][1] = 1;
    Map[7][5][1] = 1;


    int instance = 1;

    for(ystop=0;ystop<=y;ystop++) {


        for(xstop=0;xstop<=x;xstop++) {

            if (Map[xstop][ystop][instance] == 1 ){
                    cout<<"@";
            }
            else if (Map[xstop][ystop][instance] == 0){
                cout<<"o";

            }
            cout<<" ";


            }

    cout<<"\n";
    }
}

#include "spartanPi.h"
#include <time.h>

using namespace std;

SpartanPi_driver s;

int main(void){
    while(1){
        s.setLED(BLUE, 1);
        s.setLED(YELLOW, 0);
        printf("on\n");
        delay(100);
        
        s.setLED(BLUE, 0);
        s.setLED(YELLOW, 1);
        printf("off\n");
        delay(100);
    }
        
    printf("here we are\n");
    return 0;
}
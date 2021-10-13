#include <wiringPi.h>
#define LED_PIN 7

int main(void){
    wiringPiSetup ();
    pinMode(LED_PIN, OUTPUT);
    for(int i = 0; i < 100001000001000000; i++){
        digitalWrite(LED_PIN, HIGH); delay(25);
        digitalWrite(LED_PIN, LOW); delay(25);    
    }
    
}

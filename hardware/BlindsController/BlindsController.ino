#include <Stepper.h>
const int stepsPerRevolution = 2038;  // change this to fit the number of steps per revolution
int analogPin= 0;
Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11);


int raw= 0;
int openThreshold = 350;
int blindState = 0;
int mode = 1;
int avgLight = 0;
char readIn = '0';

void setup()
{
  Serial.begin(9600);
  myStepper.setSpeed(14);
  while (!Serial) {}
}

void loop()
{
  raw = analogRead(analogPin);
  Serial.print(blindState);
  if (Serial.available() > 0) {
    readIn = Serial.read();
    mode = readIn == '2'? 1 : 0;    
    if (mode == 1) {
        if (blindState == 0 && raw > openThreshold) {
          myStepper.step(3.5*stepsPerRevolution);
          blindState=1;
        }
        else if (blindState == 1 && raw < openThreshold) {
          myStepper.step(-3.5*stepsPerRevolution);
          blindState=0;
        } 
    } else {
      if (readIn == '1' && blindState == 0) {
          myStepper.step(3.5*stepsPerRevolution);
          blindState=1;
      } else if (readIn == '0' && blindState == 1) {
          myStepper.step(-3.5*stepsPerRevolution);
          blindState = 0;
      }
    }
    
  }
  delay(500);
}

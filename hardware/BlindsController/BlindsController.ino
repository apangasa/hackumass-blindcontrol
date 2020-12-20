#include <Stepper.h>
const int stepsPerRevolution = 2038;  // change this to fit the number of steps per revolution
int analogPin= 0;
Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11);


int raw= 0;
int openThreshold = 350;
int blindState = 0;

void setup()
{
  Serial.begin(9600);
  myStepper.setSpeed(14);
}

void loop()
{
  raw= analogRead(analogPin);
  Serial.println(raw);
  if (raw > openThreshold) {
    myStepper.step(5*stepsPerRevolution);
    blindState=1;
  }
  else if (raw <openThreshold) {
    myStepper.step(-5*stepsPerRevolution);
    blindState=0;
  } 
  delay(10);
}

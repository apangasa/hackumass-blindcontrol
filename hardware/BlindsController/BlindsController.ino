#include <Stepper.h>
const int stepsPerRevolution = 2038;  // change this to fit the number of steps per revolution
int analogPin= 0;   //pin to measure voltage drop over 1k resistor
Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11); //revolve stepper according to instructions with myStepper


int raw= 0; // voltage (proportion of 5V) measured from
int openThreshold = 350; // voltage needed (proportion of 5V) to open blinds
int blindState = 0; //start off with blinds closed
int mode = 1; //default to automatic mode
char readIn = '0'; // read input

void setup()
{
  Serial.begin(9600); //begin at 9600 rate of communication
  myStepper.setSpeed(14); //stepper speed set to 14
  while (!Serial) {} // wait until serial communication established
}

void loop()
{
  raw = analogRead(analogPin); //get voltage
  Serial.print(blindState); //send state of blind
  if (Serial.available() > 0) { //if data sent to arduino, read
    readIn = Serial.read();
    mode = readIn == '2'? 1 : 0; // if readIn is '2' stay in automatic, else switch to manual
    if (mode == 1) { //automatic mode
        if (blindState == 0 && raw > openThreshold) { //if blinds are closed & voltage exceeds threshold, open blinds
          myStepper.step(3.5*stepsPerRevolution);
          blindState=1;
        }
        else if (blindState == 1 && raw < openThreshold) { //if blinds are open & voltage bellow threshold, close blinds
          myStepper.step(-3.5*stepsPerRevolution);
          blindState=0;
        }
    } else { //manual mode
      if (readIn == '1' && blindState == 0) { //if input is open blinds and blinds are closed, open blinds
          myStepper.step(3.5*stepsPerRevolution);
          blindState=1;
      } else if (readIn == '0' && blindState == 1) { //if input is closed blinds and blinds are open, close blinds
          myStepper.step(-3.5*stepsPerRevolution);
          blindState = 0;
      }
    }

  }
  delay(500);
}

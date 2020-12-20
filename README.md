# Flippy
Need more natural lighting? Forgot to close your blinds before leaving home and worried about wandering eyes peeking at your valuables? Save energy for heating naturally using Flippy. Fourty eight percent of sunlight is absorbed by the earth's surface and converted to heat. Instead of using this natural source of heating, many people keep their blinds closed.

## How does it work?
Flippy consists of extensive hardware and software that allows it to control your blinds both automatically and manually. At a high level, Flippy lets the user conveniently control their blinds remotely using a smartphone. Flippy has two modes: manual and magic. In the manual mode, a user can simply open or close their blinds at their will from their smartphone. In magic mode, Flippy will automatically open the blinds when there is sufficient sunlight outside, and will close them as it gets dark.

### Hardware
On the hardware end, Flippy makes use of an Arduino Uno to operate a stepper motor according to resistances measured from a photoresistor. We empirically determined a threshold resistance that indicates daylight, so the motor opens and closes the blinds based on the measured photoresistor value compared to this threshold. The motor is mounted via a custom-engineered 3D printed bracket and interfaced with the blind rotational point via 3D printed gears.

### Software
Flippy's software consists of the following:
- Android mobile App frontend written in JavaScript to control the mode and operate the blind state in manual mode
- Arduino C code running on the Uno to programatically control the motor and moderate the light-detecting circuit
- Python Flask application running on Google Cloud Platform's App Engine to enable communications between the Android app and the Uno
- Python Flask application running locally to allow the Arduino to communicate with the cloud server
- Python code running locally to interface between the Uno and the cloud server application

![Flippy Mobile](https://github.com/apangasa/hackumass-blindcontrol/Flippy.jpg)

## Use Case
Flippy has a multitude of use cases:

Flippy maximizes your wellbeing at home by ensuring that there is adequate natural indoor lighting. Natural light increases vitamin D, a critical nutrient that prevents bone loss, heart disease, weight gain, and various cancers. Increasing indoor lighting can also ward off depression and improve sleep.

Flippy's mobile app gives users the ability to close and open their blinds from their phone when they are away from home.

Flippy also promotes home security by giving you remote access control to close and open your blinds when you are away from home. Closing the blinds and curtains are common home security measures to reduce the chances of a home invasion. 

Fun Fact: Sunlight produces 0.0079W/m^2 per lux (photon flux). One open window equates to half a heater! Imagine the savings!

 
## What's next for Flippy
The first development that we want to make is using a Wi-Fi module to connect the Arduino to the internet instead of connecting it to a computer with a local server via USB. Although our method worked for communicating between the cloud and the Arduino, the process flow would be a lot cleaner and more scalable with a Wi-Fi module, so if we had access to one, we would definitely use that instead. Additionally, we want to provide the user with more customizability and flexibility on the application end. For example, we would perhaps want to allow the user to set their custom threshold of daylight they want to let in, rather than using our empirically determined threshold value. Moreover, we could even increase the precision of the motor turning to allow in specific amounts of light. Another cool integration would be IOT expansion via Google Assistant or Amazon Alexa. Finally, we want to finish the full functionality of allowing the user to set a schedule of times to open and close by invoking our already written Google Cloud Function for doing so.



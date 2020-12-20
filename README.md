# Blind Control
Need more natural lighting? Forgot to close your blinds before leaving home and worried about wandering eyes peeking at your valuables? Save energy for heating naturally using Blind Control. Fourty eight percent of sunlight is absorbed by the surface and converted to heat. Instead of using this natural source of heating, many people keep their blinds closed.

## How does it work?
Blind Control consists of extensive hardware and software that allows it to control your blinds both automatically and manually. At a high level, Blind Control lets the user conveniently control their blinds remotely using a smartphone. Blind Control has two modes: manual and magic. In the manual mode, a user can simply open or close their blinds at their will from their smartphone. In magic mode, Blind Control will automatically open the blinds when there is sufficient sunlight outside, and will close them as it gets dark.

### Hardware
On the hardware side, Blind Control makes use of an Arduino Uno as the brains of the operation by controlling the motor used to open/close the blinds and by moderating the light-detecting circuit. 

<Talk about the hardware including CAD models, circuit diagrams, and interactions>

### Software
Blind Control's software consists of the following:
- An Android App frontend written in JavaScript to change the mode of 
- C code running on the Uno to programatically control the motor and moderate the light-detecting circuit
- Python Flask application running on Google Cloud's App Engine to enable communications between the Android app and the Uno
- Python code running locally to interface between the Uno and the cloud server application.




## Use Case
Blind Control has a multitude of use cases:

Blind Control maximizes your wellbeing at home by ensuring that there is adequate natural indoor lighting. Natural light increases vitamin D, a critical nutrient that prevents bone loss, heart disease, weight gain, and various cancers. Increasing indoor lighting can also ward off depression and improve sleep.

Blind Control's mobile app gives users the ability to close and open their blinds from their phone when they are away from home.

Using Google Cloud Functions, the mobile app can update the desired state of the blinds (open or closed) in the cloud. Separate scripts can be run locally to get the desired state and communicate with the Arduino directly. 

Blind Control also promotes home security by giving you remote access control to close and open your blinds when you are away from home. Closing the blinds and curtains are common home security measures to reduce the chances of a home invasion. 

Fun Fact: Sunlight produces 0.0079W/m^2 per lux (photon flux). One open window equates to half a heater! Imagine the savings!
 
## What's next for Blind Control
<make this look nicer>
IOT integraiton using Google Assistant or Amazon Alexa
More seamless hardware integration
other stuff

## How to replicate Blind Control
<Not sure how this works so make this better>
1. Download the app
2. Clone the thing
3. Create 3D printout with CAD model
4. Make the circuits and stuff. Program Uno
5. Deploy to cloud
6. Run local Python app.
7. Run it

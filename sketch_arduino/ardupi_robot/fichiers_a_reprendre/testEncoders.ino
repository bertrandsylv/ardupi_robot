#define WHEEL_DIAMETER 0.065
#define ANGULAR_RES 0.314159265
#define PI 3.14159265358979

// Declaration des encodeurs
#include "encoder.h"
Encoder leftEncoder(leftEncoderPin, leftEncoderInterruptNb, WHEEL_DIAMETER, ANGULAR_RES); 
Encoder rightEncoder(rightEncoderPin, rightEncoderInterruptNb, WHEEL_DIAMETER, ANGULAR_RES); 
// Declaration des interrupt handlers associes aux encodeurs
#include "encoder_interrupts.h"

#include "timer.h"
Timer timerEncoders(0.05);


// ******************** SETUP ******************************
void setup() {
  // attachement des interruptions liees aux encodeurs
  attachInterrupt(leftEncoder.getInterruptNb(),  doLeftEncoder, CHANGE);
  attachInterrupt(rightEncoder.getInterruptNb(),  doRightEncoder, CHANGE);
  
  // sens rotation vers l'avant
  leftEncoder.setRotationDir(1);
  rightEncoder.setRotationDir(1);
  
  // intialisation de la liaison serie
  Serial.begin (9600);
  
  //Serial.println("t\tLInc\tLThetaDeg\tRInc\tRThetaDeg");
  Serial.println("t\tLInc\tRInc");
  
  delay(1500);
} // ******************** END SETUP ******************************





// ******************** LOOP **********************************
void loop(){ 
  
  if (timerEncoders.checkTimeOut()){	
    Serial.print(millis()/1000.0);  
    Serial.print("\t");
    Serial.print(leftEncoder.getIncrementNb());
    //Serial.print("\t");
    //Serial.print(leftEncoder.getWheelAngle());
    Serial.print("\t");
    Serial.println(rightEncoder.getIncrementNb());
    //Serial.print("\t");
    //Serial.println(rightEncoder.getWheelAngle());
  }
  
    
} //  ******************** END LOOP **********************************


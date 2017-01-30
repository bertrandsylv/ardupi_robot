//#include "WProgram.h"
#include "Arduino.h"
#include "encoder.h"

// constructeur
Encoder::Encoder(int pin, int interruptNb, double wheelDiameter, double angularRes){
	_pin = pin;
	pinMode(_pin, INPUT);
	
	_interruptNb = interruptNb;
	
	_rotationDir = 0;
	
	_incrementNb = 0;
	//_wheelAngle = 0.0;
	_timeOfLastChange = 0.0;
	
	_wheelDiameter = wheelDiameter;
	_angularRes = angularRes;
	
	//attachInterrupt(_interruptNb, this->doEncoder, CHANGE);
}

// accesseurs
unsigned int Encoder::getPin(){
	return _pin;
}

unsigned int Encoder::getInterruptNb(){
	return _interruptNb;
}

unsigned int Encoder::getRotationDir(){
	return _rotationDir;
}

long Encoder::getIncrementNb(){
	return _incrementNb;
}

/*
double Encoder::getWheelAngle(){
	return _wheelAngle;
}
*/

double Encoder::getTimeOfLastChange(){
	return _timeOfLastChange;
}

double Encoder::getWheelDiameter(){
	return _wheelDiameter;
}

double Encoder::getAngularRes(){
	return _angularRes;
}



void Encoder::setPin(int pin){
	_pin = pin;
}

void Encoder::setInterruptNb(int interruptNb){
	_interruptNb = interruptNb;
}

void Encoder::setRotationDir(int rotationDir){
	_rotationDir = rotationDir;
}

void Encoder::setIncrementNb(long incrementNb){
	_incrementNb = incrementNb;
}

/*
void Encoder::setWheelAngle(double wheelAngle){
	_wheelAngle = wheelAngle;
}
*/

void Encoder::setTimeOfLastChange(double timeOfLastChange){
	_timeOfLastChange = timeOfLastChange;
}

void Encoder::setWheelDiameter(double wheelDiameter){
	_wheelDiameter = wheelDiameter;
}

void Encoder::setAngularRes(double angularRes){
	_angularRes = angularRes;
}


// autres méthodes

void Encoder::resetEncoder(){
	_incrementNb = 0;
	//_wheelAngle = 0.0;
	_timeOfLastChange = 0.0;
}



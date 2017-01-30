/*
-----------------------------------------
					   Encoders
				Sylvain BERTRAND, 2015
-----------------------------------------
*/


#ifndef ENCODER_H
#define ENCODER_H

// Vcc encoders: +5V


// **** connection of two encoder on Arduino MEGA ****
#define leftEncoderPin 18  // left encoder on Digital Pin 18
#define rightEncoderPin 19 // left encoder on Digital Pin 19
// corresponding interrupt numbers
#define leftEncoderInterruptNb 5
#define rightEncoderInterruptNb 4
  
  
  
class Encoder
{	

  
  private:
	// attributs
	unsigned int _pin;
	unsigned int _interruptNb;
	
	unsigned int _rotationDir;  // = +1 or -1 according to rotation direction, 0 if stopped
	
	volatile long _incrementNb; // current number of icnrements
	//volatile double _wheelAngle; // angle de la roue à l'instant k (rad)
	volatile double _timeOfLastChange; // instant de la dernière mise à jour (sec)
	
	// constantes liées à la roue
	double _wheelDiameter; // diamètre de la roue (m)
	double _angularRes; // résolution angulaire de l'encodeur (rad)


	// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	// A vérifier : même largeur entre dents et creux sur l'encodeur ? 
	// Si oui : ok
	// Si non : distinguer les passages sur les parties opaques des parties creuses de l'encodeur 
	//		1 ere solution : utiliser une interruption uniquement sur front montant 'RISING' ou descendant 'FALLING' et prendre une résolution angulaire correspondant à largeur dent + creux
	//		2 e solution : utiliser deux interruptions différentes (possible ?) (front montant 'RISING', front descendant 'FALLING') et deux résolution angulaires correspondantes
	// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

	

  public:
	// constructeur
	Encoder(int pin, int interruptNb, double wheelDiameter, double angularRes);
	
	// accesseurs
	unsigned int getPin();
	unsigned int getInterruptNb();
	unsigned int getRotationDir();
	long getIncrementNb();
	//double getWheelAngle();
	double getTimeOfLastChange();
	double getWheelDiameter();
	double getAngularRes();
	
	
	void setPin(int pin);
	void setInterruptNb(int interruptNb);
	void setRotationDir(int rotationDir);		
	void setIncrementNb(long incrementNb);
	//void setWheelAngle(double wheelTheta);
	void setTimeOfLastChange(double t);
	void setWheelDiameter(double wheelDiameter);
	void setAngularRes(double angularRes);


	// autres méthodes
	void resetEncoder(); // remise à zéro de toutes les données associées à l'encodeur
	

};
 

 
#endif

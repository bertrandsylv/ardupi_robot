#ifndef ENCODER_INTERRUPT_H
#define ENCODER_INTERRUPT_H

void doLeftEncoder()
{
	
	double t = millis()/1000.0;
	if (t>leftEncoder.getTimeOfLastChange())
	{
		leftEncoder.setIncrementNb( leftEncoder.getIncrementNb()+1*leftEncoder.getRotationDir() );

		// incrémentation de theta
		//leftEncoder.setWheelAngle( leftEncoder.getWheelAngle() + leftEncoder.getAngularRes()*leftEncoder.getRotationDir() );
	
		// maj  timeOfLastChange pour le prochain appel
		leftEncoder.setTimeOfLastChange( t );
	
		//Serial.println (leftEncoder.getIncrementNb(), DEC);          
		// use for debugging - remember to comment out

	}
	
}

void doRightEncoder()
{
	double t = millis()/1000.0;
	if (t>rightEncoder.getTimeOfLastChange() )
	{
		rightEncoder.setIncrementNb( rightEncoder.getIncrementNb()+1*rightEncoder.getRotationDir() );       
     
		// incrémentation de theta
		//rightEncoder.setWheelAngle( rightEncoder.getWheelAngle() + rightEncoder.getAngularRes()*rightEncoder.getRotationDir() );
	
		// maj  timeOfLastChange pour le prochain appel
		rightEncoder.setTimeOfLastChange( t );
	 
		//Serial.println (rightEncoder.getIncrementNb(), DEC);          
		// use for debugging - remember to comment out
	}
	 
}

#endif


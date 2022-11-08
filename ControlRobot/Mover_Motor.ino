
#include<Servo.h>
Servo motor;
void setup() {
  // put your setup code here, to run once:
  motor.attach(9,1000,2000)
  pinMode(A0,INPUT);
 

}

void loop() {
  // put your main code here, to run repeatedly:
  int potVal=analogRead(A0);
  potVal=map(potVal,0,1023,0,180);
  Motor.write(potVal):

}

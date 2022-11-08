
#define ENCA 6 //Yellow
#define ENCB 7//White

int pos=0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ENCA,INPUT);
  pinMode(ENCB,INPUT);
  attachInterrupt(digitalPinToInterrupt(ENCA),readEncoder,RISING);
 
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(pos);
}

void readEncoder(){
  int Contador=digitalRead(ENCB);
  if(Contador>0){
    pos++;
  }
  else{
    pos--;
  }
  
}

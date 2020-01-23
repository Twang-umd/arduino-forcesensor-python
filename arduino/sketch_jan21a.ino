int LEDPin = 10; //
int waitTime01 = 1000;
int waitTime02 = 1000;
//String w1 = "asdasdasdas";
//int inputnum;

void setup() {
  // put your setup code here, to run once:
  pinMode(13,OUTPUT);
  pinMode(LEDPin, OUTPUT); //declare pin 10 as output
  //Serial.begin(9600);//9600 speed higher=faster

}

void loop() {
  // put your main code here, to run repeatedly:
  
  //Serial.println("How Many Times Do You Want the Red LED to blink?"); //Prompt User for Input
  //while(Serial.available()==0) { // Wait for User to Input Data  
  //}
  //inputnum = Serial.parseInt();  //Read the data the user has input
  //Serial.println(inputnum);
  digitalWrite(13,LOW);
  digitalWrite(LEDPin, HIGH); //turn led on
  delay(waitTime01); //delay 1000ms
  digitalWrite(LEDPin, LOW); //turn led off
  delay(waitTime02);
  
  //for
  //for (int i = 1; i <= 10; i = i + 1) {
    //code
    //Serial.println(i);
    //Serial.print("print string like this");
    //Serial.println("print string like this");
    //} 
  //end for

}

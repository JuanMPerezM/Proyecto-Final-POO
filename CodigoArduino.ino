int mql135=0;
int muy_buena=8;
int regular=9;
int mala=10;
int muy_malo=11;
int extremadamente_malo=12;
void setup() {
  Serial.begin(9600);
  pinMode(muy_buena,OUTPUT);
  pinMode(regular,OUTPUT);
  pinMode(mala,OUTPUT);
  pinMode(muy_malo,OUTPUT);
  pinMode(extremadamente_malo,OUTPUT);

  digitalWrite(muy_buena,LOW);
  digitalWrite(regular,LOW);
  digitalWrite(mala,LOW);
  digitalWrite(muy_malo,LOW);
  digitalWrite(extremadamente_malo,LOW);

  

}

void loop() {
  
  


  mql135=analogRead(0);
  Serial.println(mql135,DEC);
  Serial.println("ppm");
  delay(250);
  if(mql135<=90){
  
    Serial.println("muy buena");
    digitalWrite(muy_buena,HIGH);
    digitalWrite(regular,LOW);
    digitalWrite(mala,LOW);
    digitalWrite(muy_malo,LOW);
    digitalWrite(extremadamente_malo,LOW);
    delay(500);
  }
  if(mql135>=91 and mql135<=110){    
    Serial.println("regular");
    digitalWrite(muy_buena,LOW);
    digitalWrite(regular,HIGH);
    digitalWrite(mala,LOW);
    digitalWrite(muy_malo,LOW);
    digitalWrite(extremadamente_malo,LOW);
    delay(500); 
  
  
  }
  if(mql135>=111 and mql135<=165){   
    Serial.println("mala");
    digitalWrite(muy_buena,LOW);
    digitalWrite(regular,LOW);
    digitalWrite(mala,HIGH);
    digitalWrite(muy_malo,LOW);
    digitalWrite(extremadamente_malo,LOW);
    delay(500);
  }
    if(mql135>=166 and mql135<=220){
      Serial.println("muy mala");
      digitalWrite(muy_buena,LOW);
      digitalWrite(regular,LOW);
      digitalWrite(mala,LOW);
      digitalWrite(muy_malo,HIGH);
      digitalWrite(extremadamente_malo,LOW);
      delay(500);    
    }
    if(mql135>=221 and mql135<=550){
      Serial.println("extremadamente mala");
      digitalWrite(muy_buena,LOW);
      digitalWrite(regular,LOW);
      digitalWrite(mala,LOW);
      digitalWrite(muy_malo,LOW);
      digitalWrite(extremadamente_malo,HIGH);
      delay(500);
    }
         
    
  
    
}

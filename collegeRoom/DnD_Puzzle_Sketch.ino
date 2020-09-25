int hallSensorPin1 = 2;
int hallSensorPin2 = 3;
int hallSensorPin3 = 4;
int hallSensorPin4 = 5;


int magLock = 13;
bool state1, state2, state3, state4, openState = false;

void setup() {
  Serial.begin(9600);
  pinMode(magLock, OUTPUT);
  pinMode(hallSensorPin1, INPUT_PULLUP);
  pinMode(hallSensorPin2, INPUT_PULLUP);
  pinMode(hallSensorPin3, INPUT_PULLUP);
  pinMode(hallSensorPin4, INPUT_PULLUP);
}

void loop() {
  state1 = digitalRead(hallSensorPin1);
  state2 = digitalRead(hallSensorPin2);
  state3 = digitalRead(hallSensorPin3);
  state4 = digitalRead(hallSensorPin4);


  if (state1 == LOW && state2 == LOW && state3 == LOW && state4 == LOW)
    openState = true;

  if (openState == true)
    digitalWrite(magLock, LOW);
  else digitalWrite(magLock, HIGH);

  if (state1 == LOW && state2 == HIGH && state3 == HIGH && state4 == HIGH)
    openState = false;
}

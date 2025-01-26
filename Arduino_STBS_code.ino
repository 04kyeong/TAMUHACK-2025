/*
  Ultrasonic Sensor HC-SR04 and LED Control
  Turns on an LED when an object is close enough.
  Alerts only once when the threshold distance is met.
*/

// Define pins for the ultrasonic sensor
const int trigPin = 9;
const int echoPin = 10;
const int ledPin = 3; // Define pin for the LED
const int buttonPin = 2; //button pin

// Define variables
long duration;
int distance;
// Set the threshold distance in centimeters
const int thresholdDistance = 15; //15cm from the sensor
unsigned long emptyTime = 0; // when we replace the trashbag (millis())
unsigned long fullTime = 0;  // when the trashcan is full (millis())
bool trashFull = false; // status of trashcan
bool buttonPressed = false; //status of button

// Variable to track whether the alert has been triggered
//bool alertTriggered = false;

void setup() {
  // Set the pin modes
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT);  // Sets the echoPin as an Input
  pinMode(ledPin, OUTPUT);  // Sets the ledPin as an Output
  pinMode(buttonPin, INPUT_PULLUP); // sets the buttonpin as pullup
  // Start serial communication
  Serial.begin(9600);
}

void loop() {
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  // Sets the trigPin on HIGH state for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  
  // Calculate the distance in cm
  distance = duration * 0.034 / 2;

  //debugging
  //Serial.print("Distance:");
  //Serial.println(distance);
  
  // Print the distance to the Serial Monitor
  if (distance > 0 && distance <= thresholdDistance) {
    if (!trashFull) {
      trashFull = true;
      digitalWrite(ledPin, HIGH); // Turn on the LED
      fullTime = millis(); //time spent to get the trashcan full again
      unsigned long timeToFill = fullTime - emptyTime;
      Serial.print("This can is full. Please replace the trash bag.");
      Serial.print("Trashcan has ");
      Serial.print(distance);
      Serial.println(" cm left.");
      Serial.print("It took ");
      Serial.print(timeToFill / 1000); // 초 단위로 출력
      Serial.println("seconds to get this trashcan full again.");
    }
  } //else {
    //if (trashFull) {
      //trashFull = false; //when the trashcan is not full.
    //}
    //digitalWrite(ledPin, LOW); // Turn off the LED
    // Reset the alert when the trash level goes below the threshold
  //}

  if (digitalRead(buttonPin) == LOW && !buttonPressed) {
    buttonPressed = true;
    emptyTime = millis(); // When we replaced the trashbag
    Serial.println("Trashbag has been replaced.");
    trashFull = false;
    digitalWrite(ledPin, LOW); //turn off LED
    delay(500); // 버튼 디바운싱을 위한 딜레이
  }

  if (digitalRead(buttonPin) == HIGH && buttonPressed) {
    buttonPressed = false;         // 버튼 상태 초기화
  }

  delay(100); // Small delay for stable readings
}

// Pin definitions
const int trigPin = 9;
const int echoPin = 10;
const int ledPin = 3;
 
// Threshold distance in centimeters
const int thresholdDistance = 15;
 
void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  
  // Set pin modes
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(ledPin, OUTPUT);
}
 
void loop() {
  // Send a 10-microsecond pulse to the Trig pin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  // Measure the time it takes for the Echo pin to go HIGH
  long duration = pulseIn(echoPin, HIGH);
 
  // Calculate distance in centimeters
  int distance = duration * 0.034 / 2;
 
  // Print distance to Serial Monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
 
  // Check if object is within the threshold distance
  if (distance > 0 && distance <= thresholdDistance) {
    digitalWrite(ledPin, HIGH); // Turn LED on
  } else {
    digitalWrite(ledPin, LOW); // Turn LED off
  }
 
  delay(100); // Short delay for stability
}

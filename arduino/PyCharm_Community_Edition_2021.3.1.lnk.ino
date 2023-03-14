void setup() {
  Serial.begin(9600); // Initialize the Serial port with baud rate 9600
}

void loop() {
  int output = random(-100, 100); // Generate a random number between 0 and 100
  Serial.println(output); // Send the output number to the Serial port
  delay(100); // Wait for 1 second before sending the next number
}

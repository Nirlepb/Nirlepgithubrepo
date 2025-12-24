/*
  Case Study 4: Sun Tracker Prototype (ESP32 Version)
  Objective: Demonstrate sensor input (LDR), user control (Pot + Switch), 
  and automated response (LEDs).
  
  Connections (ESP32 Default):
  - Potentiometer: GPIO 34 (Analog Input only)
  - LDR: GPIO 35 (Analog Input only)
  - Switch: GPIO 15 (Input with internal Pullup)
  - Red LED: GPIO 18 (Too Dark)
  - Green LED: GPIO 19 (Locked/Optimal)
  - Yellow LED: GPIO 21 (Too Bright)
*/

// --- Pin Definitions ---
const int PIN_POT = 34;    // Analog ADC1_CH6
const int PIN_LDR = 35;    // Analog ADC1_CH7
const int PIN_SWITCH = 15;
const int PIN_LED_RED = 18;
const int PIN_LED_GREEN = 19;
const int PIN_LED_YELLOW = 21;

// --- Variables ---
bool systemState = false;      // false = OFF, true = ON
bool lastButtonState = HIGH;   // For edge detection
int potValue = 0;              // Stores Target value
int ldrValue = 0;              // Stores Sensor value
int tolerance = 300;           // Wider tolerance due to higher resolution (0-4095)

void setup() {
  Serial.begin(115200); // Higher baud rate for ESP32

  // Initialize Pins
  // Note: GPIO 34/35 are input-only pins on ESP32
  pinMode(PIN_POT, INPUT);
  pinMode(PIN_LDR, INPUT);
  
  // ESP32 Internal Pullups are usually available on GPIO 15
  pinMode(PIN_SWITCH, INPUT_PULLUP);

  pinMode(PIN_LED_RED, OUTPUT);
  pinMode(PIN_LED_GREEN, OUTPUT);
  pinMode(PIN_LED_YELLOW, OUTPUT);

  Serial.println("ESP32 Sun Tracker Prototype Initialized.");
  Serial.println("Press Switch (GPIO 15) to toggle System ON/OFF.");
}

void loop() {
  // --- 1. Handle On/Off Switch ---
  int buttonReading = digitalRead(PIN_SWITCH);

  // Toggle state on button press (detect falling edge)
  if (lastButtonState == HIGH && buttonReading == LOW) {
    systemState = !systemState;
    delay(50); // Simple debounce
    Serial.print("System State: ");
    Serial.println(systemState ? "ON" : "OFF");
  }
  lastButtonState = buttonReading;

  // --- 2. Main Logic ---
  if (systemState) {
    // Read Sensors (ESP32 ADC is 12-bit, range 0-4095)
    potValue = analogRead(PIN_POT);
    ldrValue = analogRead(PIN_LDR);

    // Debugging output
    Serial.print("Target (Pot): ");
    Serial.print(potValue);
    Serial.print(" | Actual (LDR): ");
    Serial.println(ldrValue);

    // Compare LDR to Potentiometer (Target)
    
    if (abs(ldrValue - potValue) <= tolerance) {
      // Light is within acceptable range of target ("Locked")
      digitalWrite(PIN_LED_GREEN, HIGH);
      digitalWrite(PIN_LED_RED, LOW);
      digitalWrite(PIN_LED_YELLOW, LOW);
    } 
    else if (ldrValue < potValue) {
      // Too Dark compared to target
      digitalWrite(PIN_LED_GREEN, LOW);
      digitalWrite(PIN_LED_RED, HIGH);
      digitalWrite(PIN_LED_YELLOW, LOW);
    } 
    else {
      // Too Bright compared to target
      digitalWrite(PIN_LED_GREEN, LOW);
      digitalWrite(PIN_LED_RED, LOW);
      digitalWrite(PIN_LED_YELLOW, HIGH);
    }

  } else {
    // System is OFF: Turn off all LEDs
    digitalWrite(PIN_LED_GREEN, LOW);
    digitalWrite(PIN_LED_RED, LOW);
    digitalWrite(PIN_LED_YELLOW, LOW);
  }

  delay(100); // Small delay for loop stability
}
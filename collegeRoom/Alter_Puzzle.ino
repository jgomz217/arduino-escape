
/* -----------------------------------------------------------------------------------------
              MFRC522      Arduino       Arduino   Arduino    Arduino          Arduino
              Reader/PCD   Uno/101       Mega      Nano v3    Leonardo/Micro   Pro Micro
  Signal      Pin          Pin           Pin       Pin        Pin              Pin
  -----------------------------------------------------------------------------------------
  RST/Reset   RST          9             5         D9         RESET/ICSP-5     RST
  SPI SS      SDA(SS)      10            53        D10        10               10
  SPI MOSI    MOSI         11 / ICSP-4   51        D11        ICSP-4           16
  SPI MISO    MISO         12 / ICSP-1   50        D12        ICSP-1           14
  SPI SCK     SCK          13 / ICSP-3   52        D13        ICSP-3           15
*/

#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9          // Configurable, see typical pin layout above
#define SS_PIN1         3          // Configurable, see typical pin layout above
#define SS_PIN2         4
#define SS_PIN3         5
#define BLUE_PIN        6
#define RED_PIN         7
#define GREEN_PIN       8
#define MAGLOCK         2

MFRC522 mfrc522_1(SS_PIN1, RST_PIN);  // Create MFRC522 instance
MFRC522 mfrc522_2(SS_PIN2, RST_PIN);
MFRC522 mfrc522_3(SS_PIN3, RST_PIN);

void pulseLED();
void flashLED();
bool compareRFID1();
bool compareRFID2();
bool compareRFID3();

int fadespeed = 5;
int flashspeed = 20;
int brightness = 5;


void setup() {
  pinMode(BLUE_PIN, OUTPUT);
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(MAGLOCK, OUTPUT);
  digitalWrite(MAGLOCK, HIGH);
  Serial.begin(9600);		// Initialize serial communications with the PC
  while (!Serial);		// Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
  SPI.begin();			// Init SPI bus
  mfrc522_1.PCD_Init();		// Init MFRC522_1
  mfrc522_2.PCD_Init();   // Init MFRC522_2
  mfrc522_3.PCD_Init();   // Init MFRC522_3
}

void loop() {
  // Reset the loop if no new card present on the sensor/reader. This saves the entire process when idle
  while (compareRFID1() == false || compareRFID2() == false/* && compareRFID3 == true*/) {
    pulseLED();
    digitalWrite(MAGLOCK, HIGH);
  }
  flashLED();
  digitalWrite(MAGLOCK, LOW);
}

void flashLED() {
  for (int i = 0; i < 10; i++) {
    digitalWrite(RED_PIN, HIGH);
    delay(flashspeed);
    digitalWrite(RED_PIN, LOW);
  }
}

void pulseLED() {
  analogWrite(RED_PIN, brightness);
  brightness = brightness + fadespeed;
  if (brightness <= 1| brightness >= 255) {
    fadespeed = -fadespeed;
  }
}

bool compareRFID1() {
  if (!mfrc522_1.PICC_IsNewCardPresent())
    return false;
  else {
    mfrc522_1.PICC_ReadCardSerial();
    String ID = "";
    byte letter;

    for (byte i = 0; i < mfrc522_1.uid.size; i++) {
      ID.concat(String(mfrc522_1.uid.uidByte[i] < 0x10 ? "0" : " "));
      ID.concat(String(mfrc522_1.uid.uidByte[i], HEX));
    }
    ID.toUpperCase();
    if (ID.substring(1) == "43 A2 5A F5") {
      Serial.println("RFID1 correct");
      return true;
    }
    else return false;
  }
}

bool compareRFID2() {
  if (!mfrc522_2.PICC_IsNewCardPresent())
    return false;
  else  {
    mfrc522_2.PICC_ReadCardSerial();
    String ID = "";
    byte letter;

    for (byte i = 0; i < mfrc522_2.uid.size; i++) {
      ID.concat(String(mfrc522_2.uid.uidByte[i] < 0x10 ? "0" : " "));
      ID.concat(String(mfrc522_2.uid.uidByte[i], HEX));
    }
    ID.toUpperCase();
    if (ID.substring(1) == "D9 99 98 C4") {
      Serial.println("RFID2 correct");
      return true;
    }
    else return false;
  }
}

bool compareRFID3() {
  if (!mfrc522_3.PICC_IsNewCardPresent())
    return false;
  else  {
    mfrc522_3.PICC_ReadCardSerial();
    String ID = "";
    byte letter;

    for (byte i = 0; i < mfrc522_3.uid.size; i++) {
      ID.concat(String(mfrc522_3.uid.uidByte[i] < 0x10 ? "0" : " "));
      ID.concat(String(mfrc522_3.uid.uidByte[i], HEX));
    }
    ID.toUpperCase();
    if (ID.substring(1) == "80 2F CB 4A") {
      Serial.println("RFID2 correct");
      return true;
    }
    else return false;
  }
}

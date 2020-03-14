//Modification of tft example

#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_TFTLCD.h> // Hardware-specific library
#include <TouchScreen.h>

#if defined(__SAM3X8E__)
    #undef __FlashStringHelper::F(string_literal)
    #define F(string_literal) string_literal
#endif

// When using the BREAKOUT BOARD only, use these 8 data lines to the LCD:
// For the Arduino Uno, Duemilanove, Diecimila, etc.:
//   D0 connects to digital pin 8  (Notice these are
//   D1 connects to digital pin 9   NOT in order!)
//   D2 connects to digital pin 2
//   D3 connects to digital pin 3
//   D4 connects to digital pin 4
//   D5 connects to digital pin 5
//   D6 connects to digital pin 6
//   D7 connects to digital pin 7

#define YP A3  // must be an analog pin, use "An" notation!
#define XM A2  // must be an analog pin, use "An" notation!
#define YM 9  // can be a digital pin
#define XP 8   // can be a digital pin

#define TS_MINX 150
#define TS_MINY 120
#define TS_MAXX 920
#define TS_MAXY 940

// For better pressure precision, we need to know the resistance
// between X+ and X- Use any multimeter to read it
// For the one we're using, its 300 ohms across the X plate
TouchScreen ts = TouchScreen(XP, YP, XM, YM, 300);

#define LCD_CS A3
#define LCD_CD A2
#define LCD_WR A1
#define LCD_RD A0
// optional
#define LCD_RESET A4

// Assign human-readable names to some common 16-bit color values:
#define	BLACK   0x0000
#define	BLUE    0x001F
#define	RED     0xF800
#define	GREEN   0x07E0
#define CYAN    0x07FF
#define MAGENTA 0xF81F
#define YELLOW  0xFFE0
#define WHITE   0xFFFF

Adafruit_TFTLCD tft(LCD_CS, LCD_CD, LCD_WR, LCD_RD, LCD_RESET);

unsigned long timeStart;
bool cTrigger = false;
float deg=70.0;
float target=70.9;
int magLock = 11;

void printCount(float d) {
  tft.fillRect(25,130,190,60,BLACK);
  tft.setCursor(25,130);
  tft.setTextColor(YELLOW);
  tft.setTextSize(8);
  tft.setTextWrap(true);
  tft.print(d,1);
  tft.print(" F");
}

void check() {
    if((millis() - timeStart) > 3000) 
      digitalWrite(magLock,LOW);
    else
      digitalWrite(magLock,HIGH);
}

void setup(void) {
  Serial.begin(9600);
  tft.reset();
  uint16_t identifier = tft.readID();
  pinMode(13, OUTPUT);
  pinMode(magLock, OUTPUT);
  tft.begin(identifier);
  tft.setRotation(1);
  tft.fillScreen(BLACK);

  //tft.fillRect(320, 0, 160, 320, YELLOW);
  tft.drawTriangle(340,140,400,20,460,140,BLACK);
  tft.fillTriangle(340,140,400,20,460,140,YELLOW);
  tft.drawTriangle(340,180,400,300,460,180,BLACK);
  tft.fillTriangle(340,180,400,300,460,180,YELLOW);
  printCount(deg);
}

#define MINPRESSURE 10
#define MAXPRESSURE 1000

void loop() {
  digitalWrite(13, HIGH);
  TSPoint p = ts.getPoint();
  digitalWrite(13, LOW);
  cTrigger = false;

  // if sharing pins, you'll need to fix the directions of the touchscreen pins
  //pinMode(XP, OUTPUT);
  pinMode(XM, OUTPUT);
  pinMode(YP, OUTPUT);
  //pinMode(YM, OUTPUT);

  // we have some minimum pressure we consider 'valid'
  // pressure of 0 means no pressing!

  if (p.z > MINPRESSURE && p.z < MAXPRESSURE) {
    /*
    Serial.print("("); Serial.print(p.x);
    Serial.print(", "); Serial.print(p.y);
    Serial.println(")");
    */
    
    // scale from 0->1023 to tft.width
    p.x = map(p.x, TS_MINX, TS_MAXX, tft.width(), 0);
    p.y = map(p.y, TS_MINY, TS_MAXY, tft.height(), 0);
    /*
    Serial.print("("); Serial.print(p.x);
    Serial.print(", "); Serial.print(p.y);
    Serial.println(")");
    */
    if(p.y < 110) {
      if(p.x < 240) {
        deg += .1;
        printCount(deg);
      }
      else {
        deg -= .1;
        printCount(deg);
      }
      delay(60);
      Serial.println("Setting flag true");
      cTrigger = true;
    }
  }
  if(int(deg*10) == int(target*10) && cTrigger) {
    Serial.println("on target");
    timeStart = millis();
    check();
  }
  if(int(deg*10) == int(target*10) && !cTrigger)
    check();
  else
    digitalWrite(magLock,HIGH);
}

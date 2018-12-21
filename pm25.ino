#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>


//OLED設定
#define OLED_RESET 4
Adafruit_SSD1306 display(OLED_RESET);

//螢幕設定，定義顯示高度跟寬度
#define LOGO16_GLCD_HEIGHT 16
#define LOGO16_GLCD_WIDTH  16

#if (SSD1306_LCDHEIGHT != 32)
#error("Height incorrect, please fix Adafruit_SSD1306.h!");
#endif
String readString;

void setup() {
  Serial.begin(115200);
  Serial1.begin(57600);
  // by default, we'll generate the high voltage from the 3.3v line internally! (neat!)
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // initialize with the I2C addr 0x3D (for the 128x64)
  // init done
  display.clearDisplay();

}

void loop() {
    //英文字符显示
  display.setTextSize(1);             //设置字体大小
  display.setTextColor(WHITE);        //设置字体颜色白色
  display.setCursor(0,0);             //设置字体的起始位置
  while (Serial1.available())  
  {
    delay(30);  
    if (Serial1.available() >0)
    {
      char c = Serial1.read();  
      readString += c; 
      display.clearDisplay();
    }
  }
  display.setTextSize(4);             //设置字体大小
  display.setCursor(47,4);
  display.print(readString);          //输出文字
  display.display(); 
  delay(3000); 
  readString="";
}


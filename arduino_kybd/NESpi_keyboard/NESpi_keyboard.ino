// YOU MUST DO THIS
//TOOLS/BOARDS/LEONARDO
//SHIT WONT COMPILE IF YOU DONT
int aButton = 2;
int bButton = 3;
int startButton = 4;
int selectButton = 5;
int rightButton = 6;
int upButton = 7;
int downButton = 8;
int leftButton = 9;

void setup() 
{
  pinMode(aButton, INPUT_PULLUP); // Set the pin on input mode alternatively this can be INPUT_PULLUP to invert the signal behavior 
  pinMode(bButton, INPUT_PULLUP);
  pinMode(upButton, INPUT_PULLUP);
  pinMode(leftButton, INPUT_PULLUP);
  pinMode(downButton, INPUT_PULLUP);
  pinMode(rightButton, INPUT_PULLUP);
  pinMode(selectButton, INPUT_PULLUP);
  pinMode(startButton, INPUT_PULLUP);
  Keyboard.begin(); //begins keyboard mode keyboard.end() ends keyboard mode
//https://www.arduino.cc/en/Reference/MouseKeyboard
}

void loop() 
{
   if (digitalRead(aButton) == LOW)  // when the state of buttonOne is low KEY_LEFT_ARROW is sent to the computer 
   { 
    Keyboard.press('z'); 
   } else {
    Keyboard.release('z'); 
   }
   
   if (digitalRead(bButton) == LOW)
   { 
    Keyboard.press('a');
   } else {
    Keyboard.release('a');
   }
   
   if (digitalRead(upButton) == LOW)
   { 
    Keyboard.press(KEY_UP_ARROW); 
   } else {
    Keyboard.release(KEY_UP_ARROW);
   }
   
   if (digitalRead(downButton) == LOW)
   { 
    Keyboard.press(KEY_DOWN_ARROW);
   } else {
    Keyboard.release(KEY_DOWN_ARROW);
   }
   
   if (digitalRead(leftButton) == LOW)
   { 
    Keyboard.press(KEY_LEFT_ARROW); 
   } else {
    Keyboard.release(KEY_LEFT_ARROW);
   }
   
   if (digitalRead(rightButton) == LOW)
   { 
    Keyboard.press(KEY_RIGHT_ARROW); 
   } else {
    Keyboard.release(KEY_RIGHT_ARROW);
   }
   
   if (digitalRead(selectButton) == LOW)
   { 
    Keyboard.press(KEY_LEFT_SHIFT); 
   } else {
    Keyboard.release(KEY_LEFT_SHIFT);
   }
   
   if (digitalRead(startButton) == LOW)
   { 
    Keyboard.press(KEY_LEFT_CTRL); 
   } else {
    Keyboard.release(KEY_LEFT_CTRL);
   }
}

//C++ code will run in a sketch the only arduino specific statements you should need are 
// delay(); takes an integer argument to delay in milliseconds
//digitalWrite(pin, state);
//pinMode(pin, state);



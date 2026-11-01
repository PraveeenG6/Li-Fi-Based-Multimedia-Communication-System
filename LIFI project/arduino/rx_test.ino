//reciever code
#define LDR_PIN 5
#define PERIOD 180
bool previous_state,current_state;
void setup()
   {Serial.begin(9600);
   }
void loop()
 {current_state = get_ldr();
  if(!current_state && previous_state)
  {print_byte(get_byte());}
  previous_state = current_state;}
bool get_ldr()
 {
  return (digitalRead(5)==1) ? true : false;}
char get_byte()
 {char ret = 0;
  delayMicroseconds(PERIOD*1.5);
  for(int i = 0; i < 8; i++){
   ret = ret | get_ldr() << i; 
   delayMicroseconds(PERIOD);}
  return ret;}
void print_byte(char my_byte)
 {char buff[2];
  sprintf(buff, "%c", my_byte);
  Serial.print(buff);}
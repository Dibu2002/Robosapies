#include <ESP8266WiFi.h>
#include <WiFiClient.h>

const uint16_t port = 1234;
const char *host = "192.168.137.1";
WiFiClient client;

const int n = 6;
int m[n] = {14,12,15,13,2,0};

const int len = 10;
char a[len];

int cti(char c)
{
    return (int(c) - 48);
}

int sti(int s)
{
    int n = 0;
    for(int i = s; i < s + 3; i++)
    {
        n *= 10;
        n += cti(a[i]);
    }
    return n;
}
void setup()
{
    pinMode(LED_BUILTIN, OUTPUT);
    digitalWrite(LED_BUILTIN, LOW);
    for(int i = 0; i < n; i++)
        pinMode(m[i], OUTPUT);

    for(int i = 0; i < n; i++)
      digitalWrite(m[i], LOW);

    Serial.begin(9600);
    Serial.println("Connecting...\n");
    WiFi.mode(WIFI_STA);
    WiFi.begin("WIFI", "123456789"); 
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(" .");
    }
    Serial.println("Wifi Connected !!");
    digitalWrite(LED_BUILTIN, HIGH);
}

void loop()
{
    if (!client.connect(host, port))
    {
        Serial.println("Connection to host failed");
        delay(1000);
        return;
    }
//    Serial.println("Connected to server successful!");
    //client.println("Hello From ESP8266");
    delay(250);
    
    for(int i = 0; client.available() > 0; i++)
    {
        a[i] = client.read();
    } 
    for(int i = 0; i < 4; i++)
    {
      digitalWrite(m[i], cti(a[i]));
      Serial.println(cti(a[i]));
    }
    analogWrite (m[4], sti(4));
    Serial.println(sti(4));
    analogWrite (m[5], sti(7));
    Serial.println(sti(7));
    delay(100);
    Serial.println();
    client.stop();
}

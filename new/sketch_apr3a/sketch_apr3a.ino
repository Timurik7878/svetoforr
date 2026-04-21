#include <PubSubClient.h>
#include <WiFi.h>
const char* ssid = "123"; 
const char* pass = "123456789";
const char* mqtt_server = "m2.wqtt.ru";
const int port = 19773;
const char* mqtt_user = "u_S05TZ5";
const char* pass_mqtt = "QBt2pRBO";
WiFiClient espClient;
PubSubClient client(espClient);
void setup() {
  pinMode(2, OUTPUT);
  Serial.begin(115200);
  // put your setup code here, to run once:
  WiFi.begin(ssid, pass);
  while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  Serial.println(WiFi.localIP());
  }
  client.setServer(mqtt_server, port);
  client.setCallback(receivedCallback);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (!client.connected()){
    String clientID = "ESPCLINET";
    if(client.connect(clientID.c_str(), mqtt_user, pass_mqtt)){
      Serial.println("подключен");
      client.subscribe("u_S05TZ5/ledcontrol/#");
    }
  }
  client.loop();
  delay(100);

}

void receivedCallback(char* topic, byte* payload, unsigned int length) {
  String message;
  Serial.println("Получено");
  Serial.println(topic);
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  Serial.println(message);
  if (message == "on"){
    digitalWrite(2, HIGH);
  }
  if (message == "off"){
    digitalWrite(2, LOW);
  }
}
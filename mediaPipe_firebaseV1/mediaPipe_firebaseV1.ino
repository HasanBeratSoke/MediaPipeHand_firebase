//MUCİT PİLOT 2020 ESP8266, Firebase ve App Inventor Kullanımı Örneği
#include "FirebaseESP8266.h"
#include <ESP8266WiFi.h>

//1. Firebase veritabanı adresini, Token bilgisini ve ağ adresi bilgilerinizi giriniz.
#define FIREBASE_HOST "mediapipev2-default-rtdb.firebaseio.com" // http:// veya https:// olmadan yazın
#define FIREBASE_AUTH "LDeRznmvBNMKtOl5UyFM5i7gVsoVpFzDcXo2nkGf"
#define WIFI_SSID "Camlica-b1"
#define WIFI_PASSWORD "52338038"


//2. veritabanim adında bir firebase veritabanı nesnesi oluşturuyoruz
FirebaseData veritabanim;


void setup()
{

  Serial.begin(115200);

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Ağ Bağlantısı Oluşturuluyor");
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(300);
  }
  Serial.println();
  Serial.print("IP adresine bağlanıldı: ");
  Serial.println(WiFi.localIP());
  Serial.println();


  //3. Firebase bağlantısı başlatılıyor

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);

  //4. Ağ bağlantısı kesilirse tekrar bağlanmasına izin veriyoruz
  Firebase.reconnectWiFi(true);
 pinMode(D2,OUTPUT);
 digitalWrite(D2,LOW);
}

void loop()
{

  if(Firebase.getString(veritabanim, "/val")) //Alınacak veri tipine göre getInt, getBool, getFloat, getDouble, getString olarak kullanılabilir.
  {
    //bağlantı başarılı ve veri geliyor ise
    //Serial.print("String tipinde veri alımı başarılı, veri = ");
    //Serial.println(veritabanim.stringData());
    if (veritabanim.stringData()=="1"){
      digitalWrite(D2,HIGH);
    }
    else {
      
      digitalWrite(D2,LOW);
      }
    
    

  }else{
    //hata varsa hata mesajı ve nedeni yazdırılıyor

    Serial.print("Str verisi çekilemedi, ");
    Serial.println(veritabanim.errorReason());
  }


  
////////////////////////////////////////////////////////////////////////////////////
// firebase veritabanına veri göndermek için Firebase.setInt komutu kullanılabilir.
//if(Firebase.setInt(veritabanim, "/led", a))
//  {
//    //bağlantı başarılı ve veri geliyor ise
//     Serial.println("Int tipinde veri gönderimi başarılı");
// 
//  }else{
//    //hata varsa hata mesajı ve nedeni yazdırılıyor
//
//    Serial.print("Int tipindeki veri gönderilemedi, ");
//    Serial.println(veritabanim.errorReason());
//  }


  
}

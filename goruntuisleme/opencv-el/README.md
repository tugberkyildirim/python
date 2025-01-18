# El Tespiti Uygulaması (OpenCV ve Mediapipe)

Bu proje, OpenCV ve Mediapipe kütüphanelerini kullanarak gerçek zamanlı el tespiti ve izleme yapar. Uygulama, bir web kamerası aracılığıyla elde edilen görüntülerde elleri algılar, parmak eklemlerini çizer ve algılanan ellerin sayısını ekranda gösterir.

## Özellikler

- **El Tespiti:** Maksimum iki elin tespiti.
- **Parmak İskeleti Çizimi:** Tespit edilen ellerin parmak eklemleri ve bağlantıları çizilir.
- **El Türü Tespiti:** Sol veya sağ el olduğunu belirler.
- **Kullanıcı Bilgilendirmesi:** Çıkmak için "ESC" tuşuna basılması gerektiği ekranda belirtilir.

## Gereksinimler

Bu uygulamayı çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekir:

- Python 3.7 veya üstü
- OpenCV
- Mediapipe

Gerekli kütüphaneleri yüklemek için aşağıdaki komutları kullanabilirsiniz:

```bash
pip install opencv-python mediapipe
```

## Kodun Açıklaması

### Önemli Modüller

- **cv2:** OpenCV kütüphanesi, görüntü işleme ve kamera kontrolü için kullanılır.
- **mediapipe:** El tespiti ve parmak iskeleti çizimi için güçlü bir çözümdür.

### Ana Akış

1. **El Algılama:**
   - Mediapipe'in Hands modülü, elleri ve parmak eklemlerini algılar.
   - Çerçeve RGB formatına dönüştürülür ve el algılama işlemi gerçekleştirilir.

2. **Parmak Eklemleri Çizimi:**
   - Mediapipe'in çizim fonksiyonları kullanılarak tespit edilen ellerin parmak eklemleri çizilir.

3. **El Türü Belirleme:**
   - Algılanan elin sol veya sağ el olduğu belirlenir ve ekranda gösterilir.

4. **Bilgilendirme ve Çıkış:**
   - Uygulama çalışırken "ESC" tuşuna basılarak çıkılabilir.

### Çalıştırma

1. Kamerayı başlatmak için kodu çalıştırın:

   
```bash
   python opencv-el.py
```

2. Kamera açıldığında, algılanan elleri ve parmak eklemlerini göreceksiniz.
3. Uygulamadan çıkmak için ESC tuşuna basın.

## Lisans

Bu proje MIT Lisansı altında sunulmaktadır. Daha fazla bilgi için LICENSE dosyasını inceleyin.

---
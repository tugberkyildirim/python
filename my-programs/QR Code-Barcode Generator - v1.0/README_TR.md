# QR Kod ve Barkod Oluşturma Uygulaması

Bu uygulama, çeşitli barkod türleri ve QR kod oluşturmak için geliştirilmiştir. Kullanıcıların kurulum gerektirmeksizin bu uygulamayı çalıştırarak kolayca barkodlar ve QR kodlar oluşturabilir ve ardından bu kodları belirtilen klasörlere kaydedebilirler.

## Özellikler

- **QR Kodları**: Kullanıcılar metin, URL veya diğer verileri kullanarak QR kodları oluşturabilir.
- **Barkodlar**: Desteklenen barkod türleri arasında EAN, UPC, Code128, Code39 gibi popüler barkodlar bulunmaktadır.
- **Kayıt Özelliği**: Oluşturulan QR kodları ve barkodlar, sırasıyla `Data/QR Code` ve `Data/Barcode` klasörlerine kaydedilir.
- **Desteklenen Barkod Türleri**: Program, aşağıdaki barkod türlerini destekler:
  - **EAN-13**
  - **EAN-8**
  - **UPC-A**
  - **UPC-E**
  - **Code128**
  - **Code39**
  - **Interleaved 2 of 5**
  - **ITF-14**
  - **EAN-14**
  - **Codabar**
  - **MSI Plessey**
  - **ISBN**
  - **ISBN-13**
  - **ISSN**
  
## Kurulum

### Windows Uygulaması

Bu uygulama, bağımsız bir `.exe` dosyasıdır.
1. İndirilen `.exe` dosyasını çalıştırarak uygulamayı açın.

## Kullanım

1. **QR Kod Oluşturma**:
   - Ana ekranda, oluşturmak istediğiniz QR kodu için metin veya URL girin.
   - "QR Kod Oluştur" butonuna tıklayın.
   - QR kodu `Data/QR Code` klasörüne `.png` formatında kaydedilecektir.

2. **Barkod Oluşturma**:
   - Ana ekranda, oluşturmak istediğiniz barkod için metin girin.
   - Barkod türünü seçin (örn. EAN-13, Code128 vb.).
   - "Barkod Oluştur" butonuna tıklayın.
   - Barkod `Data/Barcode` klasörüne `.png` formatında kaydedilecektir.

### Desteklenen Barkod Türleri

Aşağıdaki barkod türlerini desteklemektedir:

- **EAN-13**: EAN-13 Barkodu
- **EAN-8**: EAN-8 Barkodu
- **UPC-A**: UPC-A Barkodu
- **UPC-E**: UPC-E Barkodu
- **Code128**: Code128 Barkodu
- **Code39**: Code39 Barkodu
- **Interleaved 2 of 5**: Interleaved 2 of 5 Barkodu
- **ITF-14**: ITF-14 Barkodu
- **EAN-14**: EAN-14 Barkodu
- **Codabar**: Codabar Barkodu
- **MSI Plessey**: MSI Plessey Barkodu
- **ISBN**: ISBN Barkodu
- **ISBN-13**: ISBN-13 Barkodu
- **ISSN**: ISSN Barkodu

### Kayıt

Oluşturduğunuz QR kodları ve barkodlar sırasıyla aşağıdaki klasörlere kaydedilir:
- **QR Kodlar**: `Data/QR Code`
- **Barkodlar**: `Data/Barcode`

## Program Akışı

1. **QR Kod Oluşturma**:
   - Kullanıcılar metin veya URL girerek QR kodu oluşturabilir.
   - Oluşturulan QR kodu belirtilen klasöre kaydedilir.

2. **Barkod Oluşturma**:
   - Kullanıcılar barkod verisini girer ve türü seçer.
   - Seçilen barkod türüne göre barkod oluşturulur ve belirtilen klasöre kaydedilir.

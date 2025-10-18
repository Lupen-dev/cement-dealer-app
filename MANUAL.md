# Cement Dealer Management System - User Guide (Turkish)

## Çimento Bayisi Yönetim Sistemi - Kullanıcı Kılavuzu

Merhaba! Bu sistem sizin çimento ticaretinizi profesyonel ve düzenli bir şekilde yönetmeniz için tasarlanmıştır.

### 📋 Sistem Özellikleri

1. **Müşteri Yönetimi**
   - Müşteri bilgilerini kaydetme (isim, telefon, email, adres)
   - Her müşterinin siparişlerini görüntüleme
   - Müşteriye ait toplam bakiye görüntüleme

2. **Sipariş Takibi**
   - Yeni siparişler oluşturma
   - Miktar ve fiyat belirleme
   - Ödeme yöntemi ve ödeme vadesini seçme
   - Siparişin durumunu takip etme (Beklenen, Teslim Edildi, Kısmen Ödendi, Ödenmiş)

3. **Tahsilat Defteri**
   - Müşteri ödemelerini kaydetme
   - Kısmi ödemeleri izleme
   - Kullanılan ödeme yöntemini kaydetme
   - Tüm işlemleri geçmiş olarak görüntüleme

4. **Raporlar**
   - Dashboard: Ana göstergeler ve son siparişler
   - Bekleyen Tahsilatlar: Ödenmemiş siparişler
   - Müşteri Raporu: Her müşterinin finansal özeti

### 🚀 Kurulum Adımları

#### Windows PowerShell'de:

1. Proje klasörüne gidin:
   ```powershell
   cd c:\Users\Zirve\Documents\banka\cement-dealer-app
   ```

2. Kurulum scriptini çalıştırın:
   ```powershell
   .\setup.ps1
   ```

3. Uygulamayı başlatın:
   ```powershell
   .\run.ps1
   ```

4. Tarayıcıda açın: http://localhost:5000

#### Windows CMD'de:

1. Proje klasörüne gidin:
   ```cmd
   cd c:\Users\Zirve\Documents\banka\cement-dealer-app
   ```

2. Kurulum scriptini çalıştırın:
   ```cmd
   setup.bat
   ```

3. Uygulamayı başlatın:
   ```cmd
   run.bat
   ```

4. Tarayıcıda açın: http://localhost:5000

### 💼 Günlük Kullanım

#### Yeni Müşteri Ekleme

1. **Müşteriler** menüsüne tıklayın
2. **+ Müşteri Ekle** butonuna tıklayın
3. Müşteri bilgilerini girin:
   - Adı (zorunlu)
   - Telefon numarası
   - Email adresi
   - Adresi
4. **Müşteri Kaydet** butonuna tıklayın

#### Yeni Sipariş Oluşturma

1. **Siparişler** menüsüne tıklayın
2. **+ Yeni Sipariş** butonuna tıklayın
3. Sipariş bilgilerini girin:
   - Müşteri seçin
   - Miktarı girin (ton cinsinden)
   - Birim fiyatı girin (Toplam otomatik hesaplanır)
   - Ödeme yöntemi seçin
   - Ödeme vadesini seçin (mesela Net 7 = 7 günde ödeme)
4. İsteğe bağlı olarak notlar ekleyin
5. **Sipariş Oluştur** butonuna tıklayın

#### Ürün Teslim Etme

1. **Siparişler** sayfasında ilgili siparişin **Görüntüle** butonuna tıklayın
2. **Teslim Edildi Olarak İşaretle** butonuna tıklayın
3. Sistem teslim tarihini otomatik olarak kaydeder

#### Ödeme Kaydetme

1. **Tahsilat** menüsüne tıklayın
2. **+ Ödeme Kaydet** butonuna tıklayın
3. Bilgileri girin:
   - Ödenecek siparişi seçin
   - Ödenen tutarı girin
   - Ödeme yöntemini seçin (Nakit, Çek, Banka Transferi, etc.)
   - Notlar ekleyin (opsiyonel)
4. **Ödeme Kaydet** butonuna tıklayın
5. Sistem sipariş durumunu otomatik olarak güncelleyecektir

#### Raporlar Görüntüleme

- **Ana Sayfa (Dashboard)**: Genel istatistikler ve son siparişler
- **Bekleyen Tahsilatlar**: Ödenmemiş ve kısmen ödenmiş tüm siparişleri gösterir
- **Müşteri Raporu**: Belirli bir müşterinin tüm siparişlerini ve finansal bilgilerini gösterir

### 📊 Sipariş Durumları

- **Beklenen (Pending)**: Henüz teslim edilmemiş sipariş
- **Teslim Edildi (Delivered)**: Teslim edilmiş, ödeme bekleniyor
- **Kısmen Ödendi (Partially Paid)**: Bir kısmı ödenmiş
- **Ödenmiş (Paid)**: Tamamı ödenmiş

### 💰 Ödeme Yöntemleri

Sistem varsayılan olarak şu ödeme yöntemlerini sunar:
- Nakit (Cash)
- Çek (Cheque)
- Banka Transferi (Bank Transfer)
- Kredi (Credit)

İhtiyacınıza göre daha fazla yöntem ekleyebilirsiniz.

### 📅 Ödeme Vadeleri

Sistem varsayılan olarak şu ödeme vadeleri sunar:
- Nakit: 0 gün (hemen ödeme)
- Net 7: 7 gün
- Net 15: 15 gün
- Net 30: 30 gün
- Net 45: 45 gün
- Net 60: 60 gün

### 📈 İpuçları ve En İyi Uygulamalar

1. **Her Zaman Teslim Etme Tarihini Güncelleyin**: Çimentoyu gönderdikten hemen sonra siparişi "Teslim Edildi" olarak işaretleyin. Bu sayede tahsilat tarihi doğru hesaplanır.

2. **Bekleyen Tahsilatlar Raporunu Kontrol Edin**: Her gün "Bekleyen Tahsilatlar" raporunu kontrol ederek vadesi geçmiş ödemeleri takip edin.

3. **Müşteri Raporlarını Kullanın**: Müşteri ile görüşmeden önce o müşterinin detaylı raporunu görüntüleyin.

4. **Notlar Ekleyin**: Siparişlere ve ödemelere notlar ekleyerek bu işlem hakkında hatırlatıcı bilgiler saklayın.

5. **Düzenli Yedek Alın**: Veritabanı dosyasını (cement_dealer.db) düzenli olarak yedekleyin.

### ⚙️ Sorun Giderme

#### Uygulama başlamıyor

**Çözüm 1**: Virtual environment'ı yeniden oluşturun
```powershell
rmdir /s venv
.\setup.ps1
```

**Çözüm 2**: Python kurulumunu kontrol edin
```powershell
python --version
```

#### "Port 5000 already in use" hatası

Bu, başka bir uygulamanın 5000 numaralı portu kullandığı anlamına gelir. 
Başka bir port kullanabilirsiniz. `run.py` dosyasını açıp şu kısmı değiştirin:

```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # 5001'i kullanın
```

Sonra http://localhost:5001 adresine gidin.

#### Veritabanı hataları

Veritabanı dosyasını silin ve yeniden başlatın:
```powershell
Remove-Item cement_dealer.db
.\run.ps1
```

### 🆘 Destek

Sorularınız veya önerileriniz varsa lütfen geliştirici ekibine başvurun.

---

**Son Güncelleme**: Ekim 2025

**Sürüm**: 1.0.0

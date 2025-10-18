# 🚀 QUICK START GUIDE - Çimento Bayisi Yönetim Sistemi

## Hızlı Başlangıç (5 Dakika)

### Adım 1: Uygulamayı Başlatın

**PowerShell kullanıyorsanız:**
```powershell
cd c:\Users\Zirve\Documents\banka\cement-dealer-app
.\setup.ps1    # İlk kez bir defa çalıştırın
.\run.ps1      # Her seferinde bunu çalıştırın
```

**Komut İstemi (CMD) kullanıyorsanız:**
```cmd
cd c:\Users\Zirve\Documents\banka\cement-dealer-app
setup.bat      # İlk kez bir defa çalıştırın
run.bat        # Her seferinde bunu çalıştırın
```

### Adım 2: Tarayıcıyı Açın

http://localhost:5000 adresine gidin

### Adım 3: İlk Müşteri Ekleyin

1. **Müşteriler** menüsüne tıklayın
2. **+ Müşteri Ekle** butonuna tıklayın
3. Müşteri adı girin
4. Telefon ve diğer bilgileri girin (opsiyonel)
5. **Müşteri Kaydet**'e tıklayın

### Adım 4: Sipariş Oluşturun

1. **Siparişler** menüsüne tıklayın
2. **+ Yeni Sipariş** butonuna tıklayın
3. Müşteri seçin
4. Miktarı girin (ton cinsinden)
5. Birim fiyatı girin
6. Ödeme yöntemi ve vadesini seçin
7. **Sipariş Oluştur**'a tıklayın

### Adım 5: Siparişi Teslim Etmek İçin İşaretle

1. Siparişin sayfasında **Teslim Edildi Olarak İşaretle** butonuna tıklayın
2. (Sistem otomatik olarak teslim tarihini kaydeder)

### Adım 6: Ödeme Kaydedin

1. **Tahsilat** menüsüne tıklayın
2. **+ Ödeme Kaydet** butonuna tıklayın
3. Siparişi seçin
4. Ödenen tutarı girin
5. Ödeme yöntemini seçin
6. **Ödeme Kaydet**'e tıklayın

### Adım 7: Raporları Görüntüleyin

- **Ana Sayfa**: Genel bakış
- **Bekleyen Tahsilatlar**: Ödenmemiş siparişler
- Müşteri detayında: O müşteriye ait bilgiler

---

## 📋 Önemli Menüler

| Menü | Açıklama |
|------|----------|
| **Müşteriler** | Müşteri bilgilerini yönetin |
| **Siparişler** | Tüm siparişleri görüntüleyin |
| **Tahsilat** | Ödeme kayıtlarını yönetin |
| **Bekleyen Tahsilatlar** | Vadesi geçmiş ödemeleri kontrol edin |

---

## ✅ Workflow Örneği

```
Müşteri Ekleme → Sipariş Oluşturma → Ürün Teslimi → Ödeme Kaydetme
      ↓              ↓                    ↓              ↓
   Ahmet           50 ton          Teslim Edildi   ₺50.000 alındı
   0555123456   ₺1.000/ton        Otomatik         Ödeme durumu
   Adres:       Toplam: ₺50.000   kaydedilir       güncellendi
```

---

## 🎯 Sık Yapılan İşlemler

### Müşterinin Tüm Bilgilerini Görmek
1. **Müşteriler**'e tıklayın
2. Müşteri adında **Görüntüle**'ye tıklayın
3. Tüm siparişleri, ödemeleri ve bakiyesi görüntülenir

### Belirli bir Siparişin Detaylarını Görmek
1. **Siparişler**'e tıklayın
2. Sipariş numarasında **Görüntüle**'ye tıklayın
3. Tüm detaylar ve yapılan ödemeler görüntülenir

### Ödenmemiş Siparişleri Görmek
1. **Bekleyen Tahsilatlar** raporuna tıklayın
2. Tüm ödenmemiş ve kısmen ödenmiş siparişler listelenir
3. Vadesi geçmiş olanlar "overdue" olarak işaretlenir

### Kısmen Ödenen Siparişe Ek Ödeme Kaydetmek
1. **Tahsilat** → **+ Ödeme Kaydet**
2. Aynı siparişi seçin
3. Kalan tutarı girin
4. Sistem otomatik olarak durumu "Ödenmiş" olarak değiştirecektir

---

## 🔧 Teknik Bilgiler

- **Veritabanı**: SQLite (cement_dealer.db)
- **Port**: 5000
- **Tarayıcı**: Chrome, Firefox, Edge, Safari
- **İşletim Sistemi**: Windows, Linux, Mac

---

## 💡 İpuçları

✓ Her işlemde **Notlar** alanını kullanın (ödeme yöntemi, müşteri talimatları, vb.)

✓ **Dashboard**'dan ana metrikleri hızlıca kontrol edin

✓ **Bekleyen Tahsilatlar** raporunu günlük kontrol edin

✓ Önemli verileri yedekleyin (cement_dealer.db dosyası)

---

## ❓ Sorunlar

**Uygulama başlamıyorsa:**
- Kurulum scriptini tekrar çalıştırın
- Python'ın kurulu olduğunu kontrol edin

**Veri kaybolmuş gibi görünüyorsa:**
- Tarayıcıyı yenileyin (F5)
- Uygulamayı yeniden başlatın

**Port hatası alıyorsanız:**
- Başka bir uygulamayı kapatın veya farklı bir port kullanın

---

**Daha ayrıntılı bilgi için MANUAL.md dosyasını okuyun**

Keyifli kullanımlar! 🎉

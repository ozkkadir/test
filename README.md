# Cam Balkon ve Profil Stok Sistemi

Bu proje, marka bazlı cam balkon ve diğer profil serilerinin stok ve fiyat takibini yapmak için Python ve Flask kullanarak geliştirilmiş basit bir prototip içerir.

## Özellikler

- SQLite veritabanı kullanarak marka, seri, profil ve renk takibi
- Excel/CSV formatındaki fiyat listelerini içe aktarma
- Profil renklerine göre fiyat çarpanı belirleme
- Basit web arayüzü üzerinden sipariş oluşturma ve fiyat hesaplama

## Gereksinimler

- Python 3.10+
- `pip install -r requirements.txt`

Uygulamayı başlatmak için:

```bash
python app.py
```

Uygulama varsayılan olarak `http://127.0.0.1:5000` adresinde çalışacaktır.

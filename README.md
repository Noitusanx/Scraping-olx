# Scraping OLX - Mobil Bekas
---
## Tujuan

Project ini bertujuan untuk melakukan web scraping pada situs web OLX sehingga mendapatkan informasi mengenai mobil bekas seperti brand, tahun, kilometer dan harga dari mobil bekas tersebut.

## Langkah-langkah

1. **Buat Environment**
```bash
    python -m venv env-bigdata-course
```
2. **Aktifkan Python virtual environment**
```bash
    source env-bigdata-course/bin/activate
```
3. **Install Scrapy**
```bash
    pip install scrapy
```
4. **Buat project Scrapy baru**
```bash
    scrapy startproject scrapping
```
5. **Jalankan spider yang akan menghasilkan format output JSON**
```bash
    scrapy crawl myspider -o scrapping.json
```

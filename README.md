# pdf-ocr-tr

Taranmış PDF'lerden metin çıkarır. Türkçe ve İngilizce çalışıyor.

```
python pdf_ocr.py belge.pdf tur
python pdf_ocr.py belge.pdf tur+eng --output sonuc.txt
```

Gerekenler: `pip install pytesseract pdf2image`, bir de bilgisayarda Tesseract (Türkçe dil paketiyle) ve Poppler kurulu olmalı.
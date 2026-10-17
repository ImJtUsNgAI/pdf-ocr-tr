#!/usr/bin/env python3
"""
PDF OCR Sistemi
Taramalı PDF'lerden metin çıkarır. Türkçe ve İngilizce destekler.
Kullanım: python3 pdf_ocr.py <input.pdf> [dil] [--output dosya.txt]
Örnek:    python3 pdf_ocr.py belge.pdf tur
          python3 pdf_ocr.py belge.pdf tur+eng --output sonuc.txt
"""

import sys
import os
import argparse
import pytesseract
from pdf2image import convert_from_path

def pdf_ocr(pdf_path: str, lang: str = "tur+eng", output_path: str = None, dpi: int = 300):
    """
    PDF dosyasını OCR ile tarar ve metni çıkarır.

    Args:
        pdf_path: PDF dosyasının yolu
        lang: Tesseract dil kodu (örn: "tur", "eng", "tur+eng")
        output_path: Çıktı metin dosyasının yolu (None = yazdırır)
        dpi: Görüntü çözünürlüğü (yüksek = daha doğru ama yavaş)
    """
    if not os.path.exists(pdf_path):
        print(f"HATA: Dosya bulunamadı: {pdf_path}")
        sys.exit(1)

    print(f"PDF okunuyor: {pdf_path}")
    print(f"Dil: {lang} | DPI: {dpi}")

    # PDF'i görüntülere dönüştür
    try:
        images = convert_from_path(pdf_path, dpi=dpi)
    except Exception as e:
        print(f"HATA: PDF açılamadı: {e}")
        sys.exit(1)

    print(f"Toplam sayfa: {len(images)}")
    
    full_text = []

    for i, image in enumerate(images, start=1):
        print(f"  Sayfa {i}/{len(images)} işleniyor...", end="\r")
        text = pytesseract.image_to_string(image, lang=lang)
        full_text.append(f"=== SAYFA {i} ===\n{text.strip()}\n")

    print("\nOCR tamamlandı!")

    result = "\n\n".join(full_text)

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"Metin kaydedildi: {output_path}")
    else:
        print("\n" + "="*60)
        print(result)

    return result


def main():
    parser = argparse.ArgumentParser(description="PDF OCR - Taramalı PDF'den metin çıkar")
    parser.add_argument("pdf", help="PDF dosyasının yolu")
    parser.add_argument("lang", nargs="?", default="tur+eng",
                        help="Dil kodu: tur, eng, tur+eng (varsayılan: tur+eng)")
    parser.add_argument("--output", "-o", help="Çıktı dosyası (.txt)")
    parser.add_argument("--dpi", type=int, default=300, help="Çözünürlük (varsayılan: 300)")
    args = parser.parse_args()

    pdf_ocr(args.pdf, lang=args.lang, output_path=args.output, dpi=args.dpi)


if __name__ == "__main__":
    main()

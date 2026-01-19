!apt-get update
!apt-get install -y tesseract-ocr tesseract-ocr-ben poppler-utils
!pip install pytesseract pdf2image pillow pandas regex

from google.colab import files
uploaded = files.upload()
print(uploaded.keys())

from pdf2image import convert_from_path
import pytesseract
import re

def clean_bangla_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\u0980-\u09FF0-9।, ]', '', text)
    return text.strip()

all_rows = []

for pdf_name in uploaded.keys():
    pages = convert_from_path(pdf_name, dpi=300)
    print(f"Processing {pdf_name}, pages: {len(pages)}")

    for page_no, page in enumerate(pages, start=1):
        raw_text = pytesseract.image_to_string(page, lang="ben")
        clean_text = clean_bangla_text(raw_text)

        if len(clean_text) > 20:  # ignore empty/noise pages
            all_rows.append({
                "file": pdf_name,
                "page": page_no,
                "text": clean_text
            })

print("Total extracted pages:", len(all_rows))

import pandas as pd

df = pd.DataFrame(all_rows)

csv_name = "extracted_bangla_text.csv"
df.to_csv(csv_name, index=False, encoding="utf-8-sig")

print("✅ CSV created:", csv_name)
df.head()

!ls -lh

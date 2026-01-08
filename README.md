# 📘 Extract Text from NCTB TextBooks or HandBOOKs (Bangla OCR Pipeline)

Extract Text from NCTB TextBooks or HandBOOKs is an open-source Python project that provides a complete **Bangla OCR (Optical Character Recognition) pipeline** to extract Bengali text from **scanned or image-based PDF textbooks and handbooks**.

This repository is designed for:
- NCTB textbook digitization
- Bangla NLP dataset creation
- LLM training and fine-tuning
- Academic and research purposes in Bangladesh

---

## 🚀 Project Highlights

- 📄 Works with **scanned / image-based PDFs**
- 🧠 Bangla OCR using **Tesseract (ben)**
- 🗂 Page-wise text extraction with page numbers
- 📊 Export output to **CSV format**
- ⚡ Supports large PDF files with batch processing
- 💻 Works on **Google Colab, Ubuntu, and local Linux**

---

## 🌾 Use Cases

- 📘 Extract text from **NCTB textbooks (Class 1–12)**
- 🧠 Build Bangla NLP datasets
- 🤖 Train or fine-tune **Bangla LLMs**
- 📊 Text mining and academic research
- 📚 Educational content digitization
- 🌾 Agriculture and Krishi Sikkha book processing

---

## 🛠 Requirements
pip install pytesseract pdf2image pillow pandas regex

### System Dependencies (Ubuntu / Google Colab)

```bash
apt update
apt install -y tesseract-ocr tesseract-ocr-ben poppler-utils

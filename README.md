# Image Steganography Student Scaffold

This package contains starter files for a simple image-based steganography lab.

## Files

- `embed.py` — scaffold for hiding a secret message inside an image
- `extract.py` — scaffold for recovering the hidden message
- `secret.txt` — example secret message
- `requirements.txt` — Python dependencies
- `Steganography_Colab_Setup.ipynb` — Google Colab setup notebook

## Student task

Complete all `TODO` sections in:

1. `embed.py`
2. `extract.py`

The completed program should:

1. Read a cover image.
2. Convert a text message into bits.
3. Hide those bits in selected image pixels.
4. Save a stego-image.
5. Extract the message again using the same configuration.

## Recommended first configuration

```python
key = 12345
colourPlane = 0
significantBit = 7
coverImage = "your_image.bmp"
secretFile = "secret.txt"
```

## Running locally

```bash
pip install -r requirements.txt
python embed.py
python extract.py
```

## Running in Google Colab

1. Upload `steg_scaffold_student.zip`.
2. Run the setup notebook.
3. Upload a BMP image.
4. Complete the TODOs.
5. Run `embed.py` and `extract.py`.

## Capacity formula

```text
capacity in bits = width × height
capacity in bytes = capacity in bits / 8
```

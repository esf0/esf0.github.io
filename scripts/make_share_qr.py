"""Build the inline SVG QR codes for the /share/ page.

Run from the repository root:
    uv run --with qrcode scripts/make_share_qr.py
"""
from pathlib import Path

import qrcode
import qrcode.image.svg

TARGETS = {
    "share-qr-home.svg": "https://esf0.github.io/",
    "share-qr-cv.svg": "https://esf0.github.io/cv/",
}

out_dir = Path("_includes")
for name, url in TARGETS.items():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(image_factory=qrcode.image.svg.SvgPathImage)
    svg = img.to_string(encoding="unicode")
    (out_dir / name).write_text(svg + "\n")
    print(f"{name}: {url} (version {qr.version})")

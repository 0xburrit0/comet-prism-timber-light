#!/usr/bin/env python3
"""
Optimize a company logo image for use as an iOS Contacts profile picture.

- Square 1024x1024 canvas
- White background
- Logo centered with comfortable padding for circular crop
- High-quality JPEG under ~200KB
"""

import sys
from pathlib import Path
from PIL import Image, ImageOps

TARGET_SIZE = 1024
PADDING_RATIO = 0.18  # fraction of canvas left as margin around logo
MAX_BYTES = 200_000
QUALITY_START = 92


def optimize_logo(input_path: str, output_path: str) -> None:
    img = Image.open(input_path).convert("RGBA")

    # Create white background canvas
    canvas = Image.new("RGBA", (TARGET_SIZE, TARGET_SIZE), (255, 255, 255, 255))

    # Calculate available space for logo (with padding)
    max_logo_side = int(TARGET_SIZE * (1 - 2 * PADDING_RATIO))

    # Scale logo to fit inside max_logo_side while preserving aspect ratio
    img.thumbnail((max_logo_side, max_logo_side), Image.Resampling.LANCZOS)

    # Center the logo on the canvas
    x = (TARGET_SIZE - img.width) // 2
    y = (TARGET_SIZE - img.height) // 2
    canvas.paste(img, (x, y), img)

    # Convert to RGB for JPEG
    final = canvas.convert("RGB")

    # Save with quality loop to stay under size limit
    quality = QUALITY_START
    while quality >= 70:
        final.save(output_path, "JPEG", quality=quality, optimize=True)
        if Path(output_path).stat().st_size <= MAX_BYTES:
            break
        quality -= 4

    print(f"Saved: {output_path} ({Path(output_path).stat().st_size} bytes, quality={quality})")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: optimize_logo.py <input_image> <output.jpg>")
        sys.exit(1)
    optimize_logo(sys.argv[1], sys.argv[2])

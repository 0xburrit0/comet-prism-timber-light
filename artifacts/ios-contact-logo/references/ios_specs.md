# iOS Contacts Profile Picture Specs

## Optimal Format

- **Shape**: Square source image (iOS crops to circle)
- **Resolution**: 1024×1024 px (Retina-ready; 512×512 is minimum practical)
- **Format**: JPEG (supported; also PNG/BMP/GIF)
- **File size**: ≤ 224 KB (iCloud Contacts hard limit is 224 KB; aim ≤ 200 KB)
- **Background**: Solid white preferred for logos (transparent becomes black or unpredictable)
- **Composition**: Logo centered with ~15–20% padding on all sides so circular crop does not clip important elements
- **Quality**: High visual fidelity; avoid heavy compression artifacts

## Why these choices

- Circular display means corner content is cropped — keep critical logo content well inside the circle.
- 1024 px provides sharp results on modern devices without exceeding practical size limits.
- White background ensures consistent appearance across light/dark interfaces and circular masks.

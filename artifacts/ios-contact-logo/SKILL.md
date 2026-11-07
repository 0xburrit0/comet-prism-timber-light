---
name: ios-contact-logo
description: "Generate one or two optimized company logo JPGs ready for use as iOS Contacts profile pictures. Use when the user provides a business name (e.g. 'Ford') and wants a clean logo contact photo."
type: workflow
lifecycle: active
---

# iOS Contact Logo

Generate optimized company logo images for iOS Contacts profile pictures. The user supplies only a business name; return 1–2 ready-to-use JPG files.

## Workflow

1. **Extract the company name**  
   The user prompt is the business name (e.g. "Ford", "Apple", "Starbucks"). Use it exactly as given. If the name is ambiguous or missing, ask for clarification in one short sentence.

2. **Find official logos**  
   Use `search_images` (and optionally `web_search` + `browse_page`) to locate high-quality official logos.  
   Preferred queries:  
   - `"[Company] official logo"`  
   - `"[Company] logo png"`  
   - `"[Company] wordmark"` or `"[Company] script logo"` for alternatives  
   Prioritize clean versions on white or transparent backgrounds from official or reputable sources. Avoid low-resolution, watermarked, or fan-made images.

3. **Select variants**  
   - Prefer **two unique options** when distinct proper versions exist (e.g. full logo + wordmark/script only).  
   - If only one high-quality official logo is available, return that single option.  
   - A single option must always be the official logo (never a generated or stylized approximation).

4. **Download candidate images**  
   Save the best 1–2 source images to disk (e.g. `/tmp/logo_full.png`, `/tmp/logo_wordmark.png`).

5. **Optimize each image**  
   Run the bundled script for every candidate:  
   ```bash
   python3 scripts/optimize_logo.py /tmp/source.png /workspace/artifacts/company-name-option1.jpg
   ```  
   The script produces a 1024×1024 white-background JPEG with centered logo and padding suitable for circular crop, kept under 200 KB.

6. **Deliver results**  
   Present the final JPG(s) to the user using `<grok type="render_file" file_path="..."/>`.  
   Label them clearly (e.g. "Official oval logo", "Script wordmark").  
   Briefly note that the images are square and optimized for the circular iOS Contacts photo crop.

## Specs

See `references/ios_specs.md` for exact size, format, and composition requirements.

## Notes

- Prefer real official logos over AI-generated ones.  
- If a logo has a complex background, use `edit_image` to clean it to white before optimization, or select a cleaner source.  
- File names should include the company name and variant for clarity.

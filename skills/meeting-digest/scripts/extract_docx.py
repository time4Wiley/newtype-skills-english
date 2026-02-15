#!/usr/bin/env python3
"""
Extract text from .docx files with paragraph preservation.
Usage: python extract_docx.py <path_to_docx>

Outputs clean text with paragraph breaks, suitable for meeting transcript analysis.
"""

import sys

def extract_text(docx_path: str) -> str:
    """Extract all non-empty paragraphs from a .docx file."""
    try:
        from docx import Document
    except ImportError:
        import subprocess
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "python-docx",
             "--break-system-packages", "-q"]
        )
        from docx import Document

    doc = Document(docx_path)
    paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    return "\n\n".join(paragraphs)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_docx.py <path_to_docx>")
        sys.exit(1)

    text = extract_text(sys.argv[1])
    print(text)

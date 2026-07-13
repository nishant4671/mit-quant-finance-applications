import os
import re

def compile_textbook():
    # Workspace root directory
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    theory_dir = os.path.join(base_dir, "notes", "theory")
    output_path = os.path.join(base_dir, "MIT_18_642_Textbook.md")

    # Map of lectures to their filenames
    # As the user progresses, we can add more chapters here
    chapters = [
        {"title": "Financial Terms, Concepts, and Bond Math", "file": "L01_Bond_Math.md"}
    ]

    compiled_content = []
    compiled_content.append("# 📖 MIT 18.642: Quantitative Finance & Mathematical Foundations")
    compiled_content.append("## Personal Student Companion (Printable Version)")
    compiled_content.append("\n---\n")
    
    # User preference headers
    compiled_content.append("> **Format:** Applied & Practical (Intuition Focus)\n> **Code & Derivations:** Omitted from print layout (Interactive code remains in lab files)\n")
    compiled_content.append("\n---\n")
    
    compiled_content.append("## 📋 Table of Contents\n")
    for i, ch in enumerate(chapters, 1):
        clean_anchor = ch["title"].lower().replace(" ", "-").replace(",", "").replace("&", "and")
        compiled_content.append(f"{i}. [Chapter {i}: {ch['title']}](#{clean_anchor})")
    compiled_content.append("\n<div style='page-break-after: always;'></div>\n")

    for i, ch in enumerate(chapters, 1):
        file_path = os.path.join(theory_dir, ch["file"])
        if not os.path.exists(file_path):
            print(f"Warning: File {file_path} not found.")
            continue
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Strip out the main document title (e.g. # 📓 Lecture 1: ...)
        content = re.sub(r"^#\s+.*$", "", content, flags=re.MULTILINE)
        
        # Strip out code blocks (```python ... ```) just in case
        content = re.sub(r"```python.*?```", "", content, flags=re.DOTALL)
        
        # Create a clean markdown anchor
        clean_anchor = ch["title"].lower().replace(" ", "-").replace(",", "").replace("&", "and")
        chapter_header = f"\n# <a name='{clean_anchor}'></a>Chapter {i}: {ch['title']}\n"
        
        compiled_content.append(chapter_header)
        compiled_content.append(content.strip())
        
        # Add a page break after each chapter
        compiled_content.append("\n<div style='page-break-after: always;'></div>\n")
        
    # Write the compiled file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(compiled_content))
        
    print(f"Successfully compiled textbook to: {output_path}")

if __name__ == "__main__":
    compile_textbook()

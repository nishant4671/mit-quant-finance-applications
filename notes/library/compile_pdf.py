import os
import re
from fpdf import FPDF
from mistletoe import markdown

def clean_for_pdf(text):
    # Normalize common typographic unicode characters that are not in Latin-1
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    text = text.replace("\u2014", "-") # Replace em-dash with hyphen

    # Filter out any other characters that cannot be encoded in Latin-1 (standard PDF core fonts)
    cleaned = []
    for char in text:
        try:
            char.encode("latin-1")
            cleaned.append(char)
        except UnicodeEncodeError:
            continue
    return "".join(cleaned)

def compile_pdf():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    md_path = os.path.join(base_dir, "MIT_18_642_Textbook.md")
    pdf_path = os.path.join(base_dir, "MIT_18_642_Textbook.pdf")

    if not os.path.exists(md_path):
        print(f"Error: Markdown file {md_path} not found. Please compile the markdown textbook first.")
        return

    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Pre-process markdown:
    # 1. Strip out HTML anchors like <a name='...'></a> which crash the FPDF HTML parser (KeyError 'href')
    md_content = re.sub(r"<a name=.*?</a>", "", md_content)
    md_content = re.sub(r"<a name=.*?>", "", md_content)

    # 2. Simplify GitHub alerts: '> [!NOTE]' -> 'Note:'
    md_content = re.sub(r">\s*\[!NOTE\]\s*\n>\s*\*\*Summary in 1 Sentence:\*\*", "**Summary:**", md_content)
    md_content = re.sub(r">\s*\[!NOTE\]", "**Note:**", md_content)
    
    # Remove blockquote markers '>' so the text flows as normal paragraphs in PDF
    lines = md_content.split("\n")
    cleaned_lines = []
    for line in lines:
        if line.strip().startswith(">"):
            cleaned_lines.append(line.replace(">", "").strip())
        else:
            cleaned_lines.append(line)
    md_content = "\n".join(cleaned_lines)

    # 3. Clean up typographic marks and non-Latin-1 characters
    md_content = clean_for_pdf(md_content)

    # 4. Convert markdown to HTML using mistletoe
    html_content = markdown(md_content)

    # 5. Strip internal HTML links (href="#...") which fail to resolve and crash FPDF
    html_content = re.sub(r'<a href="#.*?">(.*?)</a>', r'\1', html_content)
    html_content = re.sub(r'<a href=\'#.*?\'>(.*?)</a>', r'\1', html_content)

    # 6. Convert CSS page breaks to FPDF-specific <pagebreak/> tags
    html_content = html_content.replace("<div style='page-break-after: always;'></div>", "<pagebreak/>")
    html_content = html_content.replace("<div style=\"page-break-after: always;\"></div>", "<pagebreak/>")

    # Custom FPDF class for header/footer
    class MyPDF(FPDF):
        def header(self):
            if self.page_no() > 1:
                self.set_font("helvetica", "I", 9)
                self.set_text_color(100, 100, 100)
                # Avoid deprecated 'ln' parameter by placing cell and using a separate ln call
                self.cell(0, 10, "MIT 18.642: Quantitative Finance & Mathematical Foundations", 0, 0, "R")
                self.ln(10)

        def footer(self):
            self.set_y(-15)
            self.set_font("helvetica", "I", 9)
            self.set_text_color(100, 100, 100)
            self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

    # 7. Initialize PDF
    pdf = MyPDF()
    pdf.set_margins(15, 20, 15)
    pdf.add_page()
    pdf.set_font("helvetica", size=10.5)

    # 8. Render HTML to PDF
    try:
        pdf.write_html(html_content)
    except Exception as e:
        print(f"Error during HTML writing: {e}")
        print("Attempting to write cleaned plain text instead...")
        # Fallback to writing plain text if HTML parsing has issues
        pdf.add_page()
        pdf.set_font("helvetica", size=10)
        pdf.write(5, md_content)

    # 9. Output PDF
    pdf.output(pdf_path)
    print(f"Successfully compiled PDF textbook to: {pdf_path}")

if __name__ == "__main__":
    compile_pdf()

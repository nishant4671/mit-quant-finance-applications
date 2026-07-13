import os
import re

def markdown_to_latex(md_content):
    # 1. Normalize escaped dollar signs to raw dollar signs
    md_content = md_content.replace("\\$", "$")
    
    # 2. Convert currency dollar signs to LaTeX escaped format: \$
    # Match a dollar sign followed by a digit (e.g. $100, $10,000, $1.5)
    md_content = re.sub(r"\$(\d)", r"\\$\1", md_content)
    
    # 3. Mask block math $$ ... $$
    block_math_blocks = []
    def mask_block_math(match):
        block_math_blocks.append(match.group(0))
        return f"BLOCKMATHMASK{len(block_math_blocks)-1}BLOCK"
    md_content = re.sub(r"\$\$(.*?)\$\$", mask_block_math, md_content, flags=re.DOTALL)
    
    # 4. Mask inline math $ ... $
    # Since we already converted currency $ to \$, any remaining $ signs are math mode delimiters!
    inline_math_blocks = []
    def mask_inline_math(match):
        inline_math_blocks.append(match.group(0))
        return f"INLINEMATHMASK{len(inline_math_blocks)-1}INLINE"
    md_content = re.sub(r"\$(.*?)\$", mask_inline_math, md_content)

    # 5. Mask URLs in links to prevent escaping characters in URLs
    url_blocks = []
    def mask_url(match):
        text = match.group(1)
        url = match.group(2)
        url_blocks.append(url)
        return f"\\href{{URLMASK{len(url_blocks)-1}URL}}{{{text}}}"
    md_content = re.sub(r"\[(.*?)\]\((.*?)\)", mask_url, md_content)

    # 6. Convert other markdown formatting (bold, italics)
    md_content = re.sub(r"\*\*(.*?)\*\*", r"\\textbf{\1}", md_content)
    md_content = re.sub(r"\*(.*?)\*", r"\\textit{\1}", md_content)

    # 7. State-machine parsing line by line
    lines = md_content.split("\n")
    in_list = False
    in_quote = False
    in_tcolorbox = False
    new_lines = []
    
    for line in lines:
        stripped = line.strip()
        
        # Check if we should close quote or tcolorbox if the current line does not start with '>'
        if not stripped.startswith(">"):
            if in_quote:
                new_lines.append("\\end{quote}")
                in_quote = False
            if in_tcolorbox:
                new_lines.append("\\end{tcolorbox}")
                in_tcolorbox = False
                
        # Check if we should close list if the current line does not start with list indicators
        if not (stripped.startswith("* ") or stripped.startswith("- ")):
            if in_list:
                new_lines.append("\\end{itemize}")
                in_list = False
                
        # Now process the line type
        if stripped.startswith("* ") or stripped.startswith("- "):
            if not in_list:
                new_lines.append("\\begin{itemize}")
                in_list = True
            item_text = stripped[2:]
            item_text = item_text.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("#", "\\#")
            new_lines.append(f"  \\item {item_text}")
            
        elif stripped.startswith(">"):
            # It's a quote or note box
            if "[!NOTE]" in stripped or "Summary" in stripped or "Summary in 1 Sentence:" in stripped:
                if not in_tcolorbox:
                    new_lines.append("\\begin{tcolorbox}")
                    in_tcolorbox = True
            else:
                # If we are not in tcolorbox, it's a regular quote
                if not in_tcolorbox and not in_quote:
                    new_lines.append("\\begin{quote}")
                    in_quote = True
                quote_text = stripped[1:].strip()
                quote_text = quote_text.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("#", "\\#")
                if quote_text:
                    new_lines.append(quote_text)
                    
        elif stripped.startswith("#### "):
            header_text = stripped[5:].strip().replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("#", "\\#")
            new_lines.append(f"\\subsubsection{{{header_text}}}")
        elif stripped.startswith("### "):
            header_text = stripped[4:].strip().replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("#", "\\#")
            new_lines.append(f"\\subsection{{{header_text}}}")
        elif stripped.startswith("## "):
            header_text = stripped[3:].strip().replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("#", "\\#")
            new_lines.append(f"\\section{{{header_text}}}")
        elif stripped.startswith("# "):
            continue
        else:
            # Escape ordinary text characters
            escaped_line = line.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("#", "\\#")
            new_lines.append(escaped_line)
            
    # Close any remaining open environments at the end of the file
    if in_list:
        new_lines.append("\\end{itemize}")
    if in_quote:
        new_lines.append("\\end{quote}")
    if in_tcolorbox:
        new_lines.append("\\end{tcolorbox}")

    content = "\n".join(new_lines)

    # 8. Unmask math blocks
    for i, math in enumerate(block_math_blocks):
        content = content.replace(f"BLOCKMATHMASK{i}BLOCK", math)
    for i, math in enumerate(inline_math_blocks):
        content = content.replace(f"INLINEMATHMASK{i}INLINE", math)
        
    # 9. Unmask URLs
    for i, url in enumerate(url_blocks):
        content = content.replace(f"URLMASK{i}URL", url)
        
    return content

def compile_latex_book():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    theory_dir = os.path.join(base_dir, "notes", "theory")
    output_path = os.path.join(base_dir, "MIT_18_642_Textbook.tex")

    chapters = [
        {"title": "Financial Terms, Concepts, and Bond Math", "file": "L01_Bond_Math.md"},
        {"title": "Applied Linear Algebra in Quantitative Finance", "file": "L02_Linear_Algebra.md"},
        {"title": "Quantitative Equity Investing & Portfolio Optimization", "file": "L03_Quant_Equity.md"},
        {"title": "Probability Theory & Random Variables", "file": "L04_Probability_Theory.md"},
        {"title": "Stochastic Processes I & Asset Return Modeling", "file": "L05_Stochastic_Processes_I.md"},
        {"title": "Regression Analysis & Regularization", "file": "L06_Regression_Analysis.md"},
        {"title": "Linear Rates, Swaps, and Short-Rate Models", "file": "L07_Linear_Rates.md"},
        {"title": "Time Series Analysis & Volatility Forecasting", "file": "L08_Time_Series.md"},
        {"title": "Principal Component Analysis (PCA) in Finance", "file": "L09_PCA.md"},
        {"title": "Counterparty Credit Risk & Event Trading", "file": "L10_Counterparty_Risk.md"},
        {"title": "Portfolio Management & Multi-Factor Models", "file": "L11_Portfolio_Management.md"},
        {"title": "Stochastic Processes II: Continuous Time", "file": "L14_Stochastic_Processes_II.md"},
        {"title": "Volatility Modeling & Volatility Term Structure", "file": "L19_Volatility_Modeling.md"},
        {"title": "The Black-Scholes Model & Option Pricing", "file": "L21_Black_Scholes.md"},
        {"title": "Systematic Trading Strategies", "file": "L22_Systematic_Trading.md"},
        {"title": "Machine Learning in Finance", "file": "L23_Machine_Learning.md"},
        {"title": "Stochastic Calculus & Stochastic Differential Equations", "file": "L24_Stochastic_Calculus.md"}
    ]

    latex_doc = []
    
    # 1. LaTeX Preamble (Clean Academic Black & White Style)
    latex_doc.append(r"""\documentclass[11pt,oneside]{book}
\usepackage[utf8]{inputenc}
\usepackage[margin=1.2in]{geometry}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{tcolorbox}
\usepackage{hyperref}
\usepackage{booktabs}
\usepackage{titlesec}
\usepackage{fancyhdr}

\hypersetup{
    colorlinks=true,
    linkcolor=black,
    filecolor=black,      
    urlcolor=black,
}

% Clean Black & White tcolorbox styling (Matches academic standards)
\tcbset{
    colback=gray!5,
    colframe=black,
    coltitle=black,
    fonttitle=\bfseries,
    boxrule=0.8pt,
    arc=0mm,
    title=Summary
}

\title{\textbf{MIT 18.642: Topics in Mathematics with Applications in Finance} \\ \Large Lecture Notes and Reference Manual}
\author{Compiled for Self-Study}
\date{\today}

\begin{document}

\maketitle

\tableofcontents

\newpage
""")

    # 2. Add chapters
    for i, ch in enumerate(chapters, 1):
        file_path = os.path.join(theory_dir, ch["file"])
        if not os.path.exists(file_path):
            print(f"Warning: File {file_path} not found.")
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        latex_content = markdown_to_latex(content)
        
        latex_doc.append(f"\\chapter{{{ch['title']}}}")
        latex_doc.append(latex_content)
        latex_doc.append("\n\\newpage\n")
        
    latex_doc.append(r"\end{document}")

    # 3. Write output
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(latex_doc))
        
    print(f"Successfully compiled LaTeX textbook to: {output_path}")

if __name__ == "__main__":
    compile_latex_book()

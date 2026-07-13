import os
import re

def markdown_to_latex(md_content):
    # Helper to check if a block is a math block
    # We will temporarily mask math blocks to avoid escaping characters inside them
    math_blocks = []
    
    # 1. Mask block math $$ ... $$
    def mask_block_math(match):
        math_blocks.append(match.group(0))
        return f"__BLOCKMATH_{len(math_blocks)-1}__"
    md_content = re.sub(r"\$\$(.*?)\$\$", mask_block_math, md_content, flags=re.DOTALL)
    
    # 2. Mask inline math $ ... $
    def mask_inline_math(match):
        math_blocks.append(match.group(0))
        return f"__INLINEMATH_{len(math_blocks)-1}__"
    md_content = re.sub(r"\$(.*?)\$", mask_inline_math, md_content)

    # 3. Convert markdown formatting (bold, italics, links)
    md_content = re.sub(r"\*\*(.*?)\*\*", r"\\textbf{\1}", md_content)
    md_content = re.sub(r"\*(.*?)\*", r"\\textit{\1}", md_content)
    md_content = re.sub(r"\[(.*?)\]\((.*?)\)", r"\\href{\2}{\1}", md_content)

    # 4. Handle headers, lists, and quote/note blocks line by line
    lines = md_content.split("\n")
    in_list = False
    in_quote = False
    new_lines = []
    
    for line in lines:
        stripped = line.strip()
        
        # List items
        if stripped.startswith("* ") or stripped.startswith("- "):
            if not in_list:
                new_lines.append("\\begin{itemize}")
                in_list = True
            item_text = stripped[2:]
            # Escape text inside item
            item_text = item_text.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("#", "\\#")
            new_lines.append(f"  \\item {item_text}")
            continue
        else:
            if in_list:
                new_lines.append("\\end{itemize}")
                in_list = False
        
        # Quote/Note boxes
        if stripped.startswith(">"):
            if "[!NOTE]" in stripped or "Summary" in stripped:
                if not in_quote:
                    new_lines.append("\\begin{tcolorbox}")
                    in_quote = True
                continue
            else:
                if not in_quote:
                    new_lines.append("\\begin{quote}")
                    in_quote = True
                quote_text = stripped[1:].strip()
                quote_text = quote_text.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("#", "\\#")
                new_lines.append(quote_text)
                continue
        else:
            if in_quote:
                if "tcolorbox" in new_lines[-1] or "\\begin{tcolorbox}" in new_lines:
                    new_lines.append("\\end{tcolorbox}")
                else:
                    new_lines.append("\\end{quote}")
                in_quote = False
        
        # Headers
        if stripped.startswith("#### "):
            header_text = stripped[5:].strip().replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("#", "\\#")
            new_lines.append(f"\\subsubsection{{{header_text}}}")
        elif stripped.startswith("### "):
            header_text = stripped[4:].strip().replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("#", "\\#")
            new_lines.append(f"\\subsection{{{header_text}}}")
        elif stripped.startswith("## "):
            header_text = stripped[3:].strip().replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("#", "\\#")
            new_lines.append(f"\\section{{{header_text}}}")
        elif stripped.startswith("# "):
            # Main file titles, we skip them since we add \chapter{} manually
            continue
        else:
            # Escape ordinary text characters
            escaped_line = line.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("#", "\\#")
            new_lines.append(escaped_line)

    if in_list:
        new_lines.append("\\end{itemize}")
    if in_quote:
        new_lines.append("\\end{tcolorbox}")

    content = "\n".join(new_lines)

    # 5. Unmask math blocks (so LaTeX can compile math correctly)
    for i, math in enumerate(math_blocks):
        content = content.replace(f"__BLOCKMATH_{i}__", math)
        content = content.replace(f"__INLINEMATH_{i}__", math)
        
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
    
    # 1. LaTeX Preamble
    latex_doc.append(r"""\documentclass[11pt,oneside]{book}
\usepackage[utf8]{inputenc}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{tcolorbox}
\usepackage{hyperref}
\usepackage{booktabs}
\usepackage{titlesec}
\usepackage{fancyhdr}

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,      
    urlcolor=cyan,
}

\tcbset{colback=blue!5!white,colframe=blue!75!black,title=Key Summary}

\title{\textbf{MIT 18.642: Topics in Mathematics with Applications in Finance} \\ \Large Student Companion \& Lecture Notes}
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

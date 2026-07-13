import os
import re

def compile_textbook():
    # Workspace root directory
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    theory_dir = os.path.join(base_dir, "notes", "theory")
    output_path = os.path.join(base_dir, "MIT_18_642_Textbook.md")

    # Map of all lectures to their filenames
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

    compiled_content = []
    compiled_content.append("# 📖 MIT 18.642: Quantitative Finance & Mathematical Foundations")
    compiled_content.append("## Personal Student Companion (Printable Version)")
    compiled_content.append("\n---\n")
    
    # User preference headers
    compiled_content.append("> **Format:** Applied & Practical (Intuition Focus)\n> **Code & Derivations:** Omitted from print layout (Interactive code remains in lab files)\n")
    compiled_content.append("\n---\n")
    
    compiled_content.append("## 📋 Table of Contents\n")
    for i, ch in enumerate(chapters, 1):
        clean_anchor = ch["title"].lower().replace(" ", "-").replace(",", "").replace("&", "and").replace(":", "")
        compiled_content.append(f"{i}. [Chapter {i}: {ch['title']}](#{clean_anchor})")
    compiled_content.append("\n<div style='page-break-after: always;'></div>\n")

    for i, ch in enumerate(chapters, 1):
        file_path = os.path.join(theory_dir, ch["file"])
        if not os.path.exists(file_path):
            print(f"Warning: File {file_path} not found.")
            continue
        
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Strip out the main document title (e.g. # 📓 Lecture 1: ...) or (# Applied Linear Algebra...)
        content = re.sub(r"^#\s+.*$", "", content, flags=re.MULTILINE)
        
        # Strip out code blocks (```python ... ```) just in case
        content = re.sub(r"```python.*?```", "", content, flags=re.DOTALL)
        
        # Create a clean markdown anchor
        clean_anchor = ch["title"].lower().replace(" ", "-").replace(",", "").replace("&", "and").replace(":", "")
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

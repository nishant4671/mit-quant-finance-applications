# 📍 Session State Tracker

> **DO NOT DELETE.** This file is used by the AI to resume your exact learning state across sessions.

---

## 🔍 Current State
* **Active Lecture:** Lecture 1 (Financial Terms, Concepts, and Bond Math)
* **Last Completed Lesson:** Lesson 1.4: Risk Sensitivity: Duration (Completed)
* **Current Lesson:** Lesson 1.5: Risk Sensitivity: Convexity
* **Current Task:** User is watching "Lecture 1, Part III: Bond 'Mathematics'" video.

---

## 📝 Session History & Notes
* **2026-07-03 (Session 1):** 
  * Initialized the workspace rules (`AGENTS.md`) and dashboard tracking.
  * Created theory notes `notes/theory/L01_Bond_Math.md` and lab code `notes/lab/L01_Bond_Math.ipynb` for Lesson 1.1.
  * Walked through annual compounding step-by-step to build math intuition.
  * Solved the \$10,000 today vs. \$12,500 in 5 years comparison problem.
* **2026-07-03 (Session 2):**
  * Compiled the complete set of theory notes for all of Lecture 1 (Lessons 1.1 to 1.5).
  * Implemented all companion Python code in [L01_Bond_Math.ipynb](file:///C:/Users/HP/OneDrive/Desktop/mit-quant-finance-applications/notes/lab/L01_Bond_Math.ipynb) (including continuous compounding practice solver, YTM root-finder, bootstrapping spot rates, and duration/convexity Taylor approximation comparison).
  * Marked Lecture 1 as completed on [00_Dashboard.md](file:///C:/Users/HP/OneDrive/Desktop/mit-quant-finance-applications/00_Dashboard.md).
  * Created `notes/derivations/D01_Bond_Math.md` — step-by-step mathematical derivations for all Lecture 1 formulas (continuous compounding, bond pricing, Macaulay duration, modified duration, convexity + Taylor expansion).
* **2026-07-03 (Session 3):**
  * Created [L01_Real_Data.ipynb](file:///C:/Users/HP/OneDrive/Desktop/mit-quant-finance-applications/notes/lab/L01_Real_Data.ipynb) — real-market-data lab covering: FRED yield curve fetch (with hardcoded fallback), yield curve plotting, 10Y Treasury bond pricing via interpolated curve, duration/convexity stress-testing with shock analysis, and historical yield curve comparison (2018 vs 2023 vs 2024).
  * User studied and completed Theory 1.3 (Yield Curves & Spot Rates) and signed off for the day.
* **2026-07-04 (Session 4):**
  * Resumed session. Starting micro-lesson for Lesson 1.4: Risk Sensitivity (Duration).
* **2026-07-11 (Session 5):**
  * User completed independent theory study for Lesson 1.4 (Duration) using external sources.
  * Updated `AGENTS.md` to reflect user preference: return only bare topic names for syllabus requests.
* **2026-07-12 (Session 6):**
  * Resumed session. Started micro-lesson for Lesson 1.5: Risk Sensitivity (Convexity). Presenting intuition, formula, and python code, waiting for checkpoint response.
* **2026-07-13 (Session 7):**
  * Resumed session. User requested lecture video recommendations for Lesson 1.5. Provided recommendations including MIT 18.642 Lecture 1, Part III. User is now watching the lecture.
  * User reported that the previous OCW lecture note link was broken and asked for textbook recommendations. Clarified the OCW navigation layout (reorganized by Week blocks) and recommended three comprehensive textbooks (Capiński, Ruppert, and Shreve) to act as course references.
  * User asked if the AI could compile a custom, printable book matching the MIT 18.642 curriculum. Outlined the custom book plan and detailed Table of Contents, and proposed a compiler script to merge notes into a single printable PDF-ready file.
  * User requested that the textbook style match the rigorous, academic, black-and-white print of Stanford CS229 lecture notes.
  * Rewrote all 17 chapters in a detailed, paragraph-based, formal academic style.
  * Fixed string escape sequences (e.g. `\f`, `\t` conversions to formfeed/tab) in `generate_all_chapters.py` by using raw strings.
  * Implemented a robust state-machine parser in `compile_book_latex.py` to properly handle and close environments (lists, quotes, code, math).
  * Styled the LaTeX output in a high-contrast, black-and-white academic layout (Computer Modern fonts, gray-backed summary boxes). Pushed the clean [MIT_18_642_Textbook.tex](file:///C:/Users/HP/OneDrive/Desktop/mit-quant-finance-applications/MIT_18_642_Textbook.tex) to main branch.
  * Verified the compiled textbook against the MIT 18.642 syllabus and identified two missing guest application lectures: Lecture 18 (Managing Biomedical Portfolios) and Lecture 20 (Building a Regulated Event Exchange).
  * Generated and compiled these two new chapters ([L18_Biomedical_Portfolios.md](file:///C:/Users/HP/OneDrive/Desktop/mit-quant-finance-applications/notes/theory/L18_Biomedical_Portfolios.md) and [L20_Event_Trading.md](file:///C:/Users/HP/OneDrive/Desktop/mit-quant-finance-applications/notes/theory/L20_Event_Trading.md)) in the same formal academic style. Recompiled the full 19-chapter [MIT_18_642_Textbook.tex](file:///C:/Users/HP/OneDrive/Desktop/mit-quant-finance-applications/MIT_18_642_Textbook.tex) and pushed to GitHub.
  * Implemented user request to add algorithmic pseudo-code blocks across all core chapters.
  * Updated [generate_all_chapters.py](file:///C:/Users/HP/OneDrive/Desktop/mit-quant-finance-applications/notes/library/generate_all_chapters.py) to write clean pseudo-code specifications (e.g. YTM solver, spot rate bootstrapping, Lasso coordinate descent, GARCH forecasting, Euler-Maruyama simulation).
  * Upgraded [compile_book_latex.py](file:///C:/Users/HP/OneDrive/Desktop/mit-quant-finance-applications/notes/library/compile_book_latex.py) with a code block regex masking filter to compile markdown fenced code blocks into clean LaTeX `tcolorbox` framed `verbatim` structures. Pushed updated [MIT_18_642_Textbook.tex](file:///C:/Users/HP/OneDrive/Desktop/mit-quant-finance-applications/MIT_18_642_Textbook.tex) to main branch.


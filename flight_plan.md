# ✈️ Study Flight Plan: AI-Guided Quant Finance

This document is your master blueprint for studying **MIT 18.642 (Topics in Mathematics with Applications in Finance)** using Antigravity (your AI Coding Assistant) as your primary teacher.

---

## 🎯 The Core Philosophy: "MIT-Level Self-Study"

We don't just watch and take notes. We replicate the full MIT student experience:
1. **Learn** the theory (micro-lessons).
2. **Derive** the math from scratch (proofs & derivations).
3. **Code** every formula in Python.
4. **Solve** challenging problem sets.
5. **Apply** concepts to real market data.
6. **Connect** theory to industry practice (bridge notes).
7. **Test** yourself under timed conditions (weekly quizzes).

---

## 🔄 The 7-Step Learning Loop (Per Lecture)

```
┌──────────────────────────────────────────────┐
│  1. THEORY NOTES (AI)                        │
│  Read notes/theory/L##_*.md                  │
│  Intuition-first explanations + formulas     │
└──────────────────────┬───────────────────────┘
                       ▼
┌──────────────────────────────────────────────┐
│  2. DERIVATIONS (AI + User)                  │
│  Read notes/derivations/D##_*.md             │
│  Step-by-step proofs from first principles   │
└──────────────────────┬───────────────────────┘
                       ▼
┌──────────────────────────────────────────────┐
│  3. LAB CODE (AI + User)                     │
│  Run notes/lab/L##_*.ipynb                   │
│  Clean Python implementations of the math    │
└──────────────────────┬───────────────────────┘
                       ▼
┌──────────────────────────────────────────────┐
│  4. REAL DATA LAB (User)                     │
│  Run notes/lab/L##_Real_Data.ipynb           │
│  Apply concepts to actual market data        │
└──────────────────────┬───────────────────────┘
                       ▼
┌──────────────────────────────────────────────┐
│  5. PROBLEM SET (User)                       │
│  Solve notes/problem_sets/PS##_*.md          │
│  Multi-step MIT-level problems (no peeking!) │
└──────────────────────┬───────────────────────┘
                       ▼
┌──────────────────────────────────────────────┐
│  6. BRIDGE NOTES (Read)                      │
│  Read notes/bridge/B##_*.md                  │
│  How this applies in the real world          │
└──────────────────────┬───────────────────────┘
                       ▼
┌──────────────────────────────────────────────┐
│  7. WEEKLY QUIZ (User, Timed)                │
│  Complete notes/quizzes/Quiz_##_*.md         │
│  30-min timed test — score ≥ 21/30 to pass   │
└──────────────────────────────────────────────┘
```

---

## 📁 Repository Structure

```
mit-quant-finance-applications/
├── 00_Dashboard.md            ← Live progress tracker
├── flight_plan.md             ← This file (master blueprint)
├── .agents/
│   ├── AGENTS.md              ← AI behavioral rules
│   └── session_state.md       ← AI resume-state tracker
└── notes/
    ├── theory/                ← Clean markdown explanations + formulas
    │   └── L01_Bond_Math.md
    ├── derivations/           ← Step-by-step mathematical proofs
    │   └── D01_Bond_Math.md
    ├── lab/                   ← Jupyter notebooks (Python implementations)
    │   ├── L01_Bond_Math.ipynb
    │   └── L01_Real_Data.ipynb
    ├── problem_sets/          ← MIT-level problem sets + solutions
    │   ├── PS01_Bond_Math.md
    │   └── PS01_Solutions.md
    ├── bridge/                ← Theory-to-industry connections
    │   └── B01_Bond_Math.md
    ├── quizzes/               ← Timed self-assessment quizzes
    │   ├── QUIZ_TEMPLATE.md
    │   ├── Quiz_01_Bond_Math.md
    │   └── Quiz_01_Answers.md
    └── library/               ← Reference sheets and tools
```

---

## 🛠️ The Tech Rules

1. **Ignore R/RStudio:** The OCW materials use R. We ignore it. Everything is implemented in Python using `numpy`, `pandas`, `scipy`, `matplotlib`, and Jupyter notebooks in `notes/lab/`.
2. **Problem Sets are King:** You have not learned a topic until you can solve its problem set without looking at notes.
3. **Real Data or Bust:** Every lecture should have at least one notebook using real market data, not just toy examples.
4. **Bridge Folder:** When you learn a math concept, the bridge note tells you where it's used in industry and suggests resume-building project ideas.
5. **Weekly Quizzes:** Every weekend, take the quiz for the week's lecture(s). Score ≥ 21/30 to advance.

---

## 🤖 Persistent AI Instructions

A dedicated rule file has been created at `.agents/AGENTS.md`. This ensures that every time you start a new session, your AI assistant immediately reads this plan, adopts the primary teacher role, and knows exactly how you want to learn.
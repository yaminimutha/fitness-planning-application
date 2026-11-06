# FitPlan AI — Personalized Fitness Plan Agent

## Project details
- **Domain:** Generative AI & Agentic AI Systems
- **Project title:** Personalized fitness-plan generation agent: an agentic AI system reasoning over health goals
- **Type:** Student prototype / wellness companion app
- **Current implementation:** Streamlit UI + transparent rule-based agent workflow
- **Important:** The prototype does not diagnose, prescribe treatment, or replace a doctor, dietitian, or qualified fitness professional.

## Features
1. Collects fitness goal, experience level, available days, session duration, equipment, activity preference, food preference, and sleep context.
2. Uses a simple four-stage workflow: goal analysis → constraint check → plan generation → habit guidance.
3. Generates a sample weekly activity plan.
4. Allows the plan to be downloaded as CSV.
5. Stops personalization when a user selects a health-related limitation and recommends professional guidance instead.

## Run locally
1. Install Python 3.10 or later.
2. Open a terminal in this folder.
3. Create and activate a virtual environment (recommended).
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   streamlit run app.py
   ```
6. Open the local URL printed in the terminal.

## Suggested folder structure
```text
personalized_fitness_agent/
├── app.py
├── requirements.txt
├── README.md
└── sample_fitness_data.csv
```

## Sample data
`sample_fitness_data.csv` is synthetic demonstration data only. Do not use it to make medical claims or train a real-world health model without appropriate consent, governance, and expert review.

## Current limitations
- The current agent is rule-based; it does not call an LLM or use a trained predictive model.
- Plans are general examples and are not clinically validated.
- No account system or personal health data storage is included.
- Food suggestions are broad healthy-habit ideas, not calorie or nutrient prescriptions.

## Future scope
- Add a vetted LLM behind a secure server-side API key, with output validation.
- Use synthetic/anonymized data for evaluation and document the data source.
- Add a consent screen, data deletion controls, and minimal data collection.
- Add evaluation metrics such as goal relevance, constraint compliance, readability, and safety-rule pass rate.
- Ask qualified health and fitness professionals to review the safety policy before any real-world use.

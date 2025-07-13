# 🛁 Donizo Bathroom Pricing Engine

This project implements a smart pricing engine that reads a bathroom renovation **transcript** and outputs a structured **quote in JSON** format. The quote includes a breakdown of labor, materials, estimated time, VAT, margin, total cost, and a confidence score.

---

## 💡 What It Does

Given a transcript like:

> “Client wants to renovate a small 4m² bathroom. They’ll remove the old tiles, redo the plumbing for the shower, replace the toilet, install a vanity, repaint the walls, and lay new ceramic floor tiles. Budget-conscious. Located in Marseille.”

The engine produces an output JSON such as:

```json
{
  "task": "plumbing",
  "estimated_time_hr": 4,
  "material_cost": 160,
  "labor_cost": 140,
  "vat_rate": 0.1,
  "margin_rate": 0.15,
  "total_price": 379.5
}
```

---

## 🔧 Tech Stack

- **Language:** Python 3.x  
- **Output Format:** JSON  
- **Structure:** Modular (pricing logic in separate files)  
- **Extras:** Test coverage, feedback logic, city-based pricing  

---

## 📁 Project Structure

```
bathroom-pricing-engine/
├── pricing_engine.py            # Main script
├── pricing_logic/
│   ├── material_db.py           # Material prices
│   ├── labor_calc.py            # Labor estimation logic
│   └── vat_rules.py             # VAT logic
├── data/
│   └── materials.json           # Static material prices
├── output/
│   └── sample_quote.json        # Final structured quote
├── tests/
│   └── test_logic.py            # Unit tests
└── README.md
```

---

## 🚀 How to Run

### Run the engine
```bash
python pricing_engine.py
```

Output:  
✔ `output/sample_quote.json`

### Run the unit tests
```bash
python -m unittest tests/test_logic.py
```

---

## 🧾 Logic & Assumptions

### 🔹 Parsing Strategy

- The transcript is parsed using **simple keyword detection** (e.g., "plumbing", "install vanity").
- Area (`area_m2`) and city (`Marseille` or `Paris`) are inferred from the transcript.
- Based on the keywords found, relevant tasks are added to the quote.

### 🔹 Material & Labor Pricing

- Material prices are stored in `data/materials.json`.
- Labor rate is dynamic, based on the **city**.
  - Marseille: cheaper labor
  - Paris: more expensive labor
- Each task has a time estimate in hours, based on lookup logic.

### 🔹 VAT & Margin

- VAT is task-specific:
  - Example: 10% VAT for plumbing or painting
- Margin is fixed at **15%** to reflect business markup.

### 🔹 Final Cost Calculation

Each task total is calculated as:

```
base_cost = material_cost + labor_cost  
total_with_margin = base_cost * (1 + margin)  
total_with_vat = total_with_margin * (1 + VAT)
```

### 🔹 Bonus: Feedback Logic

- If the total estimate exceeds €1500:
  - A feedback message is added suggesting cost-saving changes.
- Confidence score (default 0.9) assumes medium-high parsing reliability.

---

## 📊 Sample JSON Output

```json
{
  "quote_id": "uuid",
  "generated_at": "timestamp",
  "city": "Marseille",
  "area_m2": 4,
  "tasks": [...],
  "total_estimate": 1353.55,
  "confidence_score": 0.9,
  "feedback": {
    "too_expensive": false,
    "message": "Estimate looks budget-friendly."
  }
}
```

---

## ✅ Features Summary

- 📌 Transcript → Task parser
- 💰 Dynamic pricing by city
- 🧮 Task-level cost calculation
- 🧾 Structured JSON output
- ✅ Unit-tested logic
- 💬 Bonus: Budget feedback

---

## 👤 Author

Built with care for Donizo  
GitHub: [@sparshr-tech](https://github.com/sparshr-tech)

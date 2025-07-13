# 🛁 Donizo Bathroom Pricing Engine

This project is a smart pricing engine built to generate structured bathroom renovation quotes from a natural language transcript. Built for the **Donizo Founding Data Engineer Test Case**, it's modular, testable, and includes bonus features like feedback logic and city-based pricing.

---

## 💡 What It Does

Input a transcript like:

> “Client wants to renovate a small 4m² bathroom. They’ll remove the old tiles, redo the plumbing for the shower, replace the toilet, install a vanity, repaint the walls, and lay new ceramic floor tiles. Budget-conscious. Located in Marseille.”

The engine outputs a full structured quote in JSON, including:

- Labor and material costs per task  
- Estimated time  
- VAT and margin  
- Confidence score  
- Feedback message based on budget

---

## 📁 Project Structure



## 🔧 Tech Stack
- Python 3.x
- JSON
- Modular logic per file

## 🧾 How to Run

```bash
python pricing_engine.py

## ➡ Output will be saved to:

```bash
output/sample_quote.json

## 🧾 🧪 Run Tests

```bash
python -m unittest tests/test_logic.py


## 🔧 Assumptions & Logic
Transcript Parsing: Simple keyword matching per task

City-Based Pricing: Labor rate varies by city

Material Costs: Pulled from materials.json

Margin + VAT: 15% margin; VAT based on task type

Bonus: Feedback message if estimate > €1500

## 👤 Author
Built with care for Donizo
GitHub: @sparshr-tech
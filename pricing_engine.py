import json
import os
import uuid
import datetime

from pricing_logic.material_db import load_material_prices
from pricing_logic.labor_calc import get_labor_rate_by_city, get_estimated_time
from pricing_logic.vat_rules import get_vat_for_task

def extract_info(transcript):
    city = "Marseille" if "Marseille" in transcript else "Paris"
    area = 4  # Default as mentioned
    tasks = []

    task_keywords = {
        "tile_removal": ["remove old tiles", "tile removal"],
        "plumbing": ["redo plumbing", "plumbing"],
        "toilet_installation": ["replace the toilet", "install toilet"],
        "vanity_installation": ["install a vanity", "vanity"],
        "painting": ["repaint the walls", "painting"],
        "floor_tiling": ["ceramic floor tiles", "floor tiling"]
    }

    for key, phrases in task_keywords.items():
        if any(phrase in transcript.lower() for phrase in phrases):
            tasks.append(key)

    return city, area, tasks

def calculate_pricing(city, area, tasks, materials):
    output = {
        "quote_id": str(uuid.uuid4()),
        "generated_at": datetime.datetime.now().isoformat(),
        "city": city,
        "area_m2": area,
        "tasks": []
    }

    margin = 0.15
    confidence_score = 0.9
    labor_rate = get_labor_rate_by_city(city)

    for task in tasks:
        item = {"task": task}
        time_hours = get_estimated_time(task)
        material_cost = 0

        if task == "tile_removal":
            material_cost = 0
        elif task == "plumbing":
            material_cost = materials["plumbing"]["price_per_hour"] * time_hours
        elif task == "toilet_installation":
            material_cost = materials["toilet"]["unit_price"]
        elif task == "vanity_installation":
            material_cost = materials["vanity"]["unit_price"]
        elif task == "painting":
            material_cost = materials["paint"]["price_per_m2"] * area
        elif task == "floor_tiling":
            material_cost = materials["ceramic_tile"]["price_per_m2"] * area

        labor_cost = labor_rate * time_hours
        vat = get_vat_for_task(task)
        base_cost = material_cost + labor_cost
        total_with_margin = base_cost * (1 + margin)
        total_with_vat = total_with_margin * (1 + vat)

        item.update({
            "estimated_time_hr": time_hours,
            "material_cost": round(material_cost, 2),
            "labor_cost": round(labor_cost, 2),
            "vat_rate": vat,
            "margin_rate": margin,
            "total_price": round(total_with_vat, 2)
        })

        output["tasks"].append(item)

    total_estimate = round(sum(task["total_price"] for task in output["tasks"]), 2)
    output["total_estimate"] = total_estimate
    output["confidence_score"] = confidence_score

    #Feedback Placeholder Logic
    output["feedback"] = {
        "too_expensive": total_estimate > 1500,
        "message": (
            "Client may consider removing vanity or tiling to reduce cost."
            if total_estimate > 1500
            else "Estimate looks budget-friendly."
        )
    }

    return output

if __name__ == "__main__":
    transcript = (
        "Client wants to renovate a small 4m² bathroom. They’ll remove the old tiles, "
        "redo the plumbing for the shower, replace the toilet, install a vanity, repaint the walls, "
        "and lay new ceramic floor tiles. Budget-conscious. Located in Marseille."
    )

    city, area, tasks = extract_info(transcript)
    materials = load_material_prices()
    quote = calculate_pricing(city, area, tasks, materials)

    os.makedirs("output", exist_ok=True)
    with open("output/sample_quote.json", "w") as f:
        json.dump(quote, f, indent=4)

    print("✅ Pricing quote generated at output/sample_quote.json")

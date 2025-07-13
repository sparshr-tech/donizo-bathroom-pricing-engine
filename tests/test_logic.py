import unittest
import json
from pricing_engine import extract_info, calculate_pricing
from pricing_logic.material_db import load_material_prices

class TestLaborCalc(unittest.TestCase):

    def test_labor_rate(self):
        from pricing_logic.labor_calc import get_labor_rate_by_city
        self.assertEqual(get_labor_rate_by_city("Marseille"), 35)
        self.assertEqual(get_labor_rate_by_city("Paris"), 50)
        self.assertEqual(get_labor_rate_by_city("Unknown"), 40)

    def test_estimated_time(self):
        from pricing_logic.labor_calc import get_estimated_time
        self.assertEqual(get_estimated_time("plumbing"), 4)
        self.assertEqual(get_estimated_time("painting"), 1.5)
        self.assertEqual(get_estimated_time("unknown"), 1)

    def test_full_pipeline(self):
        transcript = (
            "Client wants to renovate a small 4m² bathroom. They’ll remove the old tiles, "
            "redo the plumbing for the shower, replace the toilet, install a vanity, repaint the walls, "
            "and lay new ceramic floor tiles. Budget-conscious. Located in Marseille."
        )
        city, area, tasks = extract_info(transcript)
        materials = load_material_prices()
        quote = calculate_pricing(city, area, tasks, materials)

        # Output to console
        print("\n📦 Generated Quote JSON:\n")
        print(json.dumps(quote, indent=4))

        # Assertions
        self.assertEqual(quote["city"], "Marseille")
        self.assertEqual(quote["area_m2"], 4)
        self.assertIn("total_estimate", quote)
        self.assertIn("confidence_score", quote)
        self.assertTrue(len(quote["tasks"]) > 0)
        self.assertIn("feedback", quote)
        self.assertIn("message", quote["feedback"])

if __name__ == '__main__':
    unittest.main()

import json

def load_material_prices(file_path='data/materials.json'):
    with open(file_path, 'r') as f:
        return json.load(f)

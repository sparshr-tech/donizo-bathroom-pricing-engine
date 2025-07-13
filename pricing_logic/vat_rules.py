VAT_RULES = {
    "default": 0.10
}

def get_vat_for_task(task):
    return VAT_RULES.get(task, VAT_RULES["default"])

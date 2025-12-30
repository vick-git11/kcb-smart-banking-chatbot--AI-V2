

BRANCHES = [
    {"name": "KCB Westlands", "city": "Nairobi", "address": "Westlands Mall"},
    {"name": "KCB CBD", "city": "Nairobi", "address": "Kenyatta Avenue"},
    {"name": "KCB Kisumu", "city": "Kisumu", "address": "Oginga Odinga Street"},
]

def get_branches(city=None):
    if city:
        return [b for b in BRANCHES if b["city"].lower() == city.lower()]
    return BRANCHES

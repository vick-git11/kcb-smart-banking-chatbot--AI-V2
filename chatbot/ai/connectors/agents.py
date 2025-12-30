AGENTS = [
    {"name": "KCB Mtaani Westlands", "location": "Westlands"},
    {"name": "KCB Mtaani Rongai", "location": "Rongai"},
    {"name": "KCB Mtaani Thika", "location": "Thika"},
]

def get_agents(area=None):
    if area:
        return [a for a in AGENTS if area.lower() in a["location"].lower()]
    return AGENTS

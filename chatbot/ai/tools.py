from .connectors.branches_live import live_branch_lookup
from .connectors.agents import get_agents
from .connectors.exchange import get_rates

def run_tool(intent, text):
    text = text.lower()

    # Live branch lookup
    if "branch" in text or "where is the nearest" in text:
        # Attempt to extract meaningful location
        loc = text.replace("where is the nearest", "").replace("branch", "").strip()
        loc = loc if loc else "Kenya"
        return live_branch_lookup(loc)

    # Live agent finder
    if "agent" in text:
        area = text.lower().replace("agent", "").strip()
        return get_agents(area)

    # Live exchange rates
    if "rate" in text or "exchange" in text:
        return get_rates()

    return None

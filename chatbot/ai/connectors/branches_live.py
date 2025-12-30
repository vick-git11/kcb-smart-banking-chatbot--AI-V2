import requests

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"

HEADERS = {
    "User-Agent": "KCB-AI-Chatbot/1.0 (contact: support@kcb.ai)"
}

def live_branch_lookup(location_text: str, limit: int = 5):
    """
    Live lookup of KCB branches using OpenStreetMap Nominatim.
    This complies with OSM API policy by sending a User-Agent.
    """

    query = f"KCB Bank branch {location_text}"

    params = {
        "q": query,
        "format": "json",
        "limit": limit
    }

    try:
        response = requests.get(
            NOMINATIM_URL,
            params=params,
            headers=HEADERS,
            timeout=8
        )
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        return {"error": str(e)}

    branches = []

    for place in data:
        branches.append({
            "name": place.get("display_name"),
            "latitude": place.get("lat"),
            "longitude": place.get("lon")
        })

    return branches

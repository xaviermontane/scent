import os
import json

def load_settings():
    if not os.path.exists(SETTINGS):
        return {}

    with open("config/settings.json", "r") as f:
        return json.load(f)

def save_settings():
    with open("config/settings.json", "w") as f:
        json.dump(SETTINGS, f, indent=4)
    
def update_setting(key, value):
    settings = load_settings()
    settings[key] = value
    save_settings(settings)

def get_setting(key):
    return load_settings().get(key, None)

SETTINGS = load_settings()
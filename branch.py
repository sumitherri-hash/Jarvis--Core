import re

def process_command(text: str):
    original = text.strip()
    command = original.lower()

    if not command:
        return {
            "success": False,
            "message": "I didn't receive a command."
        }

    if "open youtube" in command:
        return {
            "success": True,
            "intent": "open_app",
            "target": "youtube",
            "message": "Opening YouTube."
        }

    if "open google" in command:
        return {
            "success": True,
            "intent": "open_website",
            "target": "https://www.google.com",
            "message": "Opening Google."
        }

    if command.startswith("open "):
        target = re.sub(r"^open\s+", "", command)

        return {
            "success": True,
            "intent": "open",
            "target": target,
            "message": f"I'll open {target}."
        }

    return {
        "success": True,
        "intent": "unknown",
        "command": original,
        "message": f"I understood your command: {original}"
    }

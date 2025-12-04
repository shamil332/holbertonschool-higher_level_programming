#!/usr/bin/env python3
import os

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for idx, attendee in enumerate(attendees, start=1):     
        name = attendee.get("name") or "N/A"
        title = attendee.get("event_title") or "N/A"
        date = attendee.get("event_date") or "N/A"
        location = attendee.get("event_location") or "N/A"

        output_text = (
            template.replace("{name}", name)
                    .replace("{event_title}", title)
                    .replace("{event_date}", date)
                    .replace("{event_location}", location)
        )

    filename = f"output_{idx}.txt"

    try:
        with open(filename, "w") as f:
            f.write(output_text)
    except Exception as e:
        print(f"Error writing file '{filename}': {e}")
        continue

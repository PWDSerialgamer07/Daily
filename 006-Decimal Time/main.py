import re


def convert_timestamp_to_seconds(timestamp):
    # Regular expression patterns for "HH:MM:SS", "MM:SS", and "SS"
    pattern_hms = r"^\d{1,2}:\d{2}:\d{2}$"  # HH:MM:SS
    pattern_ms = r"^\d{1,2}:\d{2}$"         # MM:SS
    pattern_s = r"^\d{1,2}$"                # SS
    if not isinstance(timestamp, str):  # Ensure it's a string
        return 0  # Or handle differently, depending on your needs

    if re.match(pattern_hms, timestamp):
        # Split and convert "HH:MM:SS"
        parts = timestamp.split(":")
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
        total_seconds = hours * 3600 + minutes * 60 + seconds
        return total_seconds

    elif re.match(pattern_ms, timestamp):
        # Split and convert "MM:SS"
        parts = timestamp.split(":")
        minutes = int(parts[0])
        seconds = int(parts[1])
        total_seconds = minutes * 60 + seconds
        return total_seconds

    elif re.match(pattern_s, timestamp):
        # Convert "SS"
        seconds = int(timestamp)
        return seconds

    else:
        # If it doesn't match any format, return 0
        return 0


def convert_decimal_seconds(seconds: int) -> dict:
    seconds = seconds*100000/86400
    deci_hours = seconds//10000
    deci_minutes = (seconds - deci_hours*10000)//100
    deci_seconds = seconds - deci_hours*10000 - deci_minutes*100
    return {"hours": deci_hours, "minutes": deci_minutes, "seconds": deci_seconds}


def main():
    timestamp = input(
        "Enter a timestamp in the format HH:MM:SS, MM:SS, or SS: ")
    seconds = convert_timestamp_to_seconds(timestamp)
    print(convert_decimal_seconds(seconds))


if __name__ == "__main__":
    main()

"""Create schedule from the given text."""

import re


def create_schedule_string(input_string: str) -> str:
    """Create schedule table string from the given input string."""
    schedule_dict = {}
    pattern = r"(?<!\d)(\d{1,2})[^\d](\d{1,2})\s+([A-Za-z]+)"
    for match in re.finditer(pattern, input_string):
        hour = int(match.group(1))
        minute = int(match.group(2))
        activity = match.group(3).lower()
        if hour > 23 or minute > 59:
            continue
        time_key = f"{hour:02d}:{minute:02d}"
        schedule_dict[time_key] = activity
    sorted_items = sorted(schedule_dict.items())
    return create_table(sorted_items)


def create_table(sorted_items):
    """Create table from sorted schedule items."""
    time_width = max(
        [len("time")] + [len(get_formatted_time(t)) for t, _ in sorted_items]
    )
    entries_width = max([len("entries")] + [len(a) for _, a in sorted_items])
    table_lines = []
    header = f"| {'time':<{time_width}} | " f"{'entries':<{entries_width}} |"
    separator = "-" * len(header)
    table_lines = [separator, header, separator]
    if not sorted_items:
        table_lines.append("| No entries found |")
        table_lines.append(separator)
        return "\n".join(table_lines)
    else:
        for time_24h, activity in sorted_items:
            time_12h = get_formatted_time(time_24h)
            row = f"| {time_12h:>{time_width}} | {activity:<{entries_width}} |"
            table_lines.append(row)
    table_lines.append(separator)
    return "\n".join(table_lines)


def get_table_sizes(sorted_items):
    """Get the maximum sizes for table columns."""
    max_time_width = len("time")
    max_entries_width = len("entries")
    for time_24h, activity in sorted_items:
        time_12h = get_formatted_time(time_24h)
        max_time_width = max(max_time_width, len(time_12h))
        max_entries_width = max(max_entries_width, len(activity))
    return max_time_width, max_entries_width


def get_formatted_time(time_24h):
    """Format 24 hour time to the 12 hour time."""
    hour, minute = map(int, time_24h.split(":"))
    if hour == 0:
        hour_12 = 12
        period = "AM"
    elif hour < 12:
        hour_12 = hour
        period = "AM"
    elif hour == 12:
        hour_12 = 12
        period = "PM"
    else:
        hour_12 = hour - 12
        period = "PM"

    return f"{hour_12:02d}:{minute:02d} {period}"


if __name__ == '__main__':
    print(create_schedule_string("wat 11:00 teine tekst 12:0 jah ei 10:00 pikktekst "))

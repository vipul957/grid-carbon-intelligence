def validate_window(start, duration_hours, deadline, available_hours):
    """Check a simple duration/deadline scheduling contract."""
    if duration_hours < 1 or available_hours < 1: raise ValueError("durations must be positive")
    return 0 <= start and start+duration_hours <= available_hours and start+duration_hours <= deadline

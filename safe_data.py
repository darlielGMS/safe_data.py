MAX_INPUT_BYTES = 1024 * 1024
MAX_STRING_LENGTH = 100_000


def assert_safe_size(value):
    """Reject oversized input before further processing."""
    if not isinstance(value, str):
        raise TypeError("Expected a string")

    if len(value) > MAX_STRING_LENGTH:
        raise ValueError("Input exceeds the permitted size")

    byte_length = len(value.encode("utf-8"))

    if byte_length > MAX_INPUT_BYTES:
        raise ValueError("Input exceeds the permitted byte size")

    return value


def process_untrusted_data(input_data):
    """
    Treat external input strictly as data.
    The contents are never interpreted or executed.
    """
    assert_safe_size(input_data)

    return {
        "type": "untrusted-data",
        "value": input_data
    }


def escape_html(value):
    """Escape data before inserting it into HTML."""
    value = str(value)
    assert_safe_size(value)

    return (
        value
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )


def validate_phone_number(phone):
    """
    Validate a phone number.
    Only ASCII decimal digits are accepted.
    """
    if not isinstance(phone, str):
        raise TypeError("Phone number must be a string")

    assert_safe_size(phone)

    if not phone or not all("0" <= character <= "9" for character in phone):
        raise TypeError("Phone number must contain digits only")

    return phone


def process_phone_number(phone):
    """Handle a phone number strictly as data."""
    digits = validate_phone_number(phone)

    return {
        "type": "phone-number",
        "digits": digits
    }


if __name__ == "__main__":
    external_input = "This came from an external source."

    data = process_untrusted_data(external_input)
    phone = process_phone_number("02079460000")

    print(data)
    print(phone)
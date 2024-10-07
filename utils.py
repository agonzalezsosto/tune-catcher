import urllib.parse

def convert_to_url_safe_text(input_string: str) -> str:
    formatted_string = input_string.replace('-', ' ')
    url_safe_string = urllib.parse.quote(formatted_string)
    return url_safe_string

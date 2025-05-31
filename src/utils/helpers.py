import re
from urllib.parse import quote


def slugify(text):
    # Keep Unicode letters, numbers, spaces, and hyphens
    text = re.sub(r'[^\w\s-]', '', text.strip())
    # Replace spaces and multiple hyphens with single hyphens
    text = re.sub(r'[-\s]+', '-', text)
    # Remove leading/trailing hyphens
    text = text.strip('-')
    return text.lower()


def safe_filename(filename):
    try:
        filename.encode('ascii')
        return f'attachment; filename="{filename}"'
    except UnicodeEncodeError:
        # Use RFC 2231 encoding for Unicode filenames
        encoded_filename = quote(filename.encode('utf-8'))
        return f"attachment; filename*=UTF-8''{encoded_filename}"


def get_content_type(file_extension):
    content_type_map = {
        'mp4': 'video/mp4',
        'webm': 'video/webm',
        'mkv': 'video/x-matroska',
        'avi': 'video/x-msvideo',
        'mov': 'video/quicktime',
    }
    return content_type_map.get(file_extension, 'application/octet-stream')

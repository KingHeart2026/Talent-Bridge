MAX_FILE_SIZE = 2 * 1024 * 1024

def validate_cv(file_bytes: bytes):

    if len(file_bytes) > MAX_FILE_SIZE:
        raise ValueError(
            "CV cannot exceed 2 MB"
        )

    if not file_bytes.startswith(b"%PDF-"):
        raise ValueError(
            "Only valid PDF files are accepted"
        )

    return True
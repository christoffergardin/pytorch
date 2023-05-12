def pluralize(count: int, singular_word: str, plural_word: str = "") -> str:
    if count == 1:
        return f"{count} {singular_word}"

    if not plural_word:
        plural_word = f"{singular_word}s"

    return f"{count} {plural_word}"


def to_time_str(seconds: float) -> str:
    if seconds < 0.00001:
        return "0s"
    elif seconds < 60:
        return f"{seconds:.2f}s"
    elif seconds < 3600:
        return f"{seconds / 60:.2f}m"
    else:
        return f"{seconds / 3600:.2f}h"

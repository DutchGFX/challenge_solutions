import pandas as pd
import re


def fmt(s: str) -> str:
    """
    Uses regular expressions to re-format a string by:
    - Converting the first letter of each word to uppercase and the
      remaining letters to lowercase
    - For words connected with a hyphen -, both parts should be capitalized

    Parameters
    ----------
    s : str
        input string

    Returns
    -------
    z : str
        reformatted string
    """
    fmt_word = lambda w: w[0:2].upper() + w[2:]

    # prepend " " for regex
    s = " " + s.lower()

    # word prefixed by space or -
    s = re.sub(r"[\s-]([a-z]+)", lambda m: fmt_word(m.group(0)), s)
    return s[1:]  # remove leading space


def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    """
    Reformats strings in the column of a DataFrame according to
    the requirements in the problem statement
    """
    user_content["converted_text"] = user_content["content_text"].apply(fmt)
    user_content.rename(columns={"content_text": "original_text"}, inplace=True)
    return user_content

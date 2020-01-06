import re
from typing import List, Tuple


# Question number 1:
def email_splitter(text: str) -> List[Tuple[str, str, str]]:
    pattern = re.compile(r'([\w+(\._)?]+)@([a-zA-Z]+)\.([a-zA-Z]+)')
    return pattern.findall(text)


# Question number 2
def find_words_with_first_letter(letter: str, text: str) -> List[str]:
    pattern = r"\b" + letter + r"\w*"
    return re.findall(pattern, text, re.I)


# Question number 3
def get_html_text(html: str) -> str:
    pattern = re.compile(r"<[^>]+>")
    return pattern.sub("", html)

import re

def RemoveLinks(text: list):
    result = re.sub(r"http\S+", "", text)
    return result
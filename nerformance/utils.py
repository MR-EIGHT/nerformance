from difflib import SequenceMatcher

def levenshtein_similarity(str1, str2):
    return SequenceMatcher(None, str1, str2).ratio()
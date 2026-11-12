"""Translittération approximative français -> phonèmes de l'Alde (p b f v m t d n k g l r s h y w ; a e i o u)."""
import re, unicodedata
def strip(w):
    return "".join(c for c in unicodedata.normalize("NFD", w) if unicodedata.category(c) != "Mn")
def alde(word):
    w = strip(word.lower())
    if len(w) > 3: w = re.sub(r"[stdxz]$", "", w)
    w = re.sub(r"c(?=[eiy])", "s", w); w = re.sub(r"g(?=[eiy])", "j", w)
    if len(w) > 3: w = re.sub(r"e$", "", w)
    rules = [("eau", "o"), ("au", "o"), ("ou", "u"), ("oi", "wa"), ("ai", "e"), ("ei", "e"), ("eu", "e"), ("oe", "e"),
             ("ill", "y"), ("ph", "f"), ("ch", "s"), ("qu", "k"), ("gu", "g"), ("gn", "ny"), ("th", "t"),
             ("x", "ks"), ("z", "s"), ("j$", "g"), ("j", "y"), ("c(?=[ei])", "s"), ("c", "k"), ("g(?=[ei])", "y"), ("h", ""),
             ("y(?=[^aeiou]|$)", "i"), ("(an|am|en|em)(?=[^aeiou]|$)", "an"), ("(on|om)(?=[^aeiou]|$)", "on"), ("(in|im)(?=[^aeiou]|$)", "en"),
             (r"(.)\1", r"\1")]
    for a, b in rules:
        w = re.sub(a, b, w)
    w = re.sub(r"(an)+", "an", w)
    out = []
    for ch in w:
        if ch in "aeiou": out.append(ch)
        elif ch in "pbfvmtdnkglrsyw": out.append(ch)
    return " ".join(out) or "a"

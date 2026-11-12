import math

PLACES = [("lab", "labiale"), ("den", "dentale"), ("vel", "vélaire")]
MODES = [("sou", "sourde"), ("son", "sonore"), ("fs", "fricative sourde"), ("fz", "fricative sonore"), ("nas", "nasale")]
GRID = {  # (place, mode) -> (latin, API)
 ("lab", "sou"): ("p", "p"), ("lab", "son"): ("b", "b"), ("lab", "fs"): ("f", "f"), ("lab", "fz"): ("v", "v"), ("lab", "nas"): ("m", "m"),
 ("den", "sou"): ("t", "t"), ("den", "son"): ("d", "d"), ("den", "fs"): ("th", "θ"), ("den", "fz"): ("dh", "ð"), ("den", "nas"): ("n", "n"),
 ("vel", "sou"): ("k", "k"), ("vel", "son"): ("g", "g"), ("vel", "fs"): ("kh", "x"), ("vel", "fz"): ("gh", "ɣ"), ("vel", "nas"): ("ng", "ŋ"),
}
OTHERS = [("l", "l"), ("r", "r"), ("s", "s"), ("h", "h"), ("y", "j"), ("w", "w")]
VOWELS = [("a", "a"), ("e", "e"), ("i", "i"), ("o", "o"), ("u", "u")]

def st(d): return f'<path d="{d}" class="s"/>'
def dot(x, y, r=2.6): return f'<circle cx="{x}" cy="{y}" r="{r}" class="f"/>'

# ---------- Alphabet 1 : Tige et marque (abugida, deux mains) ----------
A1_MARK = {
 "grav": {"lab": "M8,-24 L22,-16 L8,-8", "den": "M8,-24 L24,-24 L24,-12", "vel": "M8,-12 L24,-28"},
 "ink":  {"lab": "M8,-24 C26,-24 26,-8 8,-8", "den": "M8,-24 C20,-30 28,-24 24,-12", "vel": "M8,-12 C16,-14 20,-22 24,-30"},
}
A1_STEM = {"sou": "M8,-24 L8,0", "son": "M8,-24 L8,14", "fs": "M8,-44 L8,0", "fz": "M8,-44 L8,14", "nas": "M8,-24 L8,-8"}
A1_OTHER = {
 "grav": {"l": "M8,-44 L8,0 L20,-6", "r": "M8,0 L8,-24 L20,-30", "s": "M22,-24 L8,-16 L22,-8 L8,0",
          "h": "M8,-24 L8,0 M8,-24 L0,-18", "y": "M8,-24 L8,0", "w": "M2,-24 L2,0 L14,0 L14,-24"},
 "ink":  {"l": "M8,-44 L8,-6 C8,2 18,2 20,-6", "r": "M8,0 L8,-24 C8,-32 20,-32 20,-26", "s": "M22,-24 C10,-27 6,-17 14,-12 C22,-7 20,0 6,0",
          "h": "M8,-24 L8,0 M8,-24 C3,-28 -1,-24 0,-18", "y": "M8,-24 L8,0", "w": "M2,-24 L2,-8 C2,2 14,2 14,-8 L14,-24"},
}
A1_VOW = {
 "grav": {"a": dot(13, -54), "e": st("M9,-50 L18,-59"), "i": dot(9, -54) + dot(18, -54), "o": st("M8,-50 L13,-58 L19,-50"), "u": st("M8,-58 L13,-50 L19,-58")},
 "ink":  {"a": dot(13, -54), "e": st("M9,-50 Q13,-54 18,-60"), "i": dot(9, -54) + dot(18, -54), "o": st("M8,-50 Q13,-62 19,-50"), "u": st("M8,-58 Q13,-46 19,-58")},
}
A1_CARRIER = "M8,-16 L8,0"
A1_LONG = st("M2,22 L22,22")

def a1_cons(hand, place, mode):
    s = st(A1_STEM[mode]) + st(A1_MARK[hand][place])
    if mode == "nas": s += dot(8, 0)
    return s

def a1_letter(hand, key):
    """key : 'p','b',... ou voyelle seule"""
    for (pl, mo), (lat, _) in GRID.items():
        if lat == key: return a1_cons(hand, pl, mo)
    if key in A1_OTHER[hand]:
        return st(A1_OTHER[hand][key]) + (dot(16, -13) if key == "y" else "")
    if key in A1_VOW[hand]: return st(A1_CARRIER) + vow1(hand, key, None)
    raise KeyError(key)

def a1_top(cons):
    if cons is None: return "carrier"
    if cons == "l": return "asc"
    for (pl, mo), (lat, _) in GRID.items():
        if lat == cons and mo in ("fs", "fz"): return "asc"
    return "x"

def vow1(hand, v, cons):
    dy = {"carrier": 28, "x": 20, "asc": 0}[a1_top(cons)]
    return f'<g transform="translate(0,{dy})">{A1_VOW[hand][v]}</g>'

def a1_syll(hand, cons, vow=None, long=False):
    s = a1_letter(hand, cons) if cons else st(A1_CARRIER)
    if vow: s += vow1(hand, vow, cons)
    if long: s += A1_LONG
    return s

# ---------- Alphabet 2 : Branches (alphabet gravé) ----------
X2 = 14
def br(y, side, d=1, L=10):
    return f"M{X2},{y} L{X2 + side * L},{y + d * L}"
A2_MODE = {"sou": [(-40, 1)], "son": [(-40, 1), (-30, 1)], "fs": [(-24, 1)], "fz": [(-24, 1), (-14, 1)], "nas": [(0, -1)]}
A2_SIDES = {"lab": [-1], "den": [1], "vel": [-1, 1]}
def a2_cons(place, mode):
    d = f"M{X2},-40 L{X2},0 "
    for y, dr in A2_MODE[mode]:
        for side in A2_SIDES[place]:
            d += br(y, side, dr) + " "
    return st(d)
A2_OTHER = {"l": "M14,-40 L14,0 M6,-26 L22,-14", "r": "M14,-40 L14,0 M14,-40 L24,-31 L14,-22", "s": "M6,-40 L22,-28 L6,-14 L22,0",
            "h": "M14,-20 L14,0 M14,-20 L6,-12", "y": "M14,-28 L14,0 M14,-28 L6,-40 M14,-28 L22,-40", "w": "M14,-40 L14,-12 M14,-12 L6,0 M14,-12 L22,0"}
A2_VOW = {"a": "M6,-6 L14,-30 L22,-6", "e": "M22,-30 L8,-18 L22,-6", "i": "M10,-30 L13,-6 M17,-30 L20,-6",
          "o": "M6,-30 L14,-6 L22,-30", "u": "M8,-30 L22,-18 L8,-6"}
def a2_letter(key, long=False):
    for (pl, mo), (lat, _) in GRID.items():
        if lat == key: return a2_cons(pl, mo)
    if key in A2_OTHER: return st(A2_OTHER[key])
    s = st(A2_VOW[key])
    if long: s += dot(14, 7)
    return s

# ---------- Alphabet 3 : Encart (écriture entre deux parois) ----------
def a3_walls(w=24):
    return f'<path d="M0,-30 L{w},-30 M0,0 L{w},0" class="wall"/>'
def a3_cons(place, mode):
    # labiale : pend de la paroi extérieure ; dentale : monte de l'intérieure ; vélaire : traverse
    if place == "lab": y1, y2 = -30, -14
    elif place == "den": y1, y2 = 0, -16
    else: y1, y2 = -30, 0
    def tick(x, slant=0):
        return f"M{x},{y1} L{x + slant},{y2}"
    if mode == "sou": d = tick(12)
    elif mode == "son": d = tick(9) + " " + tick(15)
    elif mode == "fs": d = tick(9, 7)
    elif mode == "fz": d = tick(6, 6) + " " + tick(12, 6)
    else: d = tick(12)
    s = st(d)
    if mode == "nas":
        if place == "vel": s += dot(18, -15)
        else: s += dot(12, y2 + (5 if place == "lab" else -5))
    return s
A3_OTHER = {"l": st("M7,-30 C7,-17 17,-17 17,-30"), "r": st("M7,0 C7,-13 17,-13 17,0"), "s": st("M17,-30 C4,-27 20,-3 7,0"),
            "h": dot(12, -15), "y": st("M7,-30 C7,-19 17,-19 17,-30") + dot(12, -9), "w": st("M7,0 C7,-11 17,-11 17,0") + dot(12, -21)}
A3_VOW = {"a": "M7,-15 L17,-15", "e": "M7,-19 L17,-19 M7,-11 L17,-11", "i": "M12,-23 L12,-7", "o": "M7,-9 L12,-21 L17,-9", "u": "M7,-21 L12,-9 L17,-21"}
def a3_letter(key, long=False):
    for (pl, mo), (lat, _) in GRID.items():
        if lat == key: return a3_cons(pl, mo)
    if key in A3_OTHER: return A3_OTHER[key]
    s = st(A3_VOW[key])
    if long: s += dot(12, -30, 2.4)
    return s

# ======== Version 2 de la proposition 1 : main naine capitale, main elfique cursive ========
def tick(x, y1, y2): return f"M{x},{y1} L{x},{y2}"

# --- Main naine : capitale, compacte, hauteur unique de 40, traits au lieu des points
DW_MARK = {"lab": lambda y: f"M8,{y} L18,{y+8} L8,{y+16}",
           "den": lambda y: f"M8,{y} L18,{y} L18,{y+11}",
           "vel": lambda y: f"M8,{y+14} L18,{y}"}
def dw_cons(place, mode):
    y = -24 if mode in ("fs", "fz") else -40          # la marque descend : la hampe « monte » au-dessus d'elle
    d = DW_MARK[place](y) + " "
    if mode == "nas":
        d += "M8,-40 L8,-24 " + tick(8, -16, -6)      # tige courte + trait au lieu du point
    else:
        d += "M8,-40 L8,0 "
    if mode in ("son", "fz"):
        d += "M3,0 L13,0"                             # l'ergot de pied remplace la hampe descendante
    return st(d)
DW_OTHER = {"l": "M8,-40 L8,0 L16,-6", "r": "M8,0 L8,-40 L17,-33", "s": "M16,-40 L4,-28 L16,-14 L4,0",
            "h": "M8,-40 L8,0 M8,-40 L1,-32", "y": "M8,-40 L8,0 M15,-26 L15,-15", "w": "M2,-40 L2,0 L14,0 L14,-40"}
DW_VOW = {"a": tick(10, -55, -47), "e": "M6,-47 L14,-55", "i": tick(7, -55, -47) + " " + tick(13, -55, -47),
          "o": "M5,-47 L10,-55 L15,-47", "u": "M5,-55 L10,-47 L15,-55"}
DW_CARRIER = "M8,-40 L8,0"
def dw_letter(key):
    for (pl, mo), (lat, _) in GRID.items():
        if lat == key: return dw_cons(pl, mo)
    if key in DW_OTHER: return st(DW_OTHER[key])
    if key in DW_VOW: return st(DW_CARRIER) + st(DW_VOW[key])
    raise KeyError(key)
def dw_syll(cons, vow=None):
    s = dw_letter(cons) if cons else st(DW_CARRIER)
    if vow: s += st(DW_VOW[vow])
    return s

# --- Main elfique : cursive liée, inclinée, boucles aux hampes ; les points restent des points
ENTRY = "M-4,0 C1,-6 5,-16 8,-24"
EXIT = "L8,-4 C8,0 12,1 20,0"
EL_STEM = {
 "sou": ENTRY + " " + EXIT,
 "son": ENTRY + " L8,10 C8,20 -1,19 2,12 C5,5 13,1 20,0",
 "fs":  "M-4,0 C2,-10 3,-40 10,-44 C14,-46 12,-39 8,-36 " + EXIT,
 "fz":  "M-4,0 C2,-10 3,-40 10,-44 C14,-46 12,-39 8,-36 L8,10 C8,20 -1,19 2,12 C5,5 13,1 20,0",
 "nas": ENTRY + " L8,-10 C8,-4 14,-2 20,0",
}
EL_MARK = {"lab": "M8,-24 C25,-26 24,-8 8,-10", "den": "M8,-24 C18,-33 29,-25 22,-12", "vel": "M8,-12 C15,-14 20,-23 27,-31"}
EL_TOP = {"sou": -24, "son": -24, "fs": -44, "fz": -44, "nas": -24}
def el_cons(place, mode):
    s = st(EL_STEM[mode]) + st(EL_MARK[place])
    if mode == "nas": s += dot(14, 6)
    return s
EL_OTHER = {
 "l": "M-4,0 C2,-10 3,-40 10,-44 C14,-46 12,-39 8,-36 L8,-6 C8,2 16,3 20,0",
 "r": ENTRY + " " + EXIT + " M8,-24 C9,-32 19,-33 20,-27",
 "s": "M-4,0 C4,-4 22,-30 14,-26 C4,-22 22,-10 12,-3 C8,0 14,1 20,0",
 "h": ENTRY + " " + EXIT + " M8,-24 C3,-29 -1,-26 0,-19",
 "y": ENTRY + " " + EXIT,
 "w": "M-4,0 C0,-8 2,-20 3,-24 C3,-12 4,-2 9,-2 C14,-2 15,-12 15,-24 C15,-12 16,-1 20,0",
}
EL_VOW = {"a": dot(13, -54), "e": st("M9,-50 Q13,-54 18,-60"), "i": dot(9, -54) + dot(18, -54),
          "o": st("M8,-50 Q13,-62 19,-50"), "u": st("M8,-58 Q13,-46 19,-58")}
EL_CARRIER = "M-4,0 C2,-4 6,-10 8,-14 L8,-4 C8,0 12,1 20,0"
def el_vow(v, top):
    dy = {-14: 28, -24: 20, -44: 0}[top]
    return f'<g transform="translate(0,{dy})">{EL_VOW[v]}</g>'
def el_letter(key):
    for (pl, mo), (lat, _) in GRID.items():
        if lat == key: return el_cons(pl, mo)
    if key in EL_OTHER: return st(EL_OTHER[key]) + (dot(16, -13) if key == "y" else "")
    if key in EL_VOW: return st(EL_CARRIER) + el_vow(key, -14)
    raise KeyError(key)
def el_top(cons):
    if cons is None: return -14
    if cons == "l": return -44
    for (pl, mo), (lat, _) in GRID.items():
        if lat == cons: return EL_TOP[mo]
    return -24
def el_syll(cons, vow=None):
    s = el_letter(cons) if cons else st(EL_CARRIER)
    if vow: s += el_vow(vow, el_top(cons))
    return s
SLANT = "skewX(-14)"

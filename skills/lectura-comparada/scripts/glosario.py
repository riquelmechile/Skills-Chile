#!/usr/bin/env python3
"""Equivalente español de cada término chino que sale al usuario."""

STEM_ES = {
    "甲": "Jia, Madera yang (tronco)",
    "乙": "Yi, Madera yin (enredadera)",
    "丙": "Bing, Fuego yang (sol)",
    "丁": "Ding, Fuego yin (lámpara)",
    "戊": "Wu, Tierra yang (monte)",
    "己": "Ji, Tierra yin (huerta)",
    "庚": "Geng, Metal yang (hacha)",
    "辛": "Xin, Metal yin (joya)",
    "壬": "Ren, Agua yang (río)",
    "癸": "Gui, Agua yin (lluvia)",
}

BRANCH_ES = {
    "子": "Zi, Rata, Agua",
    "丑": "Chou, Buey, Tierra",
    "寅": "Yin, Tigre, Madera",
    "卯": "Mao, Conejo, Madera",
    "辰": "Chen, Dragón, Tierra",
    "巳": "Si, Serpiente, Fuego",
    "午": "Wu, Caballo, Fuego",
    "未": "Wei, Cabra, Tierra",
    "申": "Shen, Mono, Metal",
    "酉": "You, Gallo, Metal",
    "戌": "Xu, Perro, Tierra",
    "亥": "Hai, Cerdo, Agua",
}

GOD_ES = {
    "日主": "Amo del Día",
    "比肩": "Comparación (compañero, mismo elemento y polaridad)",
    "劫财": "Robo de riqueza (competencia)",
    "食神": "Espíritu de alimento (talento fluido)",
    "伤官": "Oficial herido (voz que rompe el molde)",
    "偏财": "Riqueza indirecta",
    "正财": "Riqueza directa",
    "七杀": "Siete asesinatos (presión, filo)",
    "正官": "Oficial directo (norma, cargo)",
    "偏印": "Sello indirecto (atajo, esquema)",
    "正印": "Sello directo (respaldo, estudio)",
}

PATRON_ES = {
    "肝气郁结": "qi de hígado trabado (pecho cerrado, ira que no sale)",
    "胆火上炎": "fuego de vesícula que sube (sienes, amargor de boca)",
    "头痛目眩": "dolor de cabeza y vértigo",
    "肝血不足": "sangre de hígado insuficiente (ojo seco, uña débil)",
    "肝风内动": "viento de hígado interno (espasmo, temblor)",
    "抑郁不舒": "ánimo bajo que no se abre",
    "心火亢盛": "fuego de corazón excesivo",
    "小肠湿热": "humedad-calor de intestino delgado",
    "失眠烦躁": "insomnio e irritación",
    "心阴虚": "yin de corazón vacío (calor fino, insomnio)",
    "心神不宁": "shen inquieto (no aterriza)",
    "血虚失眠": "insomnio de sangre vacía",
    "胃热": "calor de estómago",
    "胃寒": "frío de estómago",
    "食积": "comida estancada",
    "脾虚湿困": "bazo vacío atrapado en humedad",
    "痰湿": "flema-humedad",
    "中气下陷": "qi central que se hunde (pesadez, prolapso de ritmo)",
    "大肠燥结": "intestino grueso seco y trabado",
    "肺热": "calor de pulmón",
    "皮肤干燥": "piel seca",
    "肺阴虚": "yin de pulmón vacío",
    "鼻鼽": "rinitis",
    "金寒水冷": "metal frío y agua helada",
    "肾阳虚": "yang de riñón vacío (frío de lumbar)",
    "水湿泛滥": "agua-humedad que se desborda",
    "膀胱气化不利": "vejiga que no vaporiza (orina trabada o frecuente)",
    "肾阴虚": "yin de riñón vacío",
    "精亏": "jing menguado (reserva gastada)",
    "虚火上炎": "fuego vacío que sube (calor fantasma)",
}

HERBA_ES = {
    "薄荷": "menta",
    "菊花": "crisantemo",
    "柴胡": "bupleurum (chaihu)",
    "决明子": "semilla de casia",
    "夏枯草": "prunella",
    "当归": "angélica china (danggui)",
    "白芍": "peonía blanca",
    "枸杞": "goji",
    "酸枣仁": "semilla de azufaifo silvestre",
    "玫瑰花": "rosa",
    "莲子": "semilla de loto",
    "竹叶": "hoja de bambú",
    "麦冬": "ophiopogon (maidong)",
    "丹参": "salvia china (danshen)",
    "栀子": "gardenia",
    "百合": "lirio (bulbo)",
    "龙眼肉": "pulpa de longan",
    "生地": "rehmannia cruda",
    "阿胶": "gelatina de asno (ejiao)",
    "生姜": "jengibre fresco",
    "陈皮": "cáscara de mandarina añeja",
    "砂仁": "amomum (sharen)",
    "半夏": "pinellia",
    "黄连": "coptis",
    "茯苓": "poria (hongo fu ling)",
    "白术": "atractylodes blanco",
    "山药": "ñame chino",
    "芡实": "semilla de euryale",
    "薏苡仁": "lágrima de Job (coix)",
    "杏仁": "almendra de albaricoque",
    "枇杷叶": "hoja de níspero",
    "玄参": "scrophularia",
    "火麻仁": "semilla de cáñamo",
    "沙参": "adenophora (shashen)",
    "玉竹": "sello de Salomón (yuzhu)",
    "桑叶": "hoja de morera",
    "桔梗": "platycodon (campanilla)",
    "肉桂": "canela cassia",
    "杜仲": "eucommia (duzhong)",
    "菟丝子": "semilla de cuscuta",
    "补骨脂": "psoralea",
    "艾叶": "artemisa (aiye)",
    "熟地": "rehmannia cocida",
    "女贞子": "semilla de ligustro",
    "墨旱莲": "eclipta",
    "龟板": "plastrón de tortuga (nombre de tratado; no se indica uso)",
    "红枣": "azufaifo",
    "银耳": "hongo blanco",
}

LIBRO_ES = {
    "穷通宝鉴": "Espejo precioso que agota lo oculto (tabla de ajuste climático)",
    "三命通会": "Compendio de las tres vidas (capítulo de enfermedades)",
    "食疗": "dietoterapia",
    "黄帝内经": "Clásico Interno del Emperador Amarillo",
    "调候": "ajuste climático del gráfico",
    "用神": "dios útil (lo que el mes pide)",
    "用神": "dios útil",
    "日主": "Amo del Día",
    "立春": "Inicio de primavera solar (~4 feb)",
    "气色": "color y brillo",
    "明堂": "patio central de la palma",
    "先天": "lo dado al nacer",
    "後天": "lo cultivado",
    "大运": "Grandes Ciclos",
    "互卦": "hexagrama nuclear",
    "之卦": "hexagrama resultante",
}

STEM_PINYIN = {
    "甲": "Jia", "乙": "Yi", "丙": "Bing", "丁": "Ding", "戊": "Wu",
    "己": "Ji", "庚": "Geng", "辛": "Xin", "壬": "Ren", "癸": "Gui",
}


def t(zh: str) -> str:
    """'中文 (español)'. Si no hay entrada, deja el original."""
    if not zh:
        return zh
    if zh in STEM_ES:
        return f"{zh} ({STEM_ES[zh]})"
    if zh in BRANCH_ES:
        return f"{zh} ({BRANCH_ES[zh]})"
    if zh in GOD_ES:
        return f"{zh} ({GOD_ES[zh]})"
    if zh in PATRON_ES:
        return f"{zh} ({PATRON_ES[zh]})"
    if zh in HERBA_ES:
        return f"{zh} ({HERBA_ES[zh]})"
    if zh in LIBRO_ES:
        return f"{zh} ({LIBRO_ES[zh]})"
    return zh


def stems(xs) -> str:
    return ", ".join(t(x) for x in xs)


def patrons(xs) -> str:
    return "; ".join(t(x) for x in xs)


def herbs(xs) -> str:
    return ", ".join(t(x) for x in xs)


def mix(text: str) -> str:
    """Sustituye términos chinos conocidos dentro de una frase mixta."""
    if not text:
        return text
    out = text
    bags = (HERBA_ES, PATRON_ES, LIBRO_ES, GOD_ES, STEM_ES, BRANCH_ES)
    # Largos primero para no partir compuestos
    keys = sorted({k for bag in bags for k in bag}, key=len, reverse=True)
    for k in keys:
        if k in out:
            out = out.replace(k, t(k))
    return out


def ganzhi(s: str) -> str:
    """'庚午' → '庚午 (Geng-Wu, Metal yang / Caballo Fuego)'."""
    if not s or len(s) < 2:
        return s
    a, b = s[0], s[1]
    return f"{s} ({STEM_ES.get(a, a)} / {BRANCH_ES.get(b, b)})"

# -*- coding: utf-8 -*-
from fpdf import FPDF

# Paleta de colores (estilo Omega Ruby)
RED       = (180, 30, 30)
DARK_RED  = (120, 20, 20)
LIGHT_RED = (250, 228, 228)
GREY_BG   = (242, 242, 242)
DARK      = (40, 40, 40)
WHITE     = (255, 255, 255)
LINE      = (210, 210, 210)


class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Randomlocke - Pokemon Omega Ruby   |   Pagina {self.page_no()}",
                  align="C")


def section_title(pdf, text):
    pdf.ln(3)
    pdf.set_fill_color(*RED)
    pdf.set_text_color(*WHITE)
    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 9, "  " + text, new_x="LMARGIN", new_y="NEXT", fill=True)
    pdf.ln(2)


def rule(pdf, num, title, body):
    pdf.set_text_color(*DARK)
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(*DARK_RED)
    pdf.cell(8, 6, f"{num}.", new_x="RIGHT", new_y="TOP")
    pdf.set_text_color(*DARK)
    pdf.set_font("Helvetica", "B", 10.5)
    w_title = pdf.get_string_width(title + " ")
    pdf.cell(w_title, 6, title, new_x="RIGHT", new_y="TOP")
    pdf.set_font("Helvetica", "", 10.5)
    pdf.set_x(pdf.l_margin + 8)
    if title:
        pdf.set_xy(pdf.l_margin + 8 + w_title, pdf.get_y())
    pdf.multi_cell(0, 6, body, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1)


pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=True, margin=18)
pdf.set_margins(18, 16, 18)
pdf.add_page()

# ---------- TITULO ----------
pdf.set_fill_color(*DARK_RED)
pdf.rect(0, 0, 210, 30, "F")
pdf.set_xy(0, 8)
pdf.set_text_color(*WHITE)
pdf.set_font("Helvetica", "B", 22)
pdf.cell(210, 9, "RANDOMLOCKE", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "B", 13)
pdf.set_x(0)
pdf.cell(210, 7, "Pokemon Omega Ruby  -  Reglamento", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_text_color(*DARK)
pdf.ln(12)

# ---------- REGLAS DE CAPTURA ----------
section_title(pdf, "REGLAS DE CAPTURA")
rule(pdf, 1, "Primer encuentro:", "solo puedes capturar el PRIMER Pokemon de cada ruta o zona. Si huye o cae K.O., pierdes la captura de esa zona.")
rule(pdf, 2, "Sin reintento:", "si el primer encuentro se debilita, no hay segunda oportunidad en esa zona.")
rule(pdf, 3, "Clausula de duplicados:", "si sale una especie (o su linea evolutiva) que ya posees, repites el encuentro hasta dar con una nueva. (Opcional, recomendado.)")
rule(pdf, 4, "Clausula shiny:", "si aparece un shiny, puedes capturarlo aunque no sea tu primer encuentro.")

# ---------- REGLAS DE MUERTE ----------
section_title(pdf, "REGLAS DE MUERTE")
rule(pdf, 5, "Muerte permanente:", "un Pokemon debilitado se considera muerto. Va al PC (caja 'cementerio') de forma permanente o se libera.")
rule(pdf, 6, "Apodo obligatorio:", "pon mote a todos tus Pokemon. Mas apego, mas dolor.")

# ---------- REGLAS DE COMBATE ----------
section_title(pdf, "REGLAS DE COMBATE")
rule(pdf, 7, "Modo Fijo (Set):", "activa el estilo de combate FIJO en Opciones (sin cambio gratis al debilitar a un rival).")
rule(pdf, 8, "Sin objetos en combate:", "nada de Pociones ni Revivir desde la mochila durante la pelea. Curaciones solo en el Centro Pokemon.")
rule(pdf, 9, "Clausula de objetos (opcional):", "evita abusar de objetos de un solo uso si quieres mas reto.")

pdf.add_page()

# ---------- LEVEL CAP GIMNASIOS ----------
section_title(pdf, "TOPE DE NIVEL POR GIMNASIO (LEVEL CAP)")
pdf.set_font("Helvetica", "I", 9.5)
pdf.set_text_color(80, 80, 80)
pdf.multi_cell(0, 5, "No puedes tener Pokemon por encima del nivel del as del lider hasta vencerlo. "
                     "Si uno se pasa, no combate hasta superar ese gimnasio.",
               new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)
pdf.set_text_color(*DARK)

gyms = [
    ("1", "Roxanne",        "Ciudad Ferrica",     "Roca",      "15"),
    ("2", "Brawly",         "Ciudad Portual",     "Lucha",     "18"),
    ("3", "Wattson",        "Ciudad Malvalona",   "Electrico", "24"),
    ("4", "Flannery",       "Pueblo Lavacalda",   "Fuego",     "29"),
    ("5", "Norman",         "Ciudad Petalia",     "Normal",    "31"),
    ("6", "Winona",         "Ciudad Arborada",    "Volador",   "37"),
    ("7", "Vito y Leti",    "Ciudad Algaria",     "Psiquico",  "42"),
    ("8", "Plubio / Wallace","Ciudad Arrecipolis","Agua",      "46"),
]

# Cabecera de tabla
widths = [12, 42, 50, 36, 24]
headers = ["#", "Lider", "Ciudad", "Tipo", "Cap"]
pdf.set_font("Helvetica", "B", 10)
pdf.set_fill_color(*RED)
pdf.set_text_color(*WHITE)
for w, h in zip(widths, headers):
    align = "C" if h in ("#", "Cap") else "L"
    pdf.cell(w, 8, h, border=0, align=align, fill=True)
pdf.ln()

pdf.set_text_color(*DARK)
pdf.set_font("Helvetica", "", 10)
for i, (n, lider, city, tipo, cap) in enumerate(gyms):
    fill = i % 2 == 0
    pdf.set_fill_color(*(LIGHT_RED if fill else WHITE))
    pdf.cell(widths[0], 8, n, align="C", fill=True)
    pdf.cell(widths[1], 8, lider, fill=True)
    pdf.cell(widths[2], 8, city, fill=True)
    pdf.cell(widths[3], 8, tipo, fill=True)
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(*DARK_RED)
    pdf.cell(widths[4], 8, cap, align="C", fill=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(*DARK)
    pdf.ln()

# ---------- ALTO MANDO ----------
section_title(pdf, "ALTO MANDO + CAMPEON")
e4 = [
    ("Sidney",  "Siniestro", "51"),
    ("Phoebe",  "Fantasma",  "53"),
    ("Glacia",  "Hielo",     "54"),
    ("Drake",   "Dragon",    "56"),
    ("Steven (Campeon)", "Acero", "58"),
]
w2 = [70, 60, 34]
pdf.set_font("Helvetica", "B", 10)
pdf.set_fill_color(*RED)
pdf.set_text_color(*WHITE)
for w, h in zip(w2, ["Rival", "Tipo", "Cap"]):
    align = "C" if h == "Cap" else "L"
    pdf.cell(w, 8, h, fill=True, align=align)
pdf.ln()
pdf.set_text_color(*DARK)
pdf.set_font("Helvetica", "", 10)
for i, (rival, tipo, cap) in enumerate(e4):
    fill = i % 2 == 0
    pdf.set_fill_color(*(LIGHT_RED if fill else WHITE))
    pdf.cell(w2[0], 8, rival, fill=True)
    pdf.cell(w2[1], 8, tipo, fill=True)
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(*DARK_RED)
    pdf.cell(w2[2], 8, cap, align="C", fill=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(*DARK)
    pdf.ln()

pdf.ln(3)
pdf.set_font("Helvetica", "I", 9)
pdf.set_text_color(110, 110, 110)
pdf.multi_cell(0, 5, "Nota: los niveles son aproximados (el as de cada lider) y pueden variar +/-1-2 "
                     "segun tu randomizacion, ya que el randomizer puede reajustar niveles. "
                     "Usalos como referencia de cap.", new_x="LMARGIN", new_y="NEXT")
pdf.set_text_color(*DARK)

# ---------- EXTRAS ----------
section_title(pdf, "REGLAS EXTRA (OPCIONALES)")
extras = [
    ("Sin legendarios:", "muchos los prohiben en combate porque rompen el balance."),
    ("Box legendaries:", "si el randomizer pone un legendario como encuentro de zona, decide antes si vale."),
    ("Clausula de evolucion:", "evoluciones por nivel se respetan; las de objeto o intercambio, libres."),
    ("Modo Hardcore:", "sin comprar objetos curativos; solo usas lo que encuentres por el mundo."),
]
pdf.set_font("Helvetica", "", 10.5)
for title, body in extras:
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(*DARK_RED)
    pdf.cell(4, 6, "-", new_x="RIGHT", new_y="TOP")
    w_title = pdf.get_string_width(title + " ")
    pdf.set_text_color(*DARK)
    pdf.cell(w_title, 6, " " + title, new_x="RIGHT", new_y="TOP")
    pdf.set_font("Helvetica", "", 10.5)
    pdf.multi_cell(0, 6, " " + body, new_x="LMARGIN", new_y="NEXT")

pdf.output("/home/user/skills/Randomlocke_Omega_Ruby.pdf")
print("PDF generado correctamente.")

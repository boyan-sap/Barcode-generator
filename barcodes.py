import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code128
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

# Učitavanje Excel fajla sa pozicijama
df = pd.read_excel("positions.xlsx")
pozicije = df.iloc[:, 0].dropna().astype(str).tolist()

# Podešavanje stranice
stranica_sirina, stranica_visina = A4
kolone = 3
redovi = 8
razmak_x = 70 * mm
razmak_y = 35 * mm
margin_x = 15 * mm
margin_y = 15 * mm

# Kreiranje PDF fajla
c = canvas.Canvas("barcodes.pdf", pagesize=A4)

for i, pozicija in enumerate(pozicije):
    pozicija_na_strani = i % (kolone * redovi)
    kolona = pozicija_na_strani % kolone
    red = pozicija_na_strani // kolone

    if pozicija_na_strani == 0 and i != 0:
        c.showPage()  # Nova stranica

    # Izračunaj poziciju barkoda
    x = margin_x + kolona * razmak_x
    y = stranica_visina - margin_y - red * razmak_y - 20

    # Generisanje barkoda
    barkod = code128.Code128(pozicija, barHeight=20 * mm, barWidth=1)
    barkod.drawOn(c, x, y)

    # Dodavanje teksta ispod barkoda
    c.setFont("Helvetica", 16)
    c.drawCentredString(x + 27 * mm, y - 15, pozicija)

c.save()
print("PDF is saved as 'barcodes.pdf'.")

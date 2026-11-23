from pathlib import Path

def export_pdf(title: str, lines: list[str], path: Path) -> None:
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    pdf=canvas.Canvas(str(path),pagesize=letter); width,height=letter
    pdf.setTitle(title); y=height-54; pdf.setFont("Helvetica-Bold",16); pdf.drawString(48,y,title); y-=32; pdf.setFont("Helvetica",10)
    for line in lines:
        if y<48: pdf.showPage(); y=height-48; pdf.setFont("Helvetica",10)
        pdf.drawString(48,y,str(line)[:110]); y-=15
    pdf.save()

from fpdf import FPDF

# The orientation of the pdf should be Portrait, and the format A4
# The top of the PDF should say "CS50 Shirtificate" as text, centered horizontally
# The shirt image should be centered horizontally
# The user's name should be on top of the shirt, in white text

def cs50_base():
    pdf.set_font("Helvetica", style="B", size=40)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(
        200, 
        60, 
        "CS50 Shirtificate", 
        align="C"
    )
    pdf.image("shirtificate.png", 15, 70, w=180)
    pdf.ln(3)

def name_print():
    name = input("Name: ")
    pdf.set_font("Helvetica", style="B", size=18)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(
        200,
        220,
        f"{name} took CS50",
        align="C"
    )


pdf = FPDF(orientation="P", format="A4")
pdf.add_page()

cs50_base()
name_print()

pdf.output("shirtificate.pdf")


from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(text):

    doc = SimpleDocTemplate('startup_report.pdf')

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(text, styles['BodyText'])
    )

    doc.build(story)

    
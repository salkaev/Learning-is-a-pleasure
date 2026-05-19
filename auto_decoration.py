from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document("1000.docx") # Наш документ открываем

for stro in doc.paragraphs:
    if "Глава" in stro:
        stro.alignment = WD_ALIGN_PARAGRAPH.CENTER

from docx import Document

def read_data_from_docx(file_path):
    doc = Document(file_path)
    data = []
    for table in doc.tables:
        row_data = {}
        for row in table.rows:
            key = row.cells[0].text.strip()
            value = row.cells[1].text.strip()
            row_data[key] = value
        data.append(row_data)
    return data

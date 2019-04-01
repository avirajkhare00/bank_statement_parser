import camelot
import json

tables = camelot.read_pdf('./files/statement_2.pdf')

tables.export('output.json', f='json', compress=False)

f = open('output-page-1-table-1.json')

for row in json.loads(f.read()):

    print(row)

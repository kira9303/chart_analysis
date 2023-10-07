from pyxlsb import open_workbook

with open_workbook('HugeDataFile.xlsb') as wb:
    for sheetname in wb.sheets:
        with wb.get_sheet(sheetname) as sheet:
            for row in sheet.rows():
                values = [r.v for r in row]  # retrieving content
                #print(values)
                csv_line = ','.join(values)  # or do your thing


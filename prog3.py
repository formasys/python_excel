import openpyxl

fichiers=['/Users/macbookair/Desktop/openpyxl/january.xlsx','/Users/macbookair/Desktop/openpyxl/february.xlsx','/Users/macbookair/Desktop/openpyxl/march.xlsx']

for fichier in fichiers:
    wb=openpyxl.load_workbook(fichier)
    feuille=wb['Sheet1']
    feuille['F9']='=SUM(F5:F8)'
    feuille['E9']='Total Global'
    feuille['F9'].style='Currency'
    wb.save(fichier)

import pandas as pd

#lister les fichiers à combiner
fichiers=['/Users/macbookair/Desktop/openpyxl/january.xlsx','/Users/macbookair/Desktop/openpyxl/february.xlsx','/Users/macbookair/Desktop/openpyxl/march.xlsx']

#creer le fichier comibiné de type dataframe
fichier_combine=pd.DataFrame()

#combiner les trois fichiers
for fichier in fichiers:
    df=pd.read_excel(fichier,skiprows=3)
    print(df)
    fichier_combine=fichier_combine.append(df,ignore_index=True)

#créer le fichier excel correspondant
fichier_combine.to_excel('fich_comb.xlsx')


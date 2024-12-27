import tabula
import csv
import pandas as pd

def read_pdf( file ):

    try:
        dfs = tabula.read_pdf( file, pages=1)
        return dfs[0]
    except Exception:
        print("Arquivo não existe")
        return None

# cria novo DataFrame
def create_data_frame( primary_df ):
    # armazenar o nome do vereador
    _firstcol = primary_df.columns[0]
    names = _shear_names( primary_df[_firstcol][1] )
    
    # procurar a linha que se encontra o titulo CNPJ

# funcao que retira a palavra vereador do nome e retorna primeiro
# nome e sobrenome
def _shear_names( str_name ):
    #strip word vereador: and split first name and last names
    names = str_name.split(" ", 1)[1]
    names = names.split(" ", 1)
    print( names )

df = read_pdf( "librev.pdf" )
create_data_frame( df )
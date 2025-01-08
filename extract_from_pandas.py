import tabula

# melhora isso aqui para ler multiplas páginas
def read_pdf( file ):

    try:
        dfs = tabula.read_pdf( file, pages='all', pandas_options={'dtype':'str'}) # entrega um Dataframe
        return dfs
    except Exception:
        print("Arquivo não existe")
        return None

# cria novo DataFrame
def create_data_frame( primary_df ):
    
    # armazenar o nome do vereador
    _firstcol = primary_df.columns[0]
    names = _shear_names( primary_df[_firstcol][1] )
    
    # procurar a linha que se encontra o titulo CNPJ
    
    new_frame = primary_df.drop( range(0,9) )
    new_frame.insert(0, 'fname', names[0])
    new_frame.insert(1, 'lname', names[1])
    new_frame.insert(4, 'Nro.Documento', None)
    new_frame   =   new_frame.head( -1 )
    new_frame   =   new_frame.iloc[:, :-2]
    new_frame.rename(columns={_firstcol:'CNPJ', 'Unnamed: 0':'Data Documento', 'Unnamed: 1':'Fornecedor', 'Unnamed: 2':'Item de Despesa', 'Unnamed: 3':'Valor (R$)'}, inplace=True)

    # Split 'Data Documento' and assign the second part to 'Nro.Documento'
    new_frame['Nro.Documento'] = new_frame['Data Documento'].apply(lambda x: x.split()[1] if len(x.split()) > 1 else None)
    new_frame['Data Documento'] = new_frame['Data Documento'].apply(lambda x: x.split()[0])

    print( new_frame.head())


# funcao que retira a palavra vereador do nome e retorna primeiro
# nome e sobrenome
def _shear_names( str_name ):
    
    #strip word vereador: and split first name and last names
    names = str_name.split(" ", 1)[1]
    names = names.split(" ", 1)
    
    return names

df = read_pdf("relatorio_ceap.pdf")
for i in range(len(df)):
    print( df[i].head() )
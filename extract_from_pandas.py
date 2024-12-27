import tabula

# melhora isso aqui para ler multiplas páginas
def read_pdf( file ):

    try:
        dfs = tabula.read_pdf( file, pages=1) # entrega um Dataframe
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
    
    new_frame = primary_df.drop( range(0,9) )
    new_frame.insert(0, 'fname', names[0])
    new_frame.insert(1, 'lname', names[1])
    new_frame.insert(4, 'Nro.Documento', None)
    new_frame   =   new_frame.head( -1 )
    new_frame   =   new_frame.iloc[:, :-2]
    new_frame.rename(columns={_firstcol:'CNPJ', 'Unnamed: 0':'Data Documento', 'Unnamed: 1':'Fornecedor', 'Unnamed: 2':'Item de Despesa', 'Unnamed: 3':'Valor (R$)'}, inplace=True)

    print( new_frame.head())


# funcao que retira a palavra vereador do nome e retorna primeiro
# nome e sobrenome
def _shear_names( str_name ):
    
    #strip word vereador: and split first name and last names
    names = str_name.split(" ", 1)[1]
    names = names.split(" ", 1)
    
    return names

df = read_pdf( "librev.pdf" )
create_data_frame( df )

00020101021226850014br.gov.bcb.pix2563qrcodepix.bb.com.br/pix/v2/bf8a9d58-f823-41bf-ab47-d9bfa809fe9c5204000053039865406203.065802BR5906DETRAN6006MANAUS62070503***6304B692
00020101021226850014br.gov.bcb.pix2563qrcodepix.bb.com.br/pix/v2/72924483-c8a4-4a18-a5e9-7d0da86696f25204000053039865406210.325802BR5904IMMU6006MANAUS62070503***63047059
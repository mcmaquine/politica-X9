import tabula
import csv
import pandas as pd

dfs = tabula.read_pdf("librev.pdf")

print( dfs[0].head(25) )
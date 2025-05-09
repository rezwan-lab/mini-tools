# -*- coding: utf-8 -*-
"""match_unmatch.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-FrEYeFvpaGz9dUNorx2VhrQl_ogiTeC
"""

import pandas as pd
import numpy as np
!pip install pivottablejs
from pivottablejs import pivot_ui
from IPython.display import HTML
from IPython.display import IFrame
import json, io

from google.colab import drive
drive.mount('/content/drive')

df1 = pd.read_table("/content/drive/MyDrive/Colab Notebooks/WA_101_IBDC/nextstrain_metadata.tsv", sep='\t')

#Omicron(BA.1, BA.1.1, BA.2)

#upload_defining_mutations
df2 = pd.read_table("/content/drive/MyDrive/Colab Notebooks/WA_101_IBDC/insacog_metadata_strain.tsv", sep='\t')

df3 = df1[df1['strain'].isin(df2["strain"])]

df3.to_csv('insacog_metadata_v3.csv', index=False)

df3.to_csv('insacog_metadata_v3.1.tsv', sep="\t", index=False)

# array = ['ORF1a:S135R', 'ORF1a:T842I', 'ORF1a:K856R', 'ORF1a:G1307S', 'ORF1a:S2083I', 'ORF1a:A2710T', 'ORF1a:L3027F', 'ORF1a:T3090I', 'ORF1a:L3201F', 'ORF1a:T3255I', 'ORF1a:P3395H', 'ORF1a:I3758V',
# 'ORF1b:P314L', 'ORF1b:R1315C', 'ORF1b:I1566V', 'ORF1b:T2163I', 'S:T19I', 'S:L24S', 'S:del25/27', 'S:A67V', 'S:del69/70', 'S:T95I', 'S:G142D', 'S:N211I', 'S:V213G', 'S:G339D', 'S:R346K', 'S:S371F', 'S:S373P', 'S:S375F', 'S:T376A', 'S:D405N', 'S:R408S', 'S:K417N', 'S:N440K', 'S:S477N', 'S:T478K', 'S:E484A', 'S:Q493R', 'S:G496S', 'S:Q498R',
# 'S:N501Y', 'S:Y505H', 'S:T547K', 'S:D614G', 'S:H655Y', 'S:N679K', 'S:P681H', 'S:N764K', 'S:D796Y', 'S:N856K', 'S:Q954H', 'S:N969K', 'S:L981F', 'ORF3a:T223I', 'E:T9I', 'M:D3G', 'M:Q19E', 'M:A63T', 'ORF6:D61L', 'ORF8:S84L', 'N:P13L', 'N:R203K', 'N:G204R', 'N:S413R']
# mutation2 = mutation1.loc[~mutation1['aaSubstitutions'].isin(array)]

#mutation2 = mutation1.loc[mutation1['aaSubstitutions'].isin(array)]
#mutation2 = mutation1.loc[~mutation1['aaSubstitutions'].isin(array)]

# df1[df1['lineage'].isin(df2["lineage"])]

# #df1[~df1['lineage'].isin(df2["lineage"])]
# -*- coding: utf-8 -*-
"""Subsample.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11jzqSh97iTlEU8IrKw5xaB6LAVxxEbCO
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

df = pd.read_table("/content/drive/.../nextstrain_metadata.tsv", sep='\t')

# recent_samples = df[df['collection_month'] == 'Feb-2022']

# recent_samples.to_csv('recent_samples.tsv', sep="\t", index=False)

l1 = df[df['collection_month'] == 'Mar-2022']
l2 = df[df['collection_month'] == 'Apr-2022']

recent_samples = pd.concat([l1,l2], join="inner")

recent_samples.to_csv('recent_samples.tsv', sep="\t", index=False)

#upload
#set1_reference
set1 = pd.read_table("/content/drive/.../subsample/set1_reference_metadata.tsv", sep='\t')
#set2_global
#set2 = pd.read_table("/content/drive/MyDrive/Colab Notebooks/WA70_08.02.2022_mask/nextstrain_metadata_WA70.tsv", sep='\t')
#set3_subsample1
set3 = pd.read_table("/content/drive/.../set3_subsample1_metadata.tsv", sep='\t')
#set4_subsample2
set4 = pd.read_table("/content/drive/.../set4_subsample2_metadata.tsv", sep='\t')
#set5_rescent_sample
set5 = recent_samples

subsample=pd.concat([set1, set3, set4, recent_samples], join="inner")

subsample.to_csv('subsampled_metadata.tsv', sep="\t", index=False)

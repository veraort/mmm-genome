#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  13 13:14:06 2020

@author: vortseifen
"""

import subprocess
import argparse
import pandas
 
# open csv with pandas and write in dictionary
df = pandas.read_csv("/Users/veraortseifen/Documents/PostDoc/2020-/Xanthomonas/csv_vorlage_new.csv",sep=";")
% insert csv file contain old and new locus tags and informations you want to add


#Create a list for genbank
f=open("/Users/veraortseifen/Documents/PostDoc/2020-/Xanthomonas/W15_neu.gb")
lines=f.readlines()
f.close
% insert genbank file of the genome you want to extend with more informations
            
#If the key from lines is in the annotationfile add the description and the name to its value behind locus tags ; especially add old locus tag and description
file=open("W15_neu_extended.gb","w") #neue Datei erstellen und direkt reinschreiben
for i in lines:
    file.write(i)
    if i.startswith("                     /locus_tag="):
        i.find("/locus_tag")!=-1
        locus_tag=i.split('"')#Split the line by "
        y=df[df["locus_tag"].str.match(locus_tag[1])]
        if len(y)>0:
            locus_old=y.iloc[0]["locus_tag_old"]
            file.write("/".rjust(22)+"locus_tag_old"+'="' + str(locus_old) + '"'+"\n")
            gene_old=y.iloc[0]["gene"]
            file.write("/".rjust(22)+"gene_old"+ '="' + str(gene_old) + '"'+"\n")
            product_old=y.iloc[0]["product"]
            file.write("/".rjust(22)+"product_old"+ '="' + str(product_old) + '"'+"\n")

file.close()

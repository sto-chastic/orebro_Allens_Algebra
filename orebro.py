# -*- coding: utf-8 -*-
"""
@author: David Jimenez
"""
import pandas as pd
import itertools

def compTable():
    indAndCol = ['p','m','o','F','D','s','e','S','d','f','O','M','P']
    compoTable = pd.DataFrame(columns=indAndCol, index = indAndCol)
    compoTable.ix['p'] = ['p',	'p',	'p',	'p',	'p',	'p',	'p',	'p',	'pmosd',	'pmosd',	'pmosd',	'pmosd',	'pmoFDseSdfOMP']
    compoTable.ix['m'] = ['p',	'p',	'p',	'p',	'p',	'm',	'm',	'm',	'osd',	'osd',	'osd',	'Fef',	'DSOMP',]
    compoTable.ix['o'] = ['p',	'p',	'pmo',	'pmo',	'pmoFD',	'o',	'o',	'oFD',	'osd',	'osd',	'oFDseSdfO'	,'DSO',	'DSOMP',]
    compoTable.ix['F'] = ['p',	'm',	'o',	'F',	'D',	'o',	'F',	'D',	'osd',	'Fef',	'DSO',	'DSO',	'DSOMP',]
    compoTable.ix['D'] = ['pmoFD',	'oFD',	'oFD',	'D',	'D',	'oFD',	'D',	'D',	'oFDseSdfO',	'DSO',	'DSO',	'DSO',	'DSOMP',]
    compoTable.ix['s'] = ['p',	'p',	'pmo',	'pmo',	'pmoFD',	's',	's',	'seS',	'd',	'd',	'dfO',	'M',	'P',]
    compoTable.ix['e'] = ['p',	'm',	'o',	'F',	'D',	's',	'e',	'S',	'd',	'f',	'O',	'M',	'P',]
    compoTable.ix['S'] = ['pmoFD',	'oFD',	'oFD',	'D',	'D',	'seS',	'S',	'S',	'dfO',	'O',	'O',	'M',	'P',]
    compoTable.ix['d'] = ['p',	'p',	'pmosd',	'pmosd',	'pmoFDseSdfOMP',	'd',	'd',	'dfOMP',	'd',	'd',	'dfOMP',	'P',	'P',]
    compoTable.ix['f'] = ['p',	'm',	'osd',	'Fef',	'DSOMP',	'd',	'f',	'OMP',	'd',	'f',	'OMP',	'P',	'P',]
    compoTable.ix['O'] = ['pmoFD',	'oFD',	'oFDseSdfO',	'DSO',	'DSOMP',	'dfO',	'O',	'OMP',	'dfO',	'O',	'OMP',	'P',	'P',]
    compoTable.ix['M'] = ['pmoFD',	'seS',	'dfO',	'M',	'P',	'dfO',	'M',	'P',	'dfO',	'M',	'P',	'P',	'P',]
    compoTable.ix['P'] = ['pmoFDseSdfOMP',	'dfOMP',	'dfOMP',	'P',	'P',	'dfOMP',	'P',	'P',	'dfOMP',	'P',	'P',	'P',	'P',]         
    return compoTable

def multipleDisjunctions(asso, table):
    compo =[]
    for i  in range(0, len(asso)):
        compo.extend(list(table.ix[asso[i][0],asso[i][1]]))
    
    compoDisj = list(set(compo))
    
    return compoDisj

def simple3(c1,c2,c3):

    if(len(c1) | len(c2) >1):
        association = [[c1[a],c2[b]] for a in range(0,len(c1)) for b in range(0,len(c2))]
        c3_temp = multipleDisjunctions(association,compoTable)
    else:
        c3_temp = compoTable.ix[c1,c2]
        
    if(len(c3)==0):
        c3_prime = c3_temp
    else:
        c3_prime = list(set(c3_temp).intersection(c3))

    return c3_prime
     
    if (len(c3_prime)<1):
        print('FALSE. Constraint C3 is not path-consistent.')
    else:
        print('Constraint C3 prime is')
        print(c3_prime)

if __name__ == '__main__':
    compoTable = compTable()
    c = []
    i = 1
    ctemp = [1]
    while len(ctemp) != 0:
        ctemp = list(str(input('Enter C'+str(i)+', e.g.: type p , if the constraint is I'+str(i)+' {p} I'+str(i+1)+'. Do not introduce quotations, just p. If your network does not have more nodes, leave this blank and hit enter: ')))
        if len(ctemp) != 0:
            c.append(ctemp)
            i = i+1
        
    cs1 = list(str(input('Enter C1, e.g.: p , if the constraint is I1 {p} I2. Do not introduce quotations, just p... : ')))
    cs2 = list(str(input('Enter C2, e.g.: p , if the constraint is I2 {p} I3... :  ')))
    cs3 = list(str(input('Enter C3, e.g.: p , if the constraint is I1 {p} I3. OR leave blank if you do not know... : ')))

    
    
    
    
    
#==============================================================================
#     cs1 = list(str(input('Enter C1, e.g.: p , if the constraint is I1 {p} I2. Do not introduce quotations, just p... : ')))
#     cs2 = list(str(input('Enter C2, e.g.: p , if the constraint is I2 {p} I3... :  ')))
#     cs3 = list(str(input('Enter C3, e.g.: p , if the constraint is I1 {p} I3. OR leave blank if you do not know... : ')))
# 
#==============================================================================

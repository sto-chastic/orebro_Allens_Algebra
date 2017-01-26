# -*- coding: utf-8 -*-
"""
@author: David Jimenez
"""
import pandas as pd


def compTable():
    
#==============================================================================
#     This method generates the composition table of pairs of conjunctions for later use.    
#==============================================================================
    
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
    
#==============================================================================
#     This method computes the composition of conjunctions of relations.
#     Ultimately, the result is the conjunction of every composition of the distribution
#     of relations in the two conditions - due to the distributive property.
#==============================================================================
    
    compo =[]
    for i  in range(0, len(asso)):
        #Gets the composition of all distributions of the relations.
        compo.extend(list(table.ix[asso[i][0],asso[i][1]]))
    #Removes duplicated relations as this is a conjunction.
    compoDisj = list(set(compo))
    
    return compoDisj

if __name__ == '__main__':

#==============================================================================
#     Generate the Composition Table for the Allen's Temporal Algebra    
#==============================================================================
    
    compoTable = compTable()  
    
#==============================================================================
#     Print the instructions and catch the input from the user
#==============================================================================
    
    print(' ')
    print(' ')
    print(' ')
    print('This program checks path consistency between 3 edges in the context of Allans interval algebra. ')
    print('The relations are as follows: precedes (p), meets (m), overlaps (o), finished by (F), contains (D), starts (s), equals (e).')
    print('A capital letter means the converse relation, e.g.: finished by (F) and finishes (f).')
    input('Press Enter to continue')
        
    c1 = list(str(input('Enter C1. E.g.: p , if the constraint is I1 {p} I2. Do not introduce quotations, just p... : ')))
    c2 = list(str(input('Enter C2. E.g.: p , if the constraint is I2 {p} I3... :  ')))
    c3 = list(str(input('Enter C3. E.g.: p , if the constraint is I1 {p} I3. OR leave blank if you do not know... : ')))

#==============================================================================
#     Check weather the conditions input conditions are a conjunction of various relations
#     or simple relations.
#==============================================================================

    if(len(c1) | len(c2) >1):
        #This distributes the conjunction of relations and computes the result
        #of each simple composition of two relations
        distr = [[c1[a],c2[b]] for a in range(0,len(c1)) for b in range(0,len(c2))]
        c3_temp = multipleDisjunctions(distr,compoTable)
    else:
        #If the relations are simple relations and no conjunctions, this
        #calculates the composition.
        c3_temp = compoTable.ix[c1,c2]
        
#==============================================================================
#     If no input was given for I1 {relation} I3, then the program generates the
#     answer. Otherwise, if the input was given, then the program checks the input,
#     and refines the solution, or if there is no path consistency, it returns FALSE.
#==============================================================================
        
    if(len(c3)==0):
        c3_prime = c3_temp
    else:
        c3_prime = list(set(c3_temp).intersection(c3))
    
    if (len(c3_prime)<1):
        print('FALSE. Constraint C3 is not path-consistent.')
    else:
        print('Constraint C3 prime is:')
        print(''.join(c3_prime))
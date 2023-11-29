#!/usr/bin/env python3

genes= {}               #criando o dicionário e os seus valores
seqName = ''
seq = ''
seq_id = ''

with open('Python_08.fasta', 'r') as f:             #comando para abrir o arquivo em modo leitura
    for l in f:                       
        if l.startswith('>'):                       #comando para pegarmos cada códon separadamente, uma vez que todo códon começa com ">"
            genes[seq_id] = { 'sequence' : seqName , 'description' : seq} 
            seqName = ''
            l = l.rstrip('>')             
            l = l.rstrip().upper() 
            seq_id, seq = l.split(maxsplit = 1)

        else:
            seqName += l.rstrip()

    for k in genes.keys():
        seq_c= genes.get(k).get('sequence')        #contagem dos genes
        cA = seq_c.count('A')
        cT = seq_c.count('T')
        cC = seq_c.count('C')
        cG = seq_c.count('G')


        print("seqName\t\tA_count\tT_count\tG_count\tC_count") 
        print(k+'\t'+str(cA)+'\t'+str(cT)+'\t'+str(cG)+'\t'+str(cC))  #imprimindo o valor da contagem      
        


# Programm võtab .FASTA formaadis dna järjestuse ja eeldab, et valgusüntees algab AUG ja lõppeb stopp-koodoniga.
# Programm väljastab kõik võimalikude sünteesitavate valkude aminohappete järjestused .FASTA fileina
# Salvestatud fail salvestab samma directory'isse kus programm parasjagu on

# Funktsioon 'translatsioon' võtab kasutaja poolt antud dna järjestuse (mis on muudetud rna-ks, lihtsuse mõttes).
# Sõnastiku ja tsükkli abil asendab järjestuses 3 nukleotiidi kaupa sellele vastava aminohappe (või stopp_koodon "_")
# Funktsioon tagastab valgu aminohappe järjestuse stringina, see on lihtsalt terve järjestus muudetud aminohappeteks.
def translatsioon(rna):
    geenid = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "_", "UAG": "_",
    "UGU": "C", "UGC": "C", "UGA": "_", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }
    valk = ''
    if len(rna)%3 == 0:
        for i in range(0, len(rna), 3):
            koodon = rna[i:i + 3]
            valk+= geenid[koodon]
    return valk

#Küsib kasutajalt faili nime. Kustutab ebavajaliku info seal maha ja muudab dna rna järjestuseks
dna_jarjestus = input('Sisestage dna järjestus mida soovite transkripteerida (.FASTA formaadis): ')
dna_fail = open(dna_jarjestus)
dna = dna_fail.read()
dna = dna[19:]
rna = dna.replace('T','U').replace('\n','')
dna_fail.close() 

# Võtab translatsioonist saadud valgu järjestuse ning tükeldab stopp-koodonitega valgu tükkideks(mida lisab listi)
valk = translatsioon(rna)
valk_list = valk.split('_')
intronid_list = []

# Filtreerib ainult need valgud millel on metioniin ("M")
# Eeldus et süntees toimub lühemat teed pidi
for valk in valk_list:
    if 'M' in valk:
        asukoht = valk.find('M')
        if len(valk[asukoht:-1]) < len(valk[0:asukoht+1]):
            intronid_list.append(valk[asukoht:-1])
        else:
            if len(valk[0:asukoht+1]) > 2:
                intronid_list.append(valk[0:asukoht+1])
            else:
                intronid_list.append(valk[asukoht:-1])

# Salvestab informatsiooni faili
analüüsi_salvestus = 'analüüsi_salvestus.FASTA'
fail = open(analüüsi_salvestus,'a')
for intron in intronid_list:
    fail.writelines(intron+"\n")
fail.close()
print("analüüs edukalt läbi viidud, analüüsi tulemused on salvestatud faili nimega analüüs_salvestus.FASTA")

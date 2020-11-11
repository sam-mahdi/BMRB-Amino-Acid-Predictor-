"""
Parameters

Modify the list of values with all carbon or proton values attributed to your amino acid

"""


list_of_values=[29.09,61.66]


def compare_to_bmrb(values,residue_list,carbon_list,list2):
    with open('bmrb.csv') as file:
        for lines in file:
            if lines == '\n':
                continue
            split_lines=lines.split(',')
            residue=split_lines[0]
            if residue == 'comp_id':
                continue
            residue_list.append(residue)
            atom=split_lines[1]
            chemical_shift=float(split_lines[5])
            std=float(split_lines[6])
            lower_half=chemical_shift-std
            upper_half=chemical_shift+std
            if residue_list[0] != residue or (residue+atom) == 'VALN':
                if len(carbon_list) >= 1:
                    list2+=(carbon_list)
                    carbon_list.clear()
                else:
                    carbon_list.clear()
                    residue_list.clear()
                    residue_list.append(residue)
            if values>lower_half and values<upper_half:
                carbon_list.append(f'{residue} {atom} {chemical_shift} {std}')

def predict_peak():
    residue_list=[]
    carbon_list=[]
    list2=[]
    list3=[]
    list4=[]
    count=0
    for values in list_of_values:
        count+=1
        if count < 2:
            compare_to_bmrb(values,residue_list,carbon_list,list2)
        else:
            compare_to_bmrb(values,residue_list,carbon_list,list3)
            for entries in list3:
                split_entries=entries.split()
                residue=split_entries[0]
                for entries2 in list2:
                    split_entries2=entries2.split()
                    residue2=split_entries2[0]
                    if residue == residue2:
                        list4.append(entries)
            list2.clear()
            list3.clear()
            list2=list4+list2
            list4.clear()
    if len(list2) == 0:
        print('no match found')
    else:
        print(set(shit.split()[0] for shit in list2))
predict_peak()

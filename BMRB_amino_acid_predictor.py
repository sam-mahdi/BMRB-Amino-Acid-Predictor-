
def read_table(carbon,hydrogen):
    """
    This will go through each amino acid, and check its carbon and hydrogen coordinates.
    If they are within the user inputed range, it will store these in the lists.
    Upon completing an amino acid, it will then go through all the matches, and print them out accordingly"""
    residue_list=[]
    carbon_list=[]
    hydrogen_list=[]
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
                if len(carbon_list) >= 1 and len(hydrogen_list) >= 1:
                    for values in carbon_list:
                        split_carbon=values.split()
                        for values2 in hydrogen_list:
                            split_hydrogen=values2.split()
                            if split_hydrogen[1][1] == split_carbon[1][1]:
                                if float(split_carbon[3]) > (0.25*float(split_carbon[2])) or float(split_hydrogen[3]) > (0.25*float(split_hydrogen[2])):
                                    print(f'{values} {values2} HIGH ERROR')
                                else:
                                    print(values,values2)
                    carbon_list.clear()
                    hydrogen_list.clear()
                else:
                    carbon_list.clear()
                    hydrogen_list.clear()
                    residue_list.clear()
                    residue_list.append(residue)
            if carbon>lower_half and carbon<upper_half:
                carbon_list.append(f'{residue} {atom} {chemical_shift} {std}')
            if hydrogen>lower_half and hydrogen<upper_half:
                hydrogen_list.append(f'{residue} {atom} {chemical_shift} {std}')

def main_loop():
    while True:
        question=input('input carbon and hydrogen values: ')
        split_question=question.split()
        read_table(float(split_question[0]),float(split_question[1]))
        print('\n\n\n')

main_loop()

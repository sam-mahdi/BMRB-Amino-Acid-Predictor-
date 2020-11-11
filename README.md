# BMRB-Amino-Acid-Predictor-
These scripts are tools to assist in determining what type of amino acid the peak is

***BMRB_amino_acid_predictor.py*** will take a carbon (or nitrogen) and hydrogen co-ordinates to predict what amino acid(s) your selected peak could be. 

This is use when in the chsqc (or nhsqc if desired) when you have a peak but it could be multiple things. Rather than looking at the sheets of paper with average carbon and hydrogen chemical shift ranges, this will give you a nice print out (i.e. its just easier than looking at the paper and trying to line up averages). This uses the BMRB average chemical shifts to determine the amino acid(s). 

I.E.
```
input carbon and hydrogen values: 42.32 2.2
#Output
ASP CB 40.895 2.563 ASP HB3 2.667 0.518
```
Both the average chemical shift and error are printed since some values can have high errors. 

```
input carbon and hydrogen values: 21.35 1.12
#output
ALA CB 19.052 3.066 ALA MB 1.352 0.28
MET CE 17.254 4.252 MET ME 1.773 1.563 HIGH ERROR
THR CG2 21.595 1.917 THR MG 1.138 0.279
VAL CG1 21.547 2.434 VAL MG1 0.819 0.333 HIGH ERROR
VAL CG1 21.547 2.434 VAL MG2 0.801 0.431 HIGH ERROR
VAL CG2 21.346 2.531 VAL MG1 0.819 0.333 HIGH ERROR
VAL CG2 21.346 2.531 VAL MG2 0.801 0.431 HIGH ERROR
```
As can be seen here, MET ME (HE) has an error that is almost the same value as its average shift. Making at least its proton value useless. 

A high error is defined as an error that is 25% more than of the average shift (i.e. Val HG1 0.819/4 = 0.2, thus its error is more than 25% of the average shit)

***TOCSY_BMRB_amino_acid_predictor.py*** will take a list of carbon and hydrogen values to attempt to determine what amino acid(s) the peak is. Again, this uses the BMRB, but in this case rather than using a single carbon and hydroen value, you may use multiple. 

Often times you have a may have more than just a carbon and hydrogen value, maybe you have TOCSYs that can also give you various other carbon and hydrogen values (within the same spin system), that can be used to help predict your amino acid. Again, this just simplies having to look at the sheet and trying to determine what amino acid you might have based of all the averages. 

To use simply go into the script, and add all the values that you have. 

I.E.
```
list_of_values=[29.09,61.66]
#output
{'ILE', 'TRP', 'LYS', 'PRO'}
```
Naturally the more data/info you add, the better the prediction will be. 
```
list_of_values=[12.35,16.4,30.4,38.4,0.56,0.92,1.35]
#output
{'ILE'}
```

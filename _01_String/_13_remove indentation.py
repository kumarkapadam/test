# to set the indentation of the first line
import textwrap

'''
CRUD : Update
State : string
Behaviour : =

importing library text wrap and taking a string and passing to dedent method in textwrap class then print
'''

string = '''
        After Gordon, Dent and Batman begin an assault
        on Gotham's organised crime, the mobs hire the Joker, 
        a psychopathic criminal mastermind who wants 
        to bring all the heroes down to his level.'''
final_str = textwrap.dedent(string)
print(final_str)

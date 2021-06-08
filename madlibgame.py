# Developing game for heroku app
# A script from hamlet
# Taken from http://www.redkid.net/cgi-bin/madlibs/hamlet.pl 
print("Fill in the blanks below with whatever words you like.") 
print("When you're done, hit the See the Results! button, and your choices will be inserted into the story.")

Celebrity = input("Celebrity :")
Adjective = input("Adjective :")
Noun_1= input("Noun #1:")
Noun_2 = input("Noun #2:")
Noun_3 = input("Noun #3:")
Noun_4 = input("Noun #4:")
Plural_Noun1 = input("Plural Noun #1:")
Plural_Noun2 = input("Plural Noun #2:")
Plural_Noun3 = input("Plural Noun #3:")
Plural_Noun4 = input("Plural Noun #4:")
liq = input("Type of liquid:")
Verb_1 = input("Verb #1:")
Verb_2 = input("Verb #2:")
Verb_3 = input("Verb #3:")


madlib= f"This is the soliloquy from the play Hamlet, written by {Celebrity}\n \
In the third act of this {Adjective} play . Hamlet, who is sometimes\n \
called the the melancholy {Noun_1} , is suspicious of his stepfather\n \
and hires some actors to act out a scene in which a king is killed\n \
when someone pours {liq} into his {Noun_2} .First,\n \
however, he declaims - To be or not to be , that is the {Noun_3}\n \
Whether 'tis nobler in the mind to suffer the {Plural_Noun1} and\n \
{Plural_Noun2}  ,outrageous fortune, or to take arms against a sea of\n \
{Plural_Noun3} and by opposing end them .To die: to sleep; no more\n \
and by a sleep to say we end the heartache and the thousand natural\n \
{Plural_Noun4} that flesh is heir to, 'tis a consummation devoutly to\n \
be wish'd . To die, to {Verb_1} , to {Verb_2} perchance to\n \
{Verb_3} ay, there's the {Noun_4} .\n"

print(madlib)
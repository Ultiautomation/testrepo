#REGEX
import re
# search  :- It searches the pattern in entire text and if that pattern is found it returns it
# match   :- It searches whether the given text starts with the asked pattern 
# sub     :- Replacing the pattern with new pattern 
# findall :- It extracts the pattern from the data based on given condition 
text1="Obama was the President of USA. Now Biden rules USA"
re.search(r"USA", text1)  # produces first instance
re.search(r"usa", text1, re.I )  # re.I makes the sentence case Insensitive
re.search(r"BIDen", text1, re.I)
# re.I - do not consider the case of the string / ignore the case 
text1="Obama was the President of USA. Now Biden rules USA"
re.match(r"USA",text1) # whether the given text is starting with asked pattern- whether text1 is starting with USA
re.match(r"Obama",text1)  # Whether text1 is starting with Obama - yes then pattern return

from fuzzywuzzy import process
# Define string and array of possible matches
string = "Houston Rockets vs Los Angeles Lakers"
choices = pd.Series(['Houston vs Los Angeles', 'Heat vs Bulls', 'Rockets vs Lakers', 'Lakers vs Rockets'])

print(process.extract(string, choices, limit = 4))
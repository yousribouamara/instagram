import pandas as pd
import re

filepath1 = '/Users/yousribouamara/Downloads/followers_1.csv'
filepath2 = '/Users/yousribouamara/Downloads/following.csv'


a = pd.read_csv(filepath1)
b = pd.read_csv(filepath2)
fers = a['Followers']
fing = b['Following']

#getting rid of annoying timestamps
timestamp_pattern = re.compile(r'^[A-Za-z]{3} \d{1,2}, \d{4}, \d{1,2}:\d{2} [APMapm]{2}$')
fing_filtered = fing[fing.apply(lambda x: isinstance(x, str) and not timestamp_pattern.match(x))]


alphabet = list('abcdefghijklmnopqrstuvwxyz')

#getting rid of \... and nans
fing_filtered = [person for person in fing_filtered if pd.notna(person) and person[0].lower() in alphabet]

#set to remove duplicates
fers_set = set(fers)

#printing ppl who dont follow back
not_in_followers = [person for person in fing_filtered if person not in fers_set]
not_in_followers.remove('Accounts you choose to see content from')
print(not_in_followers)

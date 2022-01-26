scientists = ['Marie Curie', 'Albert Einstein', 'Niels Bohr',
               'Isaac Newton', 'Dmitri Mendeleev', 'Antoine Lavoisier',
           'Carl Linnaeus', 'Alfred Wegener', 'Charles Darwin']

# sort by first name
print(sorted(scientists))
# sort by last name
print(sorted(scientists, key=lambda scientist: scientist.split(' ')[-1]))
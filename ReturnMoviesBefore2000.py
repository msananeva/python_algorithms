"""Return movies that were filmed before 2000"""

movies = [('Citizen Kane', 1941), ('Spirited Away', 2001), ('What a Wonderful Life', 1946)]

pre2k = [title for (title, year) in movies if year < 2000]

print(pre2k)


#________________________________________________


movies = ['Citizen Kane', "Wow", 'Spirited Away', 'What a Wonderful Life']

wmovies = []
for title in movies:
    if title.startswith("W"):
        wmovies.append(title)

print(wmovies)

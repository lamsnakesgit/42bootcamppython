languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihito Matsumoto',
        'PHP': 'Rasmus Lerdorf',
        }

#print(languages['Python'], languages['Rasmus Lerdorf'])
for k, v in languages.items():
    print(k, "was created by", v)

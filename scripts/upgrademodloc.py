def getword(word):
    if word == "siege":
        return "Cookie Trebuchet"
    if word == "expansion":
        return "Hegemony of the Grandmatriarchs"
    if word == "army_size":
        return "Sweet Immigration"
    if word == "income":
        return "Cookie Tax Collectors"
    return "Cookie Rations"


for u in ['siege', 'expansion', 'army_size', 'income', 'morale']:
    for i in range(1, 129):
        print(f' {u}_{i}: "{getword(u)} - Level {i}"')



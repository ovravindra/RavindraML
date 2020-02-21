rarebirds = {
    'Gold-crested Toucan': {
        'Height (m)': 1.1,
        'Weight (kg)': 35,
        'Color': 'Gold',
        'Endangered': True,
        'Aggressive': True}
,
'Pearlescent Kingfisher': {
        'Height (m)': 0.25,
        'Weight (kg)': 0.5,
        'Color': 'White',
        'Endangered': False,
        'Aggressive': False}
,
'Four-meter Hummingbird': {
        'Height (m)': 0.6,
        'Weight (kg)': 0.5,
        'Color': 'Blue',
        'Endangered': True,
        'Aggressive': False}

,
'Giant Eagle': {
        'Height (m)': 1.5,
        'Weight (kg)': 52,
        'Color': 'Black and White',
        'Endangered': True,
        'Aggressive': True}
,
'Ancient Vulture': {
        'Height (m)': 2.1,
        'Weight (kg)': 70,
        'Color': 'Brown',
        'Endangered': False,
        'Aggressive': False}

}

birdlocation = ["In the canopy directly above our heads.",
"Between my 6 and 9 o’clock above.",
"Between my 9 and 12 o’clock above.",
"Between my 12 and 3 o’clock above.",
"Between my 3 and 6 o’clock above.",
"In a nest on the ground",
"Right behind you."]

codes = {
    '111':"In the canopy directly above our heads.",
    '110':"Between my 6 and 9 o’clock above.",
    '101':"Between my 9 and 12 o’clock above.",
    '100':"Between my 12 and 3 o’clock above.",
    '011':"Between my 3 and 6 o’clock above.",
    '010':"In a nest on the ground",
    '001':"Right behind you."
}
actions = ["Back Away", "Cover our Heads","Take a Photograph"]

signal = rarebirds['Giant Eagle']['Aggressive']
print(signal)
print(rarebirds.keys())
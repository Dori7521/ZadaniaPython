# SŁOWNIKI

#1
capitals = {
    'Poland':'Warsaw',
    'Germany':'Berlin',
    'Austria':'Vienna'
}
print(capitals)

#2
dict_keys = capitals.keys()
print(dict_keys)

#3
print(capitals.values())

#4
print(capitals.items())

#5
print(capitals.get('Austria'))
print(capitals.get('Poland'))

#6
stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}

print(stocks.get('PLW'))       # stocks['PLW]

#7
print(stocks['TEN']['Ten Square Games'])

#8
stocks['CDR']['CD Projekt'] = 310
print(stocks['CDR'])

#9
stocks.update({'BBT' : {'Boombit':23}}) # stocks['BBT'] = {'Boombit': 23}
print(stocks.values())

#10
ticker = [
    'ALR', 'CCC', 'CDR', 'CPS', 'DNP',
    'JSW', 'KGH', 'LPP', 'LTS', 'MBK',
    'OPL', 'PEO', 'PGE', 'PGN', 'PKN',
    'PKO', 'PLY', 'PZU', 'SPL', 'TPE'
]

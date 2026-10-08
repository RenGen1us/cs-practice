def winner(names: list[str], scores: list[float]):
    mx = -50000000040404004400440
    best_players = []
    for i in range(len(scores)):
        if scores[i] > mx:
            mx = scores[i]
            best_players.append(names[i])
    if best_players[-1] == best_players[-2]:
        return best_players[-2]
    return best_players[-1]

names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]
    
    
        
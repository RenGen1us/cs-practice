def winner(names: list[str], scores: list[float]):
    mx = float('-inf')
    best_players = []
    best_scores = []
    for i in range(len(scores)):
        if scores[i] > mx:
            mx = scores[i]
            best_scores.append(scores[i])
            best_players.append(names[i])
    if len(best_scores) > 1:
        if best_scores[-1] == best_scores[-2]:
            return best_players[-2]
    return best_players[-1]

def average(scores: list[float]):
    if scores:
        return float(f'{sum(scores) / len(scores):.2f}')
    return 0

def ranking(names: list[str], scores: list[float]):
    order = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
    return [names[j] for j in order]

def above_average(names: list[str], scores: list[float]):
    return [names[j] for j in range(len(scores)) if scores[j] > average(scores)]      
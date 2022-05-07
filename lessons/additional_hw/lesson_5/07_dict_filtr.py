def validate(data):
    return (157 <= data['h'] <= 175) and (50 <= data['w'] <= 70)


def validate_list(candidates):
    passed_candidates = []
    for candidate in candidates:
        if validate(candidate):
            passed_candidates.append(candidate)
    return passed_candidates


candidates = [
    {'name': 'Юрий', 'h': 157, 'w': 60},
    {'name': 'Олег', 'h': 177, 'w': 65},
    {'name': 'Юлия', 'h': 165, 'w': 57},
    {'name': 'Аркадий', 'h': 174, 'w': 59},
]


print(validate_list(candidates))

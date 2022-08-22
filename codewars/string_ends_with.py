def solution(string, ending):
    temp_string = string[len(string)-len(ending):]
    if temp_string == ending:
        return True
    else:
        return False


def solution_2(string, ending):
    return string.endswith(ending)

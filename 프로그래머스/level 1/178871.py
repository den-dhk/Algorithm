# 문제 이름 : 달리기 경주


# 내가 해결한 것 아님
# 참고 자료 : https://dduniverse.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8B%AC%EB%A6%AC%EA%B8%B0-%EA%B2%BD%EC%A3%BC-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

def solution(players, callings):
    dict_players = {player: i for i, player in enumerate(players)}
    for i in callings:
        idx = dict_players[i]
        dict_players[i] -= 1
        dict_players[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
    return players

print(solution(players, callings))
    
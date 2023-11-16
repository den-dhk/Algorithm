# 문제 이름 : 개인정보 수집 유효기간

# 못품

today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]


def solution(today, terms, privacies):
    answer = []
    t_year,t_month,t_day = today.split('.')
    t_year = int(t_year)
    t_month = int(t_month)
    t_day = int(t_day)
    terms_2 = []
    for i in terms:
        terms_type, terms_plus = i.split(' ')
        terms_plus = int(terms_plus)
        terms_2.append((terms_type, terms_plus))

    index = 1
    for privacy in privacies:
        term = privacy[-1]
        n_year,n_month,n_day = privacy.split('.')
        n_day = int(n_day[:-2])
        n_year = int(n_year)
        n_month = int(n_month)
        for j in terms_2:
            if j[0] == term:
                n_month += j[1]
                if n_month > 12:
                    n_month = (n_month % 12)
                    n_year += 1
                n_day -= 1
                if n_day == 0:
                    n_day = 28
                    n_month -= 1
                    if n_month == 0:
                        n_month = 12
                        n_year -= 1
                break
        if t_year > n_year:
            answer.append(index)
        elif t_year == n_year:
            if t_month > n_month:
                answer.append(index)
            elif t_month == n_month:
                if t_day > n_day:
                    answer.append(index)
        index += 1
    return answer
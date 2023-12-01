survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
answer = ''
type_t = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N": 0}
for i in range(len(choices)):
    if choices[i] < 4:
        type_t[survey[i][0]] = type_t[survey[i][0]] + (4-choices[i])
    elif 5 <= choices[i]:
        type_t[survey[i][1]] = type_t[survey[i][1]] + (choices[i]-4)
if type_t["R"] >= type_t["T"]:
    answer += "R"
else:
    answer += "T"
if type_t["C"] >= type_t["F"]:
    answer += "C"
else:
    answer += "F"
if type_t["J"] >= type_t["M"]:
    answer += "J"
else:
    answer += "M"
if type_t["A"] >= type_t["N"]:
    answer += "A"
else:
    answer += "N"
print(answer)
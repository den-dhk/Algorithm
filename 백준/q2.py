def extractErrorLogs(logs):
    # Write your code here
    answer = []
    for i in range(len(logs)):
        if logs[i][2] == 'ERROR' or logs[i][2] == 'CRITICAL':
            answer.append(logs[i])
    answer.sort(key=lambda x:(int(x[0][6:]),int(x[0][3:5]), int(x[0][0:2]), int(x[1][:2]), int(x[1][3:])))
    return answer

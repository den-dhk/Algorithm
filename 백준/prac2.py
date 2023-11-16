score = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
averages = [sum(s) for s in score]
sorted_averages = sorted(averages, reverse=True)
ranks = [sorted_averages.index(a) + 1 for a in averages]
print(ranks)
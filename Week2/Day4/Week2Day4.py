import statistics as sta

# scores = [78, 82, 85, 90, 95]

# mean = sum(scores)/len(scores)
# print(mean)

# print(sta.median(scores))

# print(sta.mode(scores))

# range = max(scores) - min(scores)
# print(range)

# print(sta.variance(scores))
# print(sta.stdev(scores))

scores = [78, 82, 82, 90, 95, 88, 76, 84]
mean = sta.mean(scores)
print(mean)
median = sta.median(scores)
print(median)
mode = sta.mode(scores)
print(mode)
max_scores = max(scores)
min_scores = min(scores)
range = max(scores) - min(scores)
print(range)
variance = sta.variance(scores)
print(variance)
stddev = sta.stdev(scores)
print(stddev)

print(f"Average student score: {mean}")
print(f"Most common scores: {mode}")
print(f"Scores range from {min_scores} to {max_scores}, a spread of {range}")
print(f"The standard deviation is {stddev}, indicating relatively consistent performance")
print(f"Most of students scored above 80")

latency = [45, 32, 50, 28, 60]

def avg(data):
    return sum(data)/len(data)

def summary(data):
    return {"Min": min(data), "Max": max(data), "Average": avg(data)}

print(summary(latency))

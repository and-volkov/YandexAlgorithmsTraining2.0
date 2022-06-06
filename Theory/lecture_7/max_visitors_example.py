"""Найти максимальное число произошедших одновременно событий. Включительно."""


def max_visitors_online(n, time_in, time_out):
    events = []
    for i in range(n):
        events.append((time_in[i], -1))  # приход человека
        events.append((time_out[i], 1))  # уход человека
    events.sort()
    online = 0
    max_online = 0
    for event in events:
        if event[1] == -1:
            online += 1
        else:
            online -= 1
        max_online = max(online, max_online)
    return max_online

def puzzle(diff, cur, prev, level):
    if diff <= level:
        return cur
    else:
        return (diff - level) * (cur + prev) + cur
    
def solution(diffs, times, limit):
    max_level, min_level = max(diffs), 1
    
    while max_level > min_level:
        mid_level = (min_level + max_level) // 2
        total = puzzle(diffs[0], times[0], 0, mid_level)
        
        for i in range(1, len(diffs)):
            prev = times[i-1]
            cur = times[i]
            total += puzzle(diffs[i], cur, prev, mid_level)
        if total <= limit:
            max_level = mid_level
        else:
            min_level = mid_level + 1
    
    return min_level
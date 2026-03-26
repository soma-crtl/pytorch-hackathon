def grade(total_reward, steps):
    # normalize score between 0 and 1
    score = max(0, min(1, total_reward / steps))
    return score
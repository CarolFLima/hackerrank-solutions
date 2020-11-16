def countingValleys(steps, path):
    step_seq = []
    counter = 0
    for step in path:
        if len(step_seq) == 0:
            step_seq.append(step)
        else:
            if step != step_seq[-1]:
                step_seq.pop()
                if len(step_seq)==0 and step == 'U':
                    counter = counter + 1
            else:
                step_seq.append(step)
    return counter
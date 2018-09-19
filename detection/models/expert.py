def fallDetect (acc_series):
    avg_acc = 0
    for acc in acc_series:
        avg_acc += acc
    avg_acc /= len(acc_series)
    if avg_acc >= 6:
        return True
    else:
        return False

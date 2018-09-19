from .models.expert import fallDetect as expertDetect

def detect(acc_series):
    return int(expertDetect(acc_series)) * 1.0

if __name__ == '__main__':
    print(detect([9.0, 10.0, 12.0, 5.0, 7.0]))

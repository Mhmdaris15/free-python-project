import numpy as np

y_true = [int(x) for x in input().split()]
y_pred =  [int(x) for x in input().split()]
tp, tn, fp, fn = 0, 0, 0, 0
for i in range(len(y_true)):
    if y_true[i] == 0 and y_true[i]==y_pred[i]:
        tn += 1
    elif y_true[i] == 0 and y_true[i]!=y_pred[i]:
        fp += 1
    elif y_true[i] == 1 and y_true[i]==y_pred[i]:
        tp += 1
    else:
        fn += 1
print(np.vstack([[float(tp), float(fp)],[float(fn), float(tn)]]))
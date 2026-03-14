
TP = 20
FP = 10
FN = 30

precision = TP / (TP + FP)
recall = TP / (TP + FN)
f_measure = 2 * precision * recall / (precision + recall)

print("Precision:", precision)
print("Recall:", recall)
print("F-Measure:", f_measure)
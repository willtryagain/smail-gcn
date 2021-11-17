import matplotlib.pyplot as plt
from train import *

# what is residual?
# number of hidden params


train_accs, test_accs = [], []

for l in range(2, 11):
	train_acc, test_acc = train(l)
	train_accs.append(train_acc)
	test_accs.append(test_acc)

plt.plot(train_accs)
plt.plot(test_accs)
plt.show()
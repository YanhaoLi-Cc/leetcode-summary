import numpy as np

np.random.seed(42)
input_size = 3
hidden_size = 3
output_size = 2
learning_rate = 0.5

W1 = np.random.randn(input_size, hidden_size) # (3, 3)
W2 = np.random.randn(hidden_size, output_size) # (3, 2)
b1 = np.zeros(hidden_size)
b2 = np.zeros(output_size)

x = np.array([[0.1, 0.2, 0.3]]) # (1, 3)
y_true = np.array([[0.4, 0.6]]) # (1, 2)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def der_sigmoid(a):
    return a * (1 - a) # a = sigmoid(x)

z1 = x @ W1 + b1 # (1, 3)
a1 = sigmoid(z1) # (1, 3)
z2 = a1 @ W2 + b2 # (1, 2)
a2 = sigmoid(z2) # (1, 2)
loss = 0.5 * np.sum((y_true - a2) ** 2)

dl_da2 = a2 - y_true # (1, 2)
dl_dz2 = dl_da2 * der_sigmoid(a2) # (1, 2)
dl_dW2 = a1.T @ dl_dz2 # (3, 1) @ (1, 2) = (3, 2)
dl_db2 = np.sum(dl_dz2, axis=0) # (2, )

dl_da1 = dl_dz2 @ W2.T # (1, 2) * (2, 3) = (1, 3)
dl_dz1 = dl_da1 * der_sigmoid(a1) # (1, 3)
dl_dW1 = x.T @ dl_dz1 # (1, 3).T @ (1, 3) = (3, 3)
dl_db1 = np.sum(dl_dz1, axis=0) # (3, )

W2 -= learning_rate * dl_dW2
b2 -= learning_rate * dl_db2
W1 -= learning_rate * dl_dW1
b1 -= learning_rate * dl_db1
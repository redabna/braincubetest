import numpy as np
import matplotlib.pyplot as plt

def f(N):
    return 0.01 * N * (100 - N)


def Euler(fun, y0, t):
    y = np.zeros(len(t))
    y[0] = y0
    for n in range(0, len(t) - 1):
        y[n + 1] = y[n] + fun(y[n], t[n]) * (t[n + 1] - t[n])
    return y


t = np.linspace(0, 10, 20)
y0 = 1
f = lambda N, t: 0.01 * N * (100 - N)
y = Euler(f, y0, t)
y_int=100/(1+99*np.exp(-t))
plt.plot(t, y, 'b.-',t, y_int, 'r.-')
plt.legend(['Numériquement','Algébriquement'])
plt.grid(True)
plt.title("évolution du nombre de contamination au cours du temps")
plt.show()

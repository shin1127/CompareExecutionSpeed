// Pythonにおける実行速度の測定

import time

num = 100000000  # 計算の繰り返し回数
pi = 0  # 円周率の近似値


if __name__ == '__main__':
    start = time.time()

pi = 0
for i in range(num):
    pi += (1 / (i * 4 + 1) - 1 / (i * 4 + 3))
print(pi4)    # 3.141592153589902

elapsed_time = time.time() - start
print("elapsed_time:% .2f" % elapsed_time + "[sec]")

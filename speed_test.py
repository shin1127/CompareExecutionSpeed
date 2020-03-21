import time

sum_test_date_list = []
pi_test_date_list = []

# 足し算による検証に用いる変数
sum_test_count = 10  # 試行回数
sum_count = 1000000000    # 1回の試行中の処理回数
sum_avg_time = 0

# 円周率算出に用いる変数
pi_test_count = 10  # 試行回数
pi = 0
pi4 = 0
pi_accuracy = 100000000  # 円周率算出の精度


# 足し算による処理時間計測

for i in range(sum_test_count):
    num = 0
    # 開始
    if __name__ == '__main__':
        sum_start = time.time()

        for j in range (sum_count):
            num += 1

    # 終了
    sum_elapsed_time = time.time() - sum_start
    sum_test_date_list.append(sum_elapsed_time)

    # print("elapsed_time:% .2f" % sum_elapsed_time + "[sec]")

print("足し算による試行結果")
for t in sum_test_date_list:
    print(str(t) + "[sec]")


#  円周率算出による処理時間計測

print("円周率算出を開始")

for i in range(pi_test_count):

    if __name__ == '__main__':
        pi_start = time.time()

    for i in range(pi_accuracy):
        pi += (1 / (i * 4 + 1) - 1 / (i * 4 + 3))
    print(pi4)    # 3.141592153589902

    pi_elapsed_time = time.time() - pi_start
    pi_test_date_list.append(pi_elapsed_time)

    # print("elapsed_time:% .2f" % pi_elapsed_time + "[sec]")

print("円周率算出による試行結果")
for t in pi_test_date_list:
    print(str(t) + "[sec]")

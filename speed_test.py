import time
import numpy

sum_test_date_list = []  # 加算処理の結果を格納するリスト
pi_test_date_list = []  # 円周率近似の結果を格納するリスト

# 足し算による検証に用いる変数
sum_test_count = 10  # 試行回数
sum_count = 1000000000  # 1回の試行中の処理回数
sum_avg_time = 0
sum_is_execution = True  # 加算処理計測を実行するかどうか

# 円周率算出に用いる変数
pi_test_count = 10  # 試行回数
pi = 0
pi4 = 0
pi_accuracy = 100000000  # 円周率算出の精度
pi_is_execution = True  # 円周率近似を実行するかどうか


# 足し算による処理時間計測

if sum_is_execution == True:
    print("足し算による処理測定")
    for i in range(sum_test_count):
        num = 0
        # 開始
        if __name__ == '__main__':
            sum_start = time.time()

            for j in range (sum_count):
                num += 1

        # 終了
        sum_elapsed_time = time.time() - sum_start

        calc_number = str(round(sum_elapsed_time, 3)) + " "
        print(calc_number, end="")
        sum_test_date_list.append(sum_elapsed_time)


#  円周率算出による処理時間計測

if pi_is_execution == True:
    print("\n")  # 改行
    print("円周率算出を開始")

    for i in range(pi_test_count):

        pi = 0
        if __name__ == '__main__':
            pi_start = time.time()

        for i in range(pi_accuracy):
            pi += (1 / (i * 4 + 1) - 1 / (i * 4 + 3))
            pi4 = pi * 4    # 3.141592153589902

        # 終了
        pi_elapsed_time = time.time() - pi_start
        pi_calc_number = str(round(pi_elapsed_time)) + " "
        print(pi_calc_number, end="")
        pi_test_date_list.append(pi_elapsed_time)


print("\n")  # 改行

if sum_is_execution == True:
    print("足し算試行の平均時間は" + str(numpy.average(sum_test_date_list)) + "sec")

if pi_is_execution == True:
    print("円周率近似試行による平均時間は" + str(numpy.average(pi_test_date_list)) + "sec")

# 計測結果の桁数を丸めて保存

if sum_is_execution == True:
    file = open("SpeedTestResultByPython.txt", "a")
    file.write("加算処理(sec)\n")
    file.write("処理回数%d" % sum_count)
    for i in sum_test_date_list:
        file.write(str(i) + "\n")
    file.close()

if pi_is_execution == True:
    file = open("SpeedTestResultByPython.txt", "a")
    file.write("近似処理(sec)\n")
    file.write("近似の精度%d" % pi_accuracy)
    for i in pi_test_date_list:
        file.write(str(i) + "\n")
    file.close()


import java.util.ArrayList;

public class SpeedTest {
	public static void main(String[] args) {

        ArrayList<Long> sumTestDateList = new ArrayList<>();  // 足し算試行のデータの格納 msec
        ArrayList<Long> piTestDateList = new ArrayList<>();  // 円周率算出試行のデータの格納 msec

        // 足し算による検証に用いる変数
        int testCount = 10;  // 試行回数
        long sumCount = 1000000000;  // 1回の試行中の処理回数
        long sumAvgTime = 0;

        // 円周率算出による処理時間計測
        double pi = 0;  // 円周率の1/4の近似値
        double pi4 = 0;  // 円周率の近似値
        int piAccuracy = 100000000;  // 円周率算出の精度
        int piCount = 10;  // 円周率を算出する回数
        long piAvgTime = 0;

        // 足し算による処理時間計測
        System.out.println("足し算による処理測定");

        for(int i = 0; i < testCount; i++){
            // 開始
            long sumStartTime = System.currentTimeMillis();
            
            // {count}回の足し算による試行
            int num = 0;
            for(long j = 0; j < sumCount; j++){
                num++;
            }
            
            // 終了
            long sumEndTime = System.currentTimeMillis();

            long sumRequiredTime = sumEndTime - sumStartTime;
            System.out.print(sumRequiredTime + " ");
            sumTestDateList.add(sumRequiredTime);
        }
        System.out.println("");  // 改行

        // 円周率算出による処理時間計測
        System.out.println("円周率算出による処理測定");

        for(int i = 0; i < piCount; i++){

            // 開始
            long piStartTime = System.currentTimeMillis();

            for(int j = 0; j < piAccuracy; j++){
                pi += (1 / (j * 4 + 1) - 1 / (j * 4 + 3));
              }
            pi4 = pi * 4;

            // 終了
            long piEndTime = System.currentTimeMillis();

            long piRequiredTime = piEndTime - piStartTime;
            System.out.print(piRequiredTime + " ");
            piTestDateList.add(piRequiredTime);
        }
        System.out.println("");  // 改行

        // 足し算処理の平均時間を求める
        sumAvgTime = calcAvg(sumTestDateList);
        System.out.println("足し算試行の平均時間は" + sumAvgTime + " msec");

        // 円周率算出の平均時間を求める
        piAvgTime = calcAvg(piTestDateList);
        System.out.println("円周率算出試行の平均時間は" + piAvgTime + " msec");

    }
            // 所要時間の平均化メソッド
            public static long calcAvg(ArrayList<Long> list){
                long total = 0;
                for (long i : list){
                    total += i;
                }
                long avg = total / list.size();
                return avg;
            }
}

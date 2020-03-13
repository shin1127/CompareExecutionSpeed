// JAVAにおける実行速度を測定する

public class SpeedTest{
   public static void main(String[] args){
       long startTime = System.currentTimeMillis();

       //以下に計測する処理を記述

       int num = 100000000;  // 計算の繰り返し回数
       float pi = 0;  // 円周率の近似値を4で割ったもの
       float pi * 4 = 0;  // 円周率の近似値

       for(int i = 0;i<num; i++){
         pi += (1 / (i * 4 + 1) - 1 / (i * 4 + 3));
       }
       pi4 = pi * 4;
       //以上、計測する処理内容

       long endTime = System.currentTimeMillis();

       System.out.println(pi4);

       System.out.println("time:" + (endTime - startTime)+"[msec]");
   }

}

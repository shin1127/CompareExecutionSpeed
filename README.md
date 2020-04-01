# CompareExecutionSpeed

# Introduction
コンパイラ型言語Javaとインタプリタ言語Pythonの処理速度差を検証するのに用いるコンソールアプリケーション。<br>
具体的には、『指定した数の加算処理』、『指定した精度での円周率の近似』を指定した回数だけ繰り返し行い、<br>
その処理にかかったそれぞれの時間を計測し、更に平均値を算出する。<br>
これらの機能を持ったコンソールアプリケーションを、JavaとPythonでそれぞれ作成した。<br>


# Background
コンパイラ型言語とインタプリタ型言語では、機械語への翻訳処理の方法が異なる為に処理速度が大きく異なり、コンパイラ型言語のほうが速いことが知られている。<br>
Java、Pythonと、両言語を学習したが、実際に処理速度差はじゅうぶんに存在するのか、またそれはどの程度のものなのかを知りたいと考えた。

# Leaning in repositry

- Python
  - round関数による数字の丸め方について学んだ。
  - Javaと異なり、Pythonではインクリメント演算子(i++など)は利用できない。
- Java
  - 使い回せるロジックに関してはメソッド化を行い、ソースコードの可読性を高めた。
- 総合
  - 用意した2種類の検証方法について、検証にかかる時間を可変にするため処理回数を調節できるよう工夫した。
  - 変数の命名に気を使った。
  - Timeライブラリなどを用いた現在時刻の取得を利用して、ターゲットとなる処理にかかった時刻を計測する方法を学んだ。

# Result
検証中。

[![Tokei](https://tokei.rs/b1/github/matsuoka-601/numop)](https://github.com/matsuoka-601/numop)
# numop
数値計算のアルゴリズムを記述した、テストプログラム集。

- eigenvalue: 行列の固有値を求めるアルゴリズムのプログラム
	- ヤコビ法
		- 固有値を求めたい対称行列に対し、回転行列による相似変換を行うことで、固有値を求める
	- べき乗法
		- 初期値ベクトルに、固有値を求めたい行列をかけていくことで、絶対値最大の固有値を求める

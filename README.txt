I implemented the k-means clustering algorithm.
Program is written in python.
Steps of the algorithm are given below.
I used datasets given.

Data1 (Top 5 Rows)

0.89,6.35
5.79,12.47
5.43,11.14
5.75,2.20
9.15,0.14

Data2 (Top 5 Rows)

5.61,-6.63
-27.19,1.79
-2.78,8.84
-0.70,-8.99
0.59,-17.19

Training and Test Sets In the Iris dataset, each flower has 50 samples. Place the first 30 samples from each flower class into the training set and put the rest of the samples into the test set.

Iris_Test.csv
Iris_Train.csv

I applied k-NN algorithm to classify test samples. I try different k values.

The results are shown below :

Euclid	        k=1     Accuracy %: 96.67	 Error Count: 58/60
Manhattan	    k=1     Accuracy %: 96.67	 Error Count: 58/60
Euclid	        k=3     Accuracy %: 98.33	 Error Count: 59/60
Manhattan	    k=3     Accuracy %: 96.67	 Error Count: 58/60
Euclid	        k=5     Accuracy %: 98.33	 Error Count: 59/60
Manhattan	    k=5     Accuracy %: 95.0	 Error Count: 57/60
Euclid	        k=7     Accuracy %: 96.67	 Error Count: 58/60
Manhattan	    k=7     Accuracy %: 95.0	 Error Count: 57/60
Euclid	        k=9     Accuracy %: 96.67	 Error Count: 58/60
Manhattan	    k=9     Accuracy %: 96.67	 Error Count: 58/60
Euclid	        k=11    Accuracy %: 95.0	 Error Count: 57/60
Manhattan	    k=11    Accuracy %: 95.0	 Error Count: 57/60
Euclid	        k=15    Accuracy %: 95.0	 Error Count: 57/60
Manhattan	    k=15	Accuracy %: 95.0	 Error Count: 57/60

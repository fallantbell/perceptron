# perceptron(單層感知機)  
## 作法  
一開始會有一筆資料  
並且分成2群  
然後先初始感知機的向量(w)
二維的資料感知機也要是二維的  
三維的資料感知機也要是三維的 以此類推  
然後對感知機與各個資料內積  
內積>0 => 兩個向量趨近同方向  
內積<0 => 兩個向量趨近反方向  
剛好對應兩個資料群  
假設有兩個資料群A,B  
目標:w向量與資料群A同方向與資料群B反方向  
如果w向量與A內積<0 也就是反方向  
那就與目標不符  
所以要將w減去 學習率\*A的向量   
這樣就會不斷接近A向量  
![image](https://github.com/fallantbell/perceptron/blob/main/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-03-15%20204043.png)  
經過不斷的調整 就會找到能夠完整分開兩個資料群的向量  


## demo  
輸入訓練次數與學習率  
![image](https://github.com/fallantbell/perceptron/blob/main/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-03-15%20180156.png)  

訓練結果  
![image](https://github.com/fallantbell/perceptron/blob/main/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202021-03-15%20180344.png)  

project1_origin 為直接跑出結果  
project1_animation 則是會跑動畫  

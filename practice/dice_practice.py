import random
##dice_q 骰子數量 跑2~9的情況
for dice_q in range(2,9):
    ##重製滿足條件之次數
    sword_7,sword_6,sword_4,sword_3,bow_1,bow_2,bh_1=0,0,0,0,0,0,0
    ##執行x次數 取機率
    x=10000
    def dice(quan):
        for i in range(quan):
            dice_val=random.randint(0,5)
            result[dice_val]+=1

    for i in range (x):
        ##重製骰數
        result=[0,0,0,0,0,0]

        dice(dice_q)
        sword_qnty= result[0]*1+result[1]*2+result[2]*3
        bow_qnty = result[3]
        horse_qnty=result[4]

        ##判斷結果符合條件
        if sword_qnty >= 7:
            sword_7+=1
        if sword_qnty >= 6:
            sword_6+=1
        if sword_qnty >= 4:
            sword_4+=1
        if sword_qnty >= 3:
            sword_3+=1    
        if bow_qnty >= 1:
            bow_1+=1
        if bow_qnty >= 2:
            bow_2+=1
        if (bow_qnty >=1 and horse_qnty >=1):
            bh_1+=1

        #print結果
        # print ("[刀1, 刀2, 刀3, 弓, 馬, 名]")
        # print (result)
        # print ("刀數:" +str (sword_qnty ))
        # print ("弓數:" +str (bow_qnty ))
        # print ("馬數:" +str (horse_qnty ))

    print ("骰子數: "+str (dice_q))
    print ("刀7機率: "+str( round (sword_7/x,2)))
    print ("刀6機率: "+str( round (sword_6/x,2)))
    print ("刀4機率: "+str( round (sword_4/x,2)))
    print ("刀3機率: "+str( round (sword_3/x,2)))
    print ("弓1機率: "+str( round (bow_1  /x,2)))
    print ("弓2機率: "+str( round (bow_2  /x,2)))
    print ("弓1+馬1機率: "+str( round (bh_1  /x,2)))
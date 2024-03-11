from django.shortcuts import render

# Create your views here.
def Pulsar(request): 
    if (request.method=="POST"):
        data=request.POST
        Mean_Integrated=float(data.get('textMean_Integrated'))
        SD=float(data.get('textSD'))
        EK=float(data.get('textEK'))
        Skewness=float(data.get('textSkewness'))
        Mean_DMSNR_Curve=float(data.get('textMean_DMSNR_Curve'))
        SD_DMSNR_Curve=float(data.get('textSD_DMSNR_Curve'))
        EK_DMSNR_Curve=float(data.get('textEK_DMSNR_Curve'))
        Skewness_DMSNR_Curve=float(data.get('textSkewness_DMSNR_Curve'))
        
        if('buttonpredict' in request.POST):
            import pandas as pd
            data=pd.read_csv("csv/Pulsar.csv")
            #print(data)


            inputs=data.drop('Class',axis=1)
            outputs=data['Class']

            import sklearn
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test=train_test_split(inputs,outputs,test_size=0.5)
            #print(x_train)
            #print(x_test)
            #print(y_train)
            #print(y_test)

            from sklearn.naive_bayes import GaussianNB
            model=GaussianNB()
            model.fit(x_train,y_train)


            #print("accuracy:",model.score(inputs,outputs)*100)
            y_pred=model.predict([[103.015625,39.341649,0.323328,1.051164,3.121237,21.744669,7.735822,63.171909]])
            #print(y_pred)

            acc=model.score(inputs,outputs)
            #print(acc*100)


            result=model.predict([[Mean_Integrated,SD,EK,Skewness,Mean_DMSNR_Curve,SD_DMSNR_Curve,EK_DMSNR_Curve,Skewness_DMSNR_Curve]])

            if result == 0:
                finalResult = "It is not dispersion"
            elif result == 1:
                finalResult = "It is dispersion"


            return render(request,'index.html',context={'result':finalResult})   
    return render(request,'index.html')
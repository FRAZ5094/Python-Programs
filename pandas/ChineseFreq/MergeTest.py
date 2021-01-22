import pandas as pd 

Frame1=pd.DataFrame(data={"Word":["Hello","Hi","Goodbye"],"Use":["Greeting","Greeting","farewell"]})
Frame2=pd.DataFrame(data={"Word":["Hello","Hi","Burh"],"Frequency":[10,20,0]})
CombinedFrame=pd.merge(Frame1,Frame2, on="Word",how="left")
CombinedFrame=CombinedFrame.fillna(value=0)
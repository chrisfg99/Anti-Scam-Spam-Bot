#Candidate Number 184521
#University of Sussex

import pandas as pd

#Class for writing txt to csv
class Writer:

    def __init__(self):
        self=self
        self.headers=['Email Subject', 'Email Address', 'Email Body', 'Links', 'Tag',"Probabilties","Subject"]

    #function for writing to csv
    #t for tagged data file, c for classfying file
    def write(self,txt,file):
        if(file=='t'):
            #data = csv.writer(open('controller\tagged_data.csv', 'wb'))
            path='controller\tagged_data.csv'
        elif(file=='c'):
            #data = csv.writer(open('controller\email_data.csv', 'wb'))
            path='controller\email_data.csv'

        #print(msg[2])
        df=pd.DataFrame(txt)
        df.columns=(self.headers)
        df.to_csv(path)
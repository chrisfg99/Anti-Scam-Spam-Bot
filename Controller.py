#Candidate Number 184521
#University of Sussex

#class to control classifier and retriever

import time
#merge 2 following into same email file######
from Controller.Email.Retriever import Retriever
from Controller.Email.Sender import Sender
from Controller.PreProcessor.PreProcessor import PreProcessor
from Controller.Writer import Writer
from Controller.Classifier.Classifier import Classifier

#Controller class is in change of the running of the program on loop
class Controller:

    def __init__(self,retraining_data=0,testing=0):
        self.retraining_data=retraining_data
        self.testing=testing
        self.r=Retriever()
        self.p=PreProcessor()
        self.w=Writer()
        self.c=Classifier(retraining_data)
        self.s=Sender()
        print("__________________________________")
        print("Initialisation of Classes Complete")
        self.run()

    #function to keep the cycle of functions executing
    def run(self):
        #create a clock to keep track of refreshing emails
        running,toTrain=True,1
        while running==True:

            #get new messages from retriver    
            messages=self.r.openInbox()

            #if there are new messages send them to pre-processor
            if messages!=[]:
                cleanTxt,subjectvectors,bodyvectors=self.p.clean(messages)

                # add new messages to CSV for classifying
                #self.w.write(cleanTxt,'c')

                #train/retrain classifier
                if toTrain==1:
                    self.c.train()
                    toTrain=0

                print("New Messages have been preprocessed")
                print("__________________________________")
                print("       Classifier Results")

                # classify new messages
                taggedTxt=self.c.classify(cleanTxt,subjectvectors,bodyvectors)

                print("__________________________________")

                # add emails with tag to CSV for retraining and signal classifier to retrain
                if self.retraining_data==1:
                    self.w.write(taggedTxt,'t')
                    toTrain=1

                #send replies to the emails gotten
                if taggedTxt!=[]:
                    self.s.send(taggedTxt)

            #stop cycle running for testing
            if self.testing==1:
                running=False

            # check emails every 60 seconds
            time.sleep(60)
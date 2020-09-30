#input: Array(envelopes), int(percent)
#Functions:

    #__init__(self, envelopes, percent)

    # play:
        #uses the 4th strategy
        #output: an envelope

    #display:
        #output:(string)- explanation about the class"
class More_then_N_percent_group_strategy():

    def __init__(self, envelopes, percent):
        self.envelopes = envelopes
        self.percent = percent

    def play(self): # return the envelope with the highest amount of money using the 4th strategy
        openedEnv = 0
        highest_amount = self.envelopes[openedEnv].money
        openedEnv = 1
        absolute_Highest_Amount = 0
        while (percent * 100) > openedEnv :
            if self.envelopes[openedEnv].money > highest_amount:
                highest_amount = self.envelopes[openedEnv].money
                Env_To_Return = self.envelopes[openedEnv]
                envelopes[openedEnv - 1].used = True
                openedEnv = openedEnv + 1
        absolute_Highest_Amount = highest_amount
        while openedEnv < 100:
            if self.envelopes[openedEnv].money > absolute_Highest_Amount:
                absolute_Highest_Amount = self.envelopes[openedEnv].money
                Env_To_Return = self.envelopes[openedEnv]
                break
            self.envelopes[openedEnv].used = True
            openedEnv = openedEnv + 1
        return Env_To_Return
    def display(self):
        return(" opens x% of envelopes and chooses the envelope \n "
               "with the highest amount of money inside. then it \n "
               "compares the amount of money to the other 100% - x% \n "
               "of the envelopes and if a higher amount is found \n"
               "it will replace the envelope and immediately return the new envelope")




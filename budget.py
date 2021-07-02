class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        return None
    
    def deposit(self, amount, description=""):
        deposited = {"amount": amount, "description": description}
        self.ledger.append(deposited)
    
    def withdraw(self, amount, description=""):
        tf = self.check_funds(amount)
        if tf == True:
            withdrawn = {"amount": -amount, "description": description}
            self.ledger.append(withdrawn)
            return True
        else:
            return False
        
    def get_balance(self):
        if len(self.ledger)==0:
            balance=0
            return balance
        else:
            balance = 0
            led = self.ledger
            for i in range(len(led)):
                x = led[i]['amount']
                balance = balance+x
            return balance
            
    
    def transfer(self, amount, category):
        tf = self.check_funds(amount)
        if tf == True:
            w_desc = "Transfer to {dc}".format(dc=category.name)
            self.ledger.append({"amount": -amount,"description": w_desc})
            
            d_desc = "Transfer from {name}".format(name=self.name)
            category.ledger.append({"amount": amount,"description": d_desc})
            return True
        else:
            return False       
        
    
    def check_funds(self, amount):
        bal = self.get_balance()
        if amount <= bal:
            return True
        else:
            return False    
    
    def __repr__(self):
        i = 0
        farm = ""
        led = self.ledger
        while i < len(led):
            des = led[i]['description']
            des = des.ljust(23)
            des = des[:23]
            
            am = led[i]['amount']
            am = f'{am:.2f}'.rjust(7)
            farm = farm+des+am+'\n'
            i+=1
            
        bal = self.get_balance()
        txt = self.name.center(30,"*")
        txt = txt.center(30, "*")
        bal = "Total: "+ str(bal)
        ledger = txt+'\n'+farm+bal
        return ledger

def create_spend_chart(categories):    
    #while loop to go through the list
    i = 0
    length = list()
    total_withdraws = float()
    category_list = list()
    while i<len(categories):
        categories[i].name = (categories[i].name).title()
        ledger = categories[i].ledger
        withdraws = float()
        
        #for loop to extract all withdrawals
        for j in range(len(ledger)):
            if ledger[j]['amount']<0:
                withdraws+=ledger[j]['amount']
               
        #summing all withdrawals
        total_withdraws+=-withdraws
        length.append(len(categories[i].name))
        category_list.append(list([-withdraws,categories[i].name]))
        i+=1
    #getting maximum length
    max_length = max(length)
    #replacing value representations with o
    for i in range(len(category_list)):
        category_list[i][0] = ("o"*(int(category_list[i][0]/total_withdraws*10)+1)).rjust(11)
        category_list[i][1] = category_list[i][1].ljust(max_length+1)
        category_list[i] = '-'.join(category_list[i])
        
    #creating the spaces to separate each category
    space = list((" ,"*11).split(","))
    space.pop()
    space.append('-')
    space.extend((" ,"*(max_length)).split(","))
    space.pop()
    
    #appending list of each column to new category column
    i = 0
    category_list_new = []
    while i < len(category_list):
        ls = list(category_list[i])
        category_list_new.append(ls)
        i+=1
    
    #inserting first column and appending it
    for i in range(1):
        slash = list(('     ,'*(max_length)).split(','))
        slash.pop()
        per = ["100| "," 90| "," 80| ",' 70| ',' 60| ',' 50| ',' 40| ',' 30| ',' 20| ',' 10| ','  0| ', '    -']
        per.extend(slash)
        category_list_new.insert(0,per)
    
    #while loop to to insert the distinguishing spaces
    i = 0
    k = 2
    l = 3
    while (i<(len(category_list))):
        category_list_new.insert(k,space)
        category_list_new.insert(l,space)
        k+=3
        i+=1
        l+=3
    #final creation of the budget    
    length = len(category_list_new[i])
    ystr ="Percentage spent by category\n"
    for i in range(len(category_list_new[0])):
        for x in category_list_new:
            ystr=ystr+x[i]+''
        if i==(len(category_list_new[0])-1):
            break
        ystr+="\n"
    return ystr
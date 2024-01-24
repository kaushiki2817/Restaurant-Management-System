
# coding: utf-8

# In[ ]:


class RMS:
    def __init__(self,restaurant_name,menu):
        self.total_bill=0
        self.menu=menu
        self.restaurant_name=restaurant_name
    def welcome_user(self):
        #welcome the user
        print("Welcome to our", self.restaurant_name,"Restaurant!")
    def display_menu(self):
        #display the menu
        print("MENU:")
        for i in self.menu:
            print(i.title(),":",self.menu[i])
        print('*'*30)
    def take_order(self):  
        
        #take order
        self.order=input("Please enter the item to order:")
    def preparation(self):
        
        #prepare the order
        print("Hooray! You've ordered!!",self.order)
        import time
        print("Cooking up your masterpiece....")
        time.sleep(3)
        self.item_price = int(self.menu[self.order.lower()])
        self.total_bill += self.item_price
    def serve_order(self):
        #serve the order
        print("Here is your",self.order.lower())
    def display_bill(self): 
        
        #display the bill
        print("Total Bill: ",self.total_bill)
    def verify_bill(self):
        
        #verify the bill
        self.amount_paid=float(input("Please enter amount here: "))
        while self.amount_paid<self.total_bill:
              self.total_bill=self.total_bill-self.amount_paid
              print("Payment insufficient. Please pay remaining",self.total_bill)
              self.amount_paid=float(input("Please enter amount here: "))
        if self.amount_paid>self.total_bill:
              self.change=self.amount_paid-self.total_bill
              print("Payment Successful!! Your change is: ",self.change)
              print("Thankyou for your Order! Enjoy your meal.")
        else:
              print("Thankyou for your Order! Enjoy your meal.")
    def thank_user(self):
        #thank the user
        print("Thank you for bringing your awesome vibes to our restaurant!!")
    def order_process(self):
        self.take_order()
        if self.order.lower() in self.menu:
              self.preparation()
              self.serve_order()
              self.user_repeat=input("Would you like to order again?")
              while self.user_repeat.lower()=="yes":
                  self.repeat_order()
                  self.user_repeat=input("Would you like to order again?")
              self.display_bill()
              self.verify_bill()
              self.thank_user()
        else:
              print("Invalid Input")
              self.order_process()


    def repeat_order(self):
        self.take_order()
        if self.order.lower() in menu:
            self.preparation()
            self.serve_order()
        else:
            print("Invalid Input")
            self.repeat_order()


          
          


if __name__=='__main__':
    
    file=open("RMS input file.txt","r")

    restaurant_name=file.readline().replace('\n','')
    food_items=file.readline().replace('\n','').split(',')

    item_price=file.readline().replace('\n','').split(',')

    menu=dict(zip(food_items,item_price))
    
    restaurant_system=(RMS(restaurant_name,menu))
    
    




    import tkinter as tk
    #main window
    window=tk.Tk()
    #change title
    window.title("Restaurant Management System")
    #window size
    window.geometry("400x400")
    #Label
    tk.Label(window,text=restaurant_name,font=("Eras Bold ITC",25)).place(x=200,y=60,anchor='center')
    #SubLabel
    tk.Button(window,text="MENU",font=("Times",10),width=23,height=2,command=restaurant_system.display_menu).place(x=120,y=115)
    #Button
    tk.Button(window,text="ORDER",font=("helvtica",10),width=20,height=2,command=restaurant_system.order_process).place(x=120,y=200)
    #Main Window
    window.mainloop()


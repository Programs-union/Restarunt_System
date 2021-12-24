import os
from tkinter import *
from tkinter import messagebox
import random


class System_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x700+0+0')
        self.root.title('Restarunt System')
        bg_color = '#091833'            # #074463
        title = Label(self.root, text='Restarunt System', font=('times new roman', 30, 'bold'), bd=12,
                      relief=GROOVE, pady=2, bg=bg_color, fg='yellow').pack(fill=X)

        # *********** variabels *******
        # *********** food ************
        self.Burger = IntVar()
        self.Pizza = IntVar()
        self.Spaghetti = IntVar()
        self.Chicken_Naggets = IntVar()
        self.Mexican_Tacos = IntVar()
        self.Hotdog = IntVar()

        # *********** drinks **********
        self.apple = IntVar()
        self.Orange = IntVar()
        self.Mango = IntVar()
        self.Lemonade = IntVar()
        self.Coffe = IntVar()
        self.Cold_Drinks = IntVar()

        # *********** dessert **********
        self.ice_cream = IntVar()
        self.Molten_Cake = IntVar()
        self.Apple_Pie = IntVar()
        self.Cheese_Cake = IntVar()
        self.Waffles = IntVar()
        self.Cookies = IntVar()

        # *********** appetizers **********
        self.Salad = IntVar()
        self.French_Fries = IntVar()
        self.Soup = IntVar()
        self.Onion_Rings = IntVar()
        self.Chicken_Wings = IntVar()
        self.Cole_Slaw = IntVar()

        # *********** total price **********
        self.food_price = StringVar()
        self.drinks_price = StringVar()
        self.desert_price = StringVar()
        self.appetizers_price = StringVar()
        self.sub_total_cost = StringVar()
        self.service_tax = StringVar()
        self.total_cost = StringVar()

        # *********** customer **********
        self.C_name = StringVar()
        self.C_phone = StringVar()
        self.bill_no = StringVar()
        self.search_bill = StringVar()
        bill = random.randint(1000,9999)
        self.bill_no.set(bill)

        # *********** Customar Detail Frame *********
        Lb1 = LabelFrame(root,text='Customer Details', font=('times new roman', 18, 'bold') ,bd=10,
                      relief=GROOVE, pady=2, bg=bg_color, fg='gold')
        Lb1.place(x=0, y=70, relwidth=1)

        C_name_Lb = Label(Lb1, text='Customar Name', font=('times new roman', 18 ,'bold'),bg=bg_color, fg='white')
        C_name_Lb.grid(row=0, column=0, padx=20, pady=5)
        C_name_txt = Entry(Lb1, width=15, font=('arial', 15), bd=7, relief=SUNKEN, textvariable=self.C_name).grid(row=0, column=1, padx=10, pady=5)

        C_phone_Lb = Label(Lb1, text='Phone No.', font=('times new roman', 18 ,'bold'),bg=bg_color, fg='white')
        C_phone_Lb.grid(row=0, column=2, padx=20, pady=5)
        C_phone_txt = Entry(Lb1, width=15, font=('arial', 15), bd=7, relief=SUNKEN, textvariable=self.C_phone).grid(row=0, column=3, padx=10, pady=5)

        C_Bill_Lb = Label(Lb1, text='Order Number', font=('times new roman', 18 ,'bold'),bg=bg_color, fg='white')
        C_Bill_Lb.grid(row=0, column=4, padx=20, pady=5)
        C_Bill_txt = Entry(Lb1, width=15, font=('arial', 15), bd=7, relief=SUNKEN, textvariable=self.search_bill).grid(row=0, column=5, padx=10, pady=5)

        Bill_button = Button(Lb1,width=10, text='search', bd=7, font=('arial', 12, 'bold'), command=self.Find_Bill).grid(row=0, column=6, padx=10, pady=5)

        # *********** food Frame *********
        Lb2 = LabelFrame(root, text='Food', font=('times new roman', 18, 'bold'), bd=10,
                         relief=GROOVE, pady=2, bg=bg_color, fg='gold')
        Lb2.place(x=0, y=160, width=290, height=380)

        Burger_Lb = Label(Lb2, text='Burger', font=('times new roman', 16 ,'bold'),bg=bg_color, fg='white')
        Burger_Lb.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        Burger_txt = Entry(Lb2, width=6, font=('times new roman', 16 ,'bold'), bd=5, relief=SUNKEN, textvariable=self.Burger)\
            .grid(row=0, column=1, padx=10, pady=10)

        Pizza_Lb = Label(Lb2, text='Pizza', font=('times new roman', 16 ,'bold'),bg=bg_color, fg='white')
        Pizza_Lb.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        Pizza_txt = Entry(Lb2, width=6, font=('times new roman', 16 ,'bold'), bd=5, relief=SUNKEN, textvariable=self.Pizza)\
            .grid(row=1, column=1, padx=10, pady=10)

        Spaghetti_Lb = Label(Lb2, text='Spaghetti', font=('times new roman', 16 ,'bold'),bg=bg_color, fg='white')
        Spaghetti_Lb.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        Spaghetti_txt = Entry(Lb2, width=6, font=('times new roman', 16 ,'bold'), bd=5, relief=SUNKEN, textvariable=self.Spaghetti)\
            .grid(row=2, column=1, padx=10, pady=10)

        Chicken_Naggets_Lb = Label(Lb2, text='Chicken Naggets', font=('times new roman', 16 ,'bold'),bg=bg_color, fg='white')
        Chicken_Naggets_Lb.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        Chicken_Naggets_txt = Entry(Lb2, width=6, font=('times new roman', 16 ,'bold'), bd=5, relief=SUNKEN, textvariable=self.Chicken_Naggets)\
            .grid(row=3, column=1, padx=10, pady=10)

        Mexican_Tacos_Lb = Label(Lb2, text='Mexican Tacos', font=('times new roman', 16 ,'bold'),bg=bg_color, fg='white')
        Mexican_Tacos_Lb.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        Mexican_Tacos_txt = Entry(Lb2, width=6, font=('times new roman', 16 ,'bold'), bd=5, relief=SUNKEN, textvariable=self.Mexican_Tacos)\
            .grid(row=4, column=1, padx=10, pady=10)

        Hotdog_Lb = Label(Lb2, text='Hotdog', font=('times new roman', 16 ,'bold'),bg=bg_color, fg='white')
        Hotdog_Lb.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        Hotdog_txt = Entry(Lb2, width=6, font=('times new roman', 16 ,'bold'), bd=5, relief=SUNKEN, textvariable=self.Hotdog)\
            .grid(row=5, column=1, padx=10, pady=10)

        # *********** drinks Frame *********
        Lb3 = LabelFrame(root, text='Drinks', font=('times new roman', 18, 'bold'), bd=10,
                         relief=GROOVE, pady=2, bg=bg_color, fg='gold')
        Lb3.place(x=290, y=160, width=260, height=380)

        apple_Lb = Label(Lb3, text='Apple Juice', font=('times new roman', 16, 'bold'), bg=bg_color, fg='white')
        apple_Lb.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        apple_txt = Entry(Lb3, width=6, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, textvariable=self.apple)\
            .grid(row=0, column=1,padx=10,pady=10)

        Orange_Lb = Label(Lb3, text='Orange Juice', font=('times new roman', 16, 'bold'), bg=bg_color, fg='white')
        Orange_Lb.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        Orange_txt = Entry(Lb3, width=6, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, textvariable=self.Orange)\
            .grid(row=1, column=1,padx=10,pady=10)

        Mango_Lb = Label(Lb3, text='Mango Juice', font=('times new roman', 16, 'bold'), bg=bg_color, fg='white')
        Mango_Lb.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        Mango_txt = Entry(Lb3, width=6, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, textvariable=self.Mango)\
            .grid(row=2, column=1,padx=10,pady=10)

        Lemonade_Lb = Label(Lb3, text='Lemonade', font=('times new roman', 16, 'bold'), bg=bg_color, fg='white')
        Lemonade_Lb.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        Lemonade_txt = Entry(Lb3, width=6, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, textvariable=self.Lemonade)\
            .grid(row=3, column=1,padx=10,pady=10)

        Coffe_Lb = Label(Lb3, text='Coffe', font=('times new roman', 16, 'bold'), bg=bg_color, fg='white')
        Coffe_Lb.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        Coffe_txt = Entry(Lb3, width=6, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, textvariable=self.Coffe)\
            .grid(row=4, column=1,padx=10,pady=10)

        Cold_Drinks_Lb = Label(Lb3, text='Cold Drinks', font=('times new roman', 16, 'bold'), bg=bg_color, fg='white')
        Cold_Drinks_Lb.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        Cold_Drinks_txt = Entry(Lb3, width=6, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, textvariable=self.Cold_Drinks)\
            .grid(row=5, column=1,padx=10,pady=10)

        # *********** desert Frame *********
        Lb4 = LabelFrame(root, text='Desert', font=('times new roman', 18, 'bold'), bd=10,
                         relief=GROOVE, pady=2, bg=bg_color, fg='gold')
        Lb4.place(x=550, y=160, width=255, height=380)

        ice_cream_Lb = Label(Lb4, text='Ice Cream', font=('times new roman', 16, 'bold'), bg=bg_color, fg='white')
        ice_cream_Lb.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        ice_cream_txt = Entry(Lb4, width=6, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, textvariable=self.ice_cream)\
            .grid(row=0, column=1, padx=10, pady=10)

        Molten_Cake_Lb = Label(Lb4, text='Molten Cake', font=('times new roman', 16, 'bold'), bg=bg_color, fg='white')
        Molten_Cake_Lb.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        Molten_Cake_txt = Entry(Lb4, width=6, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, textvariable=self.Molten_Cake)\
            .grid(row=1, column=1, padx=10, pady=10)

        Apple_Pie_Lb = Label(Lb4, text='Apple Pie', font=('times new roman', 16, 'bold'), bg=bg_color, fg='white')
        Apple_Pie_Lb.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        Apple_Pie_txt = Entry(Lb4, width=6, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, textvariable=self.Apple_Pie)\
            .grid(row=2, column=1, padx=10, pady=10)

        Cheese_Cake_Lb = Label(Lb4, text='Cheese Cake', font=('times new roman', 16, 'bold'), bg=bg_color, fg='white')
        Cheese_Cake_Lb.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        Cheese_Cake_txt = Entry(Lb4, width=6, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, textvariable=self.Cheese_Cake)\
            .grid(row=3, column=1, padx=10, pady=10)

        Waffles_Lb = Label(Lb4, text='Waffles', font=('times new roman', 16, 'bold'), bg=bg_color, fg='white')
        Waffles_Lb.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        Waffles_txt = Entry(Lb4, width=6, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, textvariable=self.Waffles)\
            .grid(row=4, column=1, padx=10, pady=10)

        Cookies_Lb = Label(Lb4, text='Cookies', font=('times new roman', 16, 'bold'), bg=bg_color, fg='white')
        Cookies_Lb.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        Cookies_txt = Entry(Lb4, width=6, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, textvariable=self.Cookies)\
            .grid(row=5, column=1, padx=10, pady=10)


        # *********** appetizers Frame *********
        Lb7 = LabelFrame(root, text='Appetizers', font=('times new roman', 18, 'bold'), bd=10,
                         relief=GROOVE, pady=2, bg=bg_color, fg='gold')
        Lb7.place(x=805, y=160, width=260, height=380)

        Salad_Lb = Label(Lb7, text='Salad', font=('times new roman', 16, 'bold'), bg=bg_color, fg='white')
        Salad_Lb.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        Salad_txt = Entry(Lb7, width=5, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, textvariable=self.Salad)\
            .grid(row=0, column=1, padx=5, pady=10)

        French_Fries_Lb = Label(Lb7, text='French Fries', font=('times new roman', 16, 'bold'), bg=bg_color, fg='white')
        French_Fries_Lb.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        French_Fries_txt = Entry(Lb7, width=5, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, textvariable=self.French_Fries)\
            .grid(row=1, column=1, padx=5, pady=10)

        Soup_Lb = Label(Lb7, text='Soup', font=('times new roman', 16, 'bold'), bg=bg_color, fg='white')
        Soup_Lb.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        Soup_txt = Entry(Lb7, width=5, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, textvariable=self.Soup)\
            .grid(row=2, column=1, padx=5, pady=10)

        Onion_Rings_Lb = Label(Lb7, text='Onion Rings', font=('times new roman', 16, 'bold'), bg=bg_color, fg='white')
        Onion_Rings_Lb.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        Onion_Rings_txt = Entry(Lb7, width=5, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, textvariable=self.Onion_Rings)\
            .grid(row=3, column=1, padx=5, pady=10)

        Chicken_Wings_Lb = Label(Lb7, text='Chicken Wings', font=('times new roman', 16, 'bold'), bg=bg_color, fg='white')
        Chicken_Wings_Lb.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        Chicken_Wings_txt = Entry(Lb7, width=5, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, textvariable=self.Chicken_Wings)\
            .grid(row=4, column=1, padx=5, pady=10)

        Cole_Slaw_Lb = Label(Lb7, text='Cole Slaw', font=('times new roman', 16, 'bold'), bg=bg_color, fg='white')
        Cole_Slaw_Lb.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        Cole_Slaw_txt = Entry(Lb7, width=5, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN, textvariable=self.Cole_Slaw)\
            .grid(row=5, column=1, padx=5, pady=10)


        # *********** Bill Area *********
        Lb5 = Frame(root, bd=10,relief=GROOVE,bg=bg_color)
        Lb5.place(x=1065, y=160, width=300, height=380)

        Bill_title = Label(Lb5, text='Order Area', font=('times new roman', 18, 'bold'), bd=7,bg=bg_color,fg='gold', relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(Lb5, orient=VERTICAL)
        self.textarea = Text(Lb5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # *********** Button Frame *********
        Lb6 = LabelFrame(root, bd=10, relief=GROOVE,bg=bg_color, font=('times new roman', 18, 'bold'), text='Order Menu', fg='gold')
        Lb6.place(x=0, y=540, relwidth=1, height=160)

        food = Label(Lb6, text='Total Food Cost', font=('arial', 14, 'bold'), fg='white',bg=bg_color)\
            .grid(row=0, column=0, sticky='w', padx=20, pady=1)
        food_txt = Entry(Lb6, width=15, font=('arial', 14, 'bold'), bd=7, relief=SUNKEN, textvariable=self.food_price)\
            .grid(row=0, column=1, padx=10, pady=1)

        drinks = Label(Lb6, text='Total Drinks Cost', font=('arial', 14, 'bold'), fg='white',bg=bg_color)\
            .grid(row=1, column=0, sticky='w', padx=20, pady=1)
        drinks_txt = Entry(Lb6, width=15, font=('arial', 14, 'bold'), bd=7, relief=SUNKEN, textvariable=self.drinks_price)\
            .grid(row=1, column=1, padx=10, pady=1)

        desert = Label(Lb6, text='Total Desert Cost', font=('arial', 14, 'bold'), fg='white',bg=bg_color)\
            .grid(row=2, column=0, sticky='w', padx=20, pady=1)
        desert_txt = Entry(Lb6, width=15, font=('arial', 14, 'bold'), bd=7, relief=SUNKEN, textvariable=self.desert_price)\
            .grid(row=2, column=1, padx=10, pady=1)

        sub_total = Label(Lb6, text='Sub Total', font=('arial', 14, 'bold'), fg='white',bg=bg_color)\
            .grid(row=0, column=2, sticky='w', padx=20, pady=1)
        sub_total_txt = Entry(Lb6, width=15, font=('arial', 14, 'bold'), bd=7, relief=SUNKEN, textvariable=self.sub_total_cost)\
            .grid(row=0, column=3, padx=10, pady=1)

        service = Label(Lb6, text='Service', font=('arial', 14, 'bold'), fg='white',bg=bg_color)\
            .grid(row=1, column=2, sticky='w', padx=20, pady=1)
        service_txt = Entry(Lb6, width=15, font=('arial', 14, 'bold'), bd=7, relief=SUNKEN, textvariable=self.service_tax)\
            .grid(row=1, column=3, padx=10, pady=1)

        total = Label(Lb6, text='Total Cost', font=('arial', 14, 'bold'), fg='white',bg=bg_color)\
            .grid(row=2, column=2, sticky='w', padx=20, pady=1)
        total_txt = Entry(Lb6, width=15, font=('arial', 14, 'bold'), bd=7, relief=SUNKEN, textvariable=self.total_cost)\
            .grid(row=2, column=3, padx=10, pady=1)

        # ******** botton frame ********
        btn_fr = Frame(Lb6, bd=7, relief=GROOVE)
        btn_fr.place(x=750, width=572, height=115)

        total_btn = Button(btn_fr, text='Total', bg='cadetblue', fg='white', bd=7, pady=25, width=10, command=self.Total,
                           font=(('times new roman'), 15, 'bold')).grid(row=0, column=0, padx=0, pady=5)

        recipt_btn = Button(btn_fr, text='Recipt', bg='cadetblue', fg='white', bd=7, pady=25, width=10,
                        font=(('times new roman'), 15, 'bold'), command=self.bill_area).grid(row=0, column=1, padx=0, pady=5)

        # exit
        save_btn = Button(btn_fr, text='Save', bg='cadetblue', fg='white', bd=7, pady=25, width=10,command=self.Save,
                          font=(('times new roman'), 15, 'bold')).grid(row=0, column=2, padx=0, pady=5)

        reset_btn = Button(btn_fr, text='Reset', bg='cadetblue', fg='white', bd=7, pady=25, command=self.Reset
                           , width=10, font=(('times new roman'), 15, 'bold')).grid(row=0, column=3, padx=0, pady=5)

        # self.welcome()

    def Total(self):
        self.f_Burger_p = self.Burger.get()*70
        self.f_Pizza_p = self.Pizza.get()*60
        self.f_Spaghetti_p = self.Spaghetti.get()*50
        self.f_Chicken_Naggets_p = self.Chicken_Naggets.get()*40
        self.f_Mexican_Tacos_p = self.Mexican_Tacos.get()*45
        self.f_Hotdog_p = self.Hotdog.get()*45
        self.total_food_price = float(self.f_Burger_p + self.f_Pizza_p + self.f_Spaghetti_p +
                                      self.f_Chicken_Naggets_p + self.f_Mexican_Tacos_p + self.f_Hotdog_p)
        self.food_price.set(str(self.total_food_price) + ' EP')

        self.dr_apple_p = self.apple.get()*30
        self.dr_Orange_p = self.Orange.get()*30
        self.dr_Mango_p = self.Mango.get()*40
        self.dr_Lemonade_p = self.Lemonade.get()*30
        self.dr_Coffe_p = self.Coffe.get()*35
        self.dr_Cold_Drinks_p = self.Cold_Drinks.get()*25
        self.total_drinks_price = float(self.dr_apple_p + self.dr_Orange_p + self.dr_Mango_p +
                                        self.dr_Lemonade_p + self.dr_Coffe_p + self.dr_Cold_Drinks_p)
        self.drinks_price.set(str(self.total_drinks_price) + ' EP')

        self.ds_ice_cream_p = self.ice_cream.get()*20
        self.ds_Molten_Cake_p = self.Molten_Cake.get()*30
        self.ds_Apple_Pie_p = self.Apple_Pie.get()*25
        self.ds_Cheese_Cake_p = self.Cheese_Cake.get()*35
        self.ds_Waffles_p = self.Waffles.get()*30
        self.ds_Cookies_p = self.Cookies.get()*20
        self.total_desert_price = float(self.ds_ice_cream_p + self.ds_Molten_Cake_p + self.ds_Apple_Pie_p +
                                        self.ds_Cheese_Cake_p + self.ds_Waffles_p + self.ds_Cookies_p)
        self.desert_price.set(str(self.total_desert_price) + ' EP')

        self.a_Salad_p = self.Salad.get()*20
        self.a_French_Fries_p = self.French_Fries.get()*20
        self.a_Soup_p = self.Soup.get()*25
        self.a_Onion_Rings_p = self.Onion_Rings.get()*25
        self.a_Chicken_Wings_p = self.Chicken_Wings.get()*35
        self.a_Cole_Slaw_p = self.Cole_Slaw.get()*15
        self.total_appetizers_price = float(self.a_Salad_p + self.a_French_Fries_p + self.a_Soup_p +
                                        self.a_Onion_Rings_p + self.a_Chicken_Wings_p + self.a_Cole_Slaw_p)
        self.appetizers_price.set(str(self.total_appetizers_price) + ' EP')

        self.sub_total = float(self.total_food_price + self.total_drinks_price + self.total_desert_price
                               + self.total_appetizers_price)
        self.sub_total_cost.set(str(self.sub_total) + ' EP')
        self.total_service = float(self.sub_total * 0.15)
        self.service_tax.set(str(self.total_service) + ' EP')
        self.total_price = float(self.sub_total + self.total_service)
        self.total_cost.set(str(self.total_price) + ' EP')

    def Recipt(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, '\twelcome to bill\n\n')
        self.textarea.insert(END, f' Bill Number : {self.bill_no.get()}\n')
        self.textarea.insert(END, f' Customar Name : {self.C_name.get()}\n')
        self.textarea.insert(END, f' Phone Number : {self.C_phone.get()}\n')
        self.textarea.insert(END, '*'*32+'\n')
        if self.sub_total != 0.0:
            self.textarea.insert(END, f' item\t\tQTY\tprice\n')
            self.textarea.insert(END, '*' * 32 + '\n')

    def bill_area(self):
        if self.C_name.get() == '':
            messagebox.showerror('Error','Please,Enter customar name')
        elif self.C_phone.get() == '':
            messagebox.showerror('Error','Please,Enter customar phone number')
        elif self.sub_total_cost.get() == '0.0 EP':
            messagebox.showerror('Error', 'Sorry,No item chossen')

        else:
            self.Recipt()

            if self.Burger.get() != 0:
                self.textarea.insert(END, f' Burger \t\t{self.Burger.get()}\t{self.f_Burger_p}\n')
            if self.Pizza.get() != 0:
                self.textarea.insert(END, f' Pizza \t\t{self.Pizza.get()}\t{self.f_Pizza_p}\n')
            if self.Spaghetti.get() != 0:
                self.textarea.insert(END, f' Spaghetti \t\t{self.Spaghetti.get()}\t{self.f_Spaghetti_p}\n')
            if self.Chicken_Naggets.get() != 0:
                self.textarea.insert(END, f' Chicken Naggets \t\t{self.Chicken_Naggets.get()}\t{self.f_Chicken_Naggets_p}\n')
            if self.Mexican_Tacos.get() != 0:
                self.textarea.insert(END, f' Mexican Tacos \t\t{self.Mexican_Tacos.get()}\t{self.f_Mexican_Tacos_p}\n')
            if self.Hotdog.get() != 0:
                self.textarea.insert(END, f' Hotdog \t\t{self.Hotdog.get()}\t{self.f_Hotdog_p}\n')


            if self.apple.get() != 0:
                self.textarea.insert(END, f' Apple Juice \t\t{self.apple.get()}\t{self.dr_apple_p}\n')
            if self.Orange.get() != 0:
                self.textarea.insert(END, f' Orange Juice \t\t{self.Pizza.get()}\t{self.dr_Orange_p}\n')
            if self.Mango.get() != 0:
                self.textarea.insert(END, f' Mango Juice \t\t{self.Spaghetti.get()}\t{self.dr_Mango_p}\n')
            if self.Lemonade.get() != 0:
                self.textarea.insert(END, f' Lemonade \t\t{self.Lemonade.get()}\t{self.dr_Lemonade_p}\n')
            if self.Coffe.get() != 0:
                self.textarea.insert(END, f' Coffe \t\t{self.Coffe.get()}\t{self.dr_Coffe_p}\n')
            if self.Cold_Drinks.get() != 0:
                self.textarea.insert(END, f' Cold Drinks \t\t{self.Cold_Drinks.get()}\t{self.dr_Cold_Drinks_p}\n')

            if self.ice_cream.get() != 0:
                self.textarea.insert(END, f' Ice cream \t\t{self.ice_cream.get()}\t{self.ds_ice_cream_p}\n')
            if self.Molten_Cake.get() != 0:
                self.textarea.insert(END, f' Molten Cake \t\t{self.Molten_Cake.get()}\t{self.ds_Molten_Cake_p}\n')
            if self.Apple_Pie.get() != 0:
                self.textarea.insert(END, f' Apple Pie \t\t{self.Apple_Pie.get()}\t{self.ds_Apple_Pie_p}\n')
            if self.Cheese_Cake.get() != 0:
                self.textarea.insert(END, f' Cheese Cake \t\t{self.Cheese_Cake.get()}\t{self.ds_Cheese_Cake_p}\n')
            if self.Waffles.get() != 0:
                self.textarea.insert(END, f' Waffles \t\t{self.Waffles.get()}\t{self.ds_Waffles_p}\n')
            if self.Cookies.get() != 0:
                self.textarea.insert(END, f' Cookies \t\t{self.Cookies.get()}\t{self.ds_Cookies_p}\n')

            if self.Salad.get() != 0:
                self.textarea.insert(END, f' Salad \t\t{self.Salad.get()}\t{self.a_Salad_p}\n')
            if self.French_Fries.get() != 0:
                self.textarea.insert(END, f' French Fries \t\t{self.French_Fries.get()}\t{self.a_French_Fries_p}\n')
            if self.Soup.get() != 0:
                self.textarea.insert(END, f' Soup \t\t{self.Soup.get()}\t{self.a_Soup_p}\n')
            if self.Onion_Rings.get() != 0:
                self.textarea.insert(END, f' Onion Rings \t\t{self.Onion_Rings.get()}\t{self.a_Onion_Rings_p}\n')
            if self.Chicken_Wings.get() != 0:
                self.textarea.insert(END, f' Chicken Wings \t\t{self.Chicken_Wings.get()}\t{self.a_Chicken_Wings_p}\n')
            if self.Cole_Slaw.get() != 0:
                self.textarea.insert(END, f' Cole Slaw \t\t{self.Cole_Slaw.get()}\t{self.a_Cole_Slaw_p}\n')

            if self.sub_total != 0.0:
                self.textarea.insert(END, '*' * 32 + '\n')
                self.textarea.insert(END, f' Sub Total  \t\t\t{self.sub_total_cost.get()}\n')
            if self.total_service != 0.0:
                self.textarea.insert(END, f' Service tax  \t\t\t{self.service_tax.get()}\n')
            if self.total_price != 0.0:
                self.textarea.insert(END, f' Total Cost  \t\t\t{self.total_cost.get()}\n')
                self.textarea.insert(END, '*' * 32 + '\n')

    def Save(self):
        op = messagebox.askyesno('Save Bill','Do you want to save this order ?')
        if op > 0 :
            self.bill_data = self.textarea.get('1.0', END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo('Save', f'Order no. {self.bill_no.get()} saved successfully')
        else:
            return

    def Find_Bill(self):
        present = 'no'
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open("bills/" + i, "r")
                self.textarea.delete('1.0', END)
                for j in f1:
                    self.textarea.insert(END, j)
                f1.close()
                present = 'yes'
        if present == 'no':
            messagebox.showerror('Error','Invalid order No.')

    def Reset(self):
        op = messagebox.askyesno('Exit', 'Do you really want to reset ?')
        if op > 0:
            self.Burger.set(0)
            self.Pizza.set(0)
            self.Spaghetti.set(0)
            self.Chicken_Naggets.set(0)
            self.Mexican_Tacos.set(0)
            self.Hotdog.set(0)

            # *********** drinks **********
            self.apple.set(0)
            self.Orange.set(0)
            self.Mango.set(0)
            self.Lemonade.set(0)
            self.Coffe.set(0)
            self.Cold_Drinks.set(0)

            # *********** dessert **********
            self.ice_cream.set(0)
            self.Molten_Cake.set(0)
            self.Apple_Pie.set(0)
            self.Cheese_Cake.set(0)
            self.Waffles.set(0)
            self.Cookies.set(0)

            # *********** appetizers **********
            self.Salad.set(0)
            self.French_Fries.set(0)
            self.Soup.set(0)
            self.Onion_Rings.set(0)
            self.Chicken_Wings.set(0)
            self.Cole_Slaw.set(0)

            # *********** total price **********
            self.food_price.set('')
            self.drinks_price.set('')
            self.desert_price.set('')
            self.sub_total_cost.set('')
            self.service_tax.set('')
            self.total_cost.set('')

            # *********** customer **********
            self.C_name.set('')
            self.C_phone.set('')
            self.bill_no.set('')
            self.search_bill.set('')
            bill = random.randint(1000, 9999)
            self.bill_no.set(bill)
            self.Recipt()

            # self.textarea.delete('1.0',END)

    def Exit(self):
        op = messagebox.askyesno('Exit', 'Do you really want to exit ?')
        if op > 0:
            self.root.destroy()


restarunt = Tk()
system = System_App(restarunt)

restarunt.mainloop()

from tkinter import *
import tkinter as tk
import sqlite3
from PIL import ImageTk, Image


def login_as_manager():
    global manager_window
    manager_window = Tk()
    manager_window.title("Online Bookstore/Manager")
    manager_window.iconbitmap("Itzikgur-My-Seven-Books-1.ico")
    
    if username.get()=="lib_manager" and password.get()=="employee3003":
    
        title_label = Label(manager_window, text="Successfully logged in as the manager of the book-shop!",font=("Times",20,"bold"))
        title_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20,ipadx=100)
        
        add_rec_button = Button(manager_window, text="Add new record",command=add_record_window)
        add_rec_button.grid(row=1,column=0,padx=15,pady=5)
        
        show_rec_button = Button(manager_window, text="Show inventory",command=show_record_window)
        show_rec_button.grid(row=1,column=1,padx=15,pady=5)
        
        delete_rec_button = Button(manager_window, text="Delete a record",command=delete_record_window)
        delete_rec_button.grid(row=2,column=0,padx=15,pady=5)
        
        update_rec_button = Button(manager_window, text="Update a record",command=update_record_window)
        update_rec_button.grid(row=2,column=1,padx=15,pady=5)
        
        show_req_button = Button(manager_window, text="Show request fields",command=show_request)
        show_req_button.grid(row=3,column=0,padx=15,pady=5)
        
        
        
        close_btn_manager = Button(manager_window,text="Close",command=manager_window.destroy)
        close_btn_manager.grid(row=4,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
        
    else:
        title_label = Label(manager_window, text="ERROR, INVALID USERNAME OR PASSWORD!!",font=("Times",16,"bold"))
        title_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20,ipadx=100)
        
        close_btn_login = Button(manager_window,text="Close",command=manager_window.destroy)
        close_btn_login.grid(row=3,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
    
    
    
    
    
def login_as_owner():
    global owner_window
    owner_window = Tk()
    owner_window.title("Online Bookstore/Owner")
    owner_window.iconbitmap("Itzikgur-My-Seven-Books-1.ico")
    
    if username.get()=="lib_owner" and password.get()=="employee3003":
        
        title_label = Label(owner_window, text="Successfully logged in as the owner of the book-shop!",font=("Times",20,"bold"))
        title_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20,ipadx=100)
        
        add_rec_button = Button(owner_window, text="Add new record",command=add_record_window)
        add_rec_button.grid(row=1,column=0,padx=15,pady=5)
        
        show_rec_button = Button(owner_window, text="Show inventory",command=show_record_window)
        show_rec_button.grid(row=1,column=1,padx=15,pady=5)
        
        delete_rec_button = Button(owner_window, text="Delete a record",command=delete_record_window)
        delete_rec_button.grid(row=2,column=0,padx=15,pady=5)
        
        update_rec_button = Button(owner_window, text="Update a record",command=update_record_window)
        update_rec_button.grid(row=2,column=1,padx=15,pady=5)
        
        show_req_button = Button(owner_window, text="Show request fields",command=show_request)
        show_req_button.grid(row=3,column=0,padx=15,pady=5)
        
        
        
        close_btn_owner = Button(owner_window,text="Close",command=owner_window.destroy)
        close_btn_owner.grid(row=4,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
        
    else:
        title_label = Label(owner_window, text="ERROR, INVALID USERNAME OR PASSWORD!!",font=("Times",16,"bold"))
        title_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20,ipadx=100)
        
        close_btn_login = Button(owner_window,text="Close",command=owner_window.destroy)
        close_btn_login.grid(row=3,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
    
    
    
    

def login_as_sales_clerk():
    global sales_clerk_window
    sales_clerk_window = Tk()
    sales_clerk_window.title("Online Bookstore/Sales clerk")
    sales_clerk_window.iconbitmap("Itzikgur-My-Seven-Books-1.ico")
    
    if username.get()=="lib_sales_clerk" and password.get()=="employee3003":
    
        title_label = Label(sales_clerk_window, text="Successfully logged in as the Sales clerk of the book-shop!",font=("Times",20,"bold"))
        title_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20,ipadx=100)
        
        add_rec_button = Button(sales_clerk_window, text="Add new record",command=add_record_window)
        add_rec_button.grid(row=1,column=0,padx=15,pady=5)
        
        show_rec_button = Button(sales_clerk_window, text="Show inventory",command=show_record_window)
        show_rec_button.grid(row=1,column=1,padx=15,pady=5)
        
        delete_rec_button = Button(sales_clerk_window, text="Delete a record",command=delete_record_window)
        delete_rec_button.grid(row=2,column=0,padx=15,pady=5)
        
        update_rec_button = Button(sales_clerk_window, text="Update a record",command=update_record_window)
        update_rec_button.grid(row=2,column=1,padx=15,pady=5)
        
        show_req_button = Button(sales_clerk_window, text="Show request fields",command=show_request)
        show_req_button.grid(row=3,column=0,padx=15,pady=5)
        
        
        close_btn_sales_clerk = Button(sales_clerk_window,text="Close",command=sales_clerk_window.destroy)
        close_btn_sales_clerk.grid(row=4,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
        
    else:
        title_label = Label(sales_clerk_window, text="ERROR, INVALID USERNAME OR PASSWORD!!",font=("Times",16,"bold"))
        title_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20,ipadx=100)
        
        close_btn_login = Button(sales_clerk_window,text="Close",command=sales_clerk_window.destroy)
        close_btn_login.grid(row=3,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
 
    
 
def show_request():
    global show_request_window
    show_request_window = Tk()
    show_request_window.title("Online Bookstore/Request fields")
    show_request_window.iconbitmap("Itzikgur-My-Seven-Books-1.ico")
    
    title_label = Label(show_request_window, text="REQUEST FIELD OF BOOKS",font=("Times",28,"bold","underline"))
    title_label.grid(row=0,column=0,columnspan=6,padx=20,pady=20,ipadx=100)
    
    conn = sqlite3.connect('request_records.db')
    c = conn.cursor()
    
    c.execute("SELECT oid, * FROM request")
    data = c.fetchall()
    
    print_data1 = Label(show_request_window,text="S. No.",font=("bold"))
    print_data1.grid(row=1,column=0,padx=5,pady=5)
    print_data2 = Label(show_request_window,text="Book Title",font=("bold"))
    print_data2.grid(row=1,column=1,padx=5,pady=5)
    print_data3 = Label(show_request_window,text="ISBN",font=("bold"))
    print_data3.grid(row=1,column=2,padx=5,pady=5)
    print_data4 = Label(show_request_window,text="Author's Name",font=("bold"))
    print_data4.grid(row=1,column=3,padx=5,pady=5)
    
    i=2
    for record in data:
        print_data_label1 = Label(show_request_window,text=record[0])
        print_data_label1.grid(row=i,column=0)
        print_data_label2 = Label(show_request_window,text=record[1])
        print_data_label2.grid(row=i,column=1)
        print_data_label3 = Label(show_request_window,text=record[2])
        print_data_label3.grid(row=i,column=2)
        print_data_label4 = Label(show_request_window,text=record[3])
        print_data_label4.grid(row=i,column=3)
        i = i+1
    
    conn.commit()
    conn.close()
    
    close_btn = Button(show_request_window,text="Close",command=show_request_window.destroy)
    close_btn.grid(row=i+1,column=0,columnspan=6,padx=10,pady=10,ipadx=100)
    


def submit1(book_title,ISBN,author_name):
    conn = sqlite3.connect('request_records.db')
    c = conn.cursor()
    
    if book_title.get()=="" or ISBN.get()=="" or author_name.get()=="" :
        title_label = Label(add_request_window, text="ERROR, INVALID ENTRY!!",font=("Times",16,"bold"))
        title_label.grid(row=7,column=0,columnspan=2,padx=20,pady=20,ipadx=100)
        return
        
    c.execute("INSERT INTO request VALUES (:book_title, :ISBN, :author_name)",
              {
                  'book_title': book_title.get(),
                  'ISBN': ISBN.get(),
                  'author_name': author_name.get()
              })
    
    conn.commit()
    conn.close()
    
    book_title.delete(0,END)
    ISBN.delete(0,END)
    author_name.delete(0,END)
    
    add_request_window.destroy()

    


def add_request():
    global add_request_window
    add_request_window = Tk()
    add_request_window.title("Online Bookstore/Add new record")
    add_request_window.iconbitmap("Itzikgur-My-Seven-Books-1.ico")
    
    title_label = Label(add_request_window, text="ADDING A REQUEST FIELD",font=("Times",28,"bold","underline"))
    title_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20,ipadx=100)
    book_title = Entry(add_request_window,width=100)
    book_title.grid(row=1,column=1,padx=20)
    ISBN = Entry(add_request_window,width=100)
    ISBN.grid(row=2,column=1,padx=20)
    author_name = Entry(add_request_window,width=100)
    author_name.grid(row=3,column=1,padx=20)
    
    book_title_label = Label(add_request_window, text="Book Title")
    book_title_label.grid(row=1,column=0)
    ISBN_label = Label(add_request_window, text="ISBN")
    ISBN_label.grid(row=2,column=0)
    author_name_label = Label(add_request_window, text="Author's Name")
    author_name_label.grid(row=3,column=0)
    
    submit_btn = Button(add_request_window,text="Click to add request", command=lambda:submit1(book_title,ISBN,author_name))
    submit_btn.grid(row = 6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)  
    
    
def purchase():
    pass


def search1():
     conn = sqlite3.connect('book_records.db')
     c = conn.cursor()
     
     c.execute("SELECT oid, * FROM books WHERE book_title = ?" , (book_title_search.get(),))
     data = c.fetchall()
     
     value = ''
     for record in data:
         value += str(record)
         
     if value=='':
         print_info1 = Label(title_window,text="This book isn't available in the book-shop.",font=("bold"))
         print_info1.grid(row=4,column=0,columnspan=2,padx=5,pady=5)
         
         request_btn = Button(title_window,text="Add book to request field",command=add_request)
         request_btn.grid(row=5,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
         
     else:
         
         print_data1 = Label(title_window,text="Rack No.",font=("bold"))
         print_data1.grid(row=4,column=0,padx=5,pady=5)
         print_data2 = Label(title_window,text="Book Title",font=("bold"))
         print_data2.grid(row=4,column=1,padx=5,pady=5)
         print_data3 = Label(title_window,text="ISBN",font=("bold"))
         print_data3.grid(row=4,column=2,padx=5,pady=5)
         print_data4 = Label(title_window,text="Author's Name",font=("bold"))
         print_data4.grid(row=4,column=3,padx=5,pady=5)
         print_data5 = Label(title_window,text="Number of Copies",font=("bold"))
         print_data5.grid(row=4,column=4,padx=5,pady=5)
         print_data6 = Label(title_window,text="Price per Book",font=("bold"))
         print_data6.grid(row=4,column=5,padx=5,pady=5)
         
         
         i=5
         for record in data:
             print_data_label1 = Label(title_window,text=record[0])
             print_data_label1.grid(row=i,column=0)
             print_data_label2 = Label(title_window,text=record[1])
             print_data_label2.grid(row=i,column=1)
             print_data_label3 = Label(title_window,text=record[2])
             print_data_label3.grid(row=i,column=2)
             print_data_label4 = Label(title_window,text=record[3])
             print_data_label4.grid(row=i,column=3)
             print_data_label5 = Label(title_window,text=record[4])
             print_data_label5.grid(row=i,column=4)
             print_data_label6 = Label(title_window,text=record[5])
             print_data_label6.grid(row=i,column=5)
             i = i+1
     
         purchase_btn = Button(title_window,text="Purchase",command=purchase)
         purchase_btn.grid(row=i,column=1,columnspan=3,padx=10,pady=10,ipadx=50)
     
         
     conn.commit()
     conn.close()
   
    
    
    

def search_by_book_title():
    global title_window
    title_window = Tk()
    title_window.title("Online Bookstore/Customer/Search book by book's title")
    title_window.iconbitmap("Itzikgur-My-Seven-Books-1.ico")
    
    title_label = Label(title_window, text="Searching a book by it's title",font=("Times",18,"bold"))
    title_label.grid(row=0,column=0,columnspan=2,padx=20,pady=15,ipadx=100)
    global book_title_search
    book_title_search = Entry(title_window,width=40)
    book_title_search.grid(row=1,column=1,padx=15,pady=5)
    book_search = book_title_search.get()
    book_title_search_label = Label(title_window, text="Book Title")
    book_title_search_label.grid(row=1,column=0,padx=5,pady=15)
    
    search_title_button = Button(title_window, text="Search",command=search1)
    search_title_button.grid(row=2,column=0,padx=10,pady=10)
    close_btn_login = Button(title_window,text="Close",command=title_window.destroy)
    close_btn_login.grid(row=2,column=1,padx=10,pady=5)
    
    
def search2():
     conn = sqlite3.connect('book_records.db')
     c = conn.cursor()
     
     c.execute("SELECT oid, * FROM books WHERE author_name = ?" , (book_author_search.get(),))
     data = c.fetchall()
     
     value = ''
     for record in data:
         value += str(record)
         
     if value=='':
         print_info1 = Label(title1_window,text="This book isn't available in the book-shop.",font=("bold"))
         print_info1.grid(row=4,column=0,columnspan=2,padx=5,pady=5)
         
         request_btn = Button(title1_window,text="Add book to request field",command=add_request)
         request_btn.grid(row=5,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
         
     else:
         
         print_data1 = Label(title1_window,text="Rack No.",font=("bold"))
         print_data1.grid(row=4,column=0,padx=5,pady=5)
         print_data2 = Label(title1_window,text="Book Title",font=("bold"))
         print_data2.grid(row=4,column=1,padx=5,pady=5)
         print_data3 = Label(title1_window,text="ISBN",font=("bold"))
         print_data3.grid(row=4,column=2,padx=5,pady=5)
         print_data4 = Label(title1_window,text="Author's Name",font=("bold"))
         print_data4.grid(row=4,column=3,padx=5,pady=5)
         print_data5 = Label(title1_window,text="Number of Copies",font=("bold"))
         print_data5.grid(row=4,column=4,padx=5,pady=5)
         print_data6 = Label(title1_window,text="Price per Book",font=("bold"))
         print_data6.grid(row=4,column=5,padx=5,pady=5)
         
         
         i=5
         for record in data:
             print_data_label1 = Label(title1_window,text=record[0])
             print_data_label1.grid(row=i,column=0)
             print_data_label2 = Label(title1_window,text=record[1])
             print_data_label2.grid(row=i,column=1)
             print_data_label3 = Label(title1_window,text=record[2])
             print_data_label3.grid(row=i,column=2)
             print_data_label4 = Label(title1_window,text=record[3])
             print_data_label4.grid(row=i,column=3)
             print_data_label5 = Label(title1_window,text=record[4])
             print_data_label5.grid(row=i,column=4)
             print_data_label6 = Label(title1_window,text=record[5])
             print_data_label6.grid(row=i,column=5)
             i = i+1
     
         purchase_btn = Button(title1_window,text="Purchase",command=purchase)
         purchase_btn.grid(row=i,column=1,columnspan=3,padx=10,pady=10,ipadx=50)
     
         
     conn.commit()
     conn.close()
       
    
    
    
    
def search_by_author_name():
    global title1_window
    title1_window = Tk()
    title1_window.title("Online Bookstore/Customer/Search book by author's name")
    title1_window.iconbitmap("Itzikgur-My-Seven-Books-1.ico")
    
    title_label = Label(title1_window, text="Searching a book by it's author's name",font=("Times",18,"bold"))
    title_label.grid(row=0,column=0,columnspan=2,padx=20,pady=15,ipadx=100)
    global book_author_search
    book_author_search = Entry(title1_window,width=40)
    book_author_search.grid(row=1,column=1,padx=15,pady=5)
    book_author_search_label = Label(title1_window, text="Author's name")
    book_author_search_label.grid(row=1,column=0,padx=5,pady=15)
    
    search_title_button = Button(title1_window, text="Search",command=search2)
    search_title_button.grid(row=2,column=0,padx=10,pady=10)
    close_btn_login = Button(title1_window,text="Close",command=title1_window.destroy)
    close_btn_login.grid(row=2,column=1,padx=10,pady=5)


def login_as_customer():
    global customer_window
    customer_window = Tk()
    customer_window.title("Online Bookstore/Customer")
    customer_window.iconbitmap("Itzikgur-My-Seven-Books-1.ico")

    if password.get()=="customer3003":    

        title_label = Label(customer_window, text="Successfully logged in as the Customer of the book-shop!",font=("Times",20,"bold"))
        title_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20,ipadx=100)
        
        search_by_book_title_button = Button(customer_window, text="Search by Book's title",command=search_by_book_title)
        search_by_book_title_button.grid(row=1,column=0,padx=15,pady=5)
        
        search_by_author_name_button = Button(customer_window, text="Search by Author's name",command=search_by_author_name)
        search_by_author_name_button.grid(row=1,column=1,padx=15,pady=5)
        
        close_btn_customer = Button(customer_window,text="Close",command=customer_window.destroy)
        close_btn_customer.grid(row=3,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
        
    else:
        title_label = Label(customer_window, text="ERROR, INVALID USERNAME OR PASSWORD!!",font=("Times",16,"bold"))
        title_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20,ipadx=100)
        
        close_btn_login = Button(customer_window,text="Close",command=customer_window.destroy)
        close_btn_login.grid(row=3,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
    
    
    



def login(clicked):
    global login_window
    login_window = Tk()
    login_window.title("Online Bookstore/Login")
    login_window.iconbitmap("Itzikgur-My-Seven-Books-1.ico")
    
    global username
    global password
    
    if clicked.get() == 'Employee(Manager)':
        
        title_label = Label(login_window, text="LOGIN CREDENTIALS",font=("Times",16,"bold","underline"))
        title_label.grid(row=1,column=0,columnspan=2,padx=20,pady=20,ipadx=100)
        
        username = Entry(login_window,width=50)
        username.grid(row=2,column=1,padx=20)
        password = Entry(login_window,width=50)
        password.grid(row=3,column=1,padx=20)
        
        username_label = Label(login_window, text="Username")
        username_label.grid(row=2,column=0)
        password_label = Label(login_window, text="Password")
        password_label.grid(row=3,column=0)
        
        label4 = Label(login_window, text="LOGIN AS " + clicked.get(), font=("Times",16,"bold"),pady=10,padx=10)
        label4.grid(row=0,column=0,columnspan=2)
        
        login_button = Button(login_window, text="login",command=login_as_manager)
        login_button.grid(row=4,column=0,padx=10,columnspan=2,pady=10,ipadx=50)
        close_btn_login = Button(login_window,text="Close",command=login_window.destroy)
        close_btn_login.grid(row=5,column=0,padx=10,columnspan=2,pady=5,ipadx=50)
        
    elif clicked.get() == 'Employee(Owner)':
        
        title_label = Label(login_window, text="LOGIN CREDENTIALS",font=("Times",16,"bold","underline"))
        title_label.grid(row=1,column=0,columnspan=2,padx=20,pady=20,ipadx=100)
        
        username = Entry(login_window,width=50)
        username.grid(row=2,column=1,padx=20)
        password = Entry(login_window,width=50)
        password.grid(row=3,column=1,padx=20)
        
        username_label = Label(login_window, text="Username")
        username_label.grid(row=2,column=0)
        password_label = Label(login_window, text="Password")
        password_label.grid(row=3,column=0)
        
        label4 = Label(login_window, text="LOGIN AS " + clicked.get(), font=("Times",16,"bold"),pady=10,padx=10)
        label4.grid(row=0,column=0,columnspan=2)
        
        login_button = Button(login_window, text="login",command=login_as_owner)
        login_button.grid(row=4,column=0,padx=10,columnspan=2,pady=10)
        close_btn_login = Button(login_window,text="Close",command=login_window.destroy)
        close_btn_login.grid(row=5,column=0,padx=10,pady=5,columnspan=2,ipadx=50)
        
        
    elif clicked.get() == 'Employee(Sales clerk)':
        
        title_label = Label(login_window, text="LOGIN CREDENTIALS",font=("Times",16,"bold","underline"))
        title_label.grid(row=1,column=0,columnspan=2,padx=20,pady=20,ipadx=100)
        
        username = Entry(login_window,width=50)
        username.grid(row=2,column=1,padx=20)
        password = Entry(login_window,width=50)
        password.grid(row=3,column=1,padx=20)
        
        username_label = Label(login_window, text="Username")
        username_label.grid(row=2,column=0)
        password_label = Label(login_window, text="Password")
        password_label.grid(row=3,column=0)
        
        label4 = Label(login_window, text="LOGIN AS " + clicked.get(), font=("Times",16,"bold"),pady=10,padx=10)
        label4.grid(row=0,column=0,columnspan=2)
        
        login_button = Button(login_window, text="login",command=login_as_sales_clerk)
        login_button.grid(row=4,column=0,padx=10,pady=10,columnspan=2,ipadx=50)
        close_btn_login = Button(login_window,text="Close",command=login_window.destroy)
        close_btn_login.grid(row=5,column=0,padx=10,pady=5,columnspan=2,ipadx=50)
        
    elif clicked.get() == 'Customer':
        
        title_label = Label(login_window, text="LOGIN CREDENTIALS",font=("Times",16,"bold","underline"))
        title_label.grid(row=1,column=0,columnspan=2,padx=20,pady=20,ipadx=100)
        
        username = Entry(login_window,width=50)
        username.grid(row=2,column=1,padx=20)
        password = Entry(login_window,width=50)
        password.grid(row=3,column=1,padx=20)
        
        username_label = Label(login_window, text="Username")
        username_label.grid(row=2,column=0)
        password_label = Label(login_window, text="Password")
        password_label.grid(row=3,column=0)
        
        label4 = Label(login_window, text="LOGIN AS " + clicked.get(), font=("Times",16,"bold"),pady=10,padx=10)
        label4.grid(row=0,column=0,columnspan=2)
        
        login_button = Button(login_window, text="login",command=login_as_customer)
        login_button.grid(row=4,column=0,padx=10,columnspan=2,pady=10,ipadx=50)
        close_btn_login = Button(login_window,text="Close",command=login_window.destroy)
        close_btn_login.grid(row=5,column=0,padx=10,columnspan=2,pady=5,ipadx=50)
        
    else :
        title_label = Label(login_window, text="ERROR, INVALID CHOICE!!",font=("Times",16,"bold"))
        title_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20,ipadx=100)
        
        close_btn_login = Button(login_window,text="Close",command=login_window.destroy)
        close_btn_login.grid(row=3,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
               
    
    
    

def submit(book_title,ISBN,author_name,number_of_copies,price_per_book):
    
    conn = sqlite3.connect('book_records.db')
    c = conn.cursor()
    
    if book_title.get()=="" or ISBN.get()=="" or author_name.get()=="" or number_of_copies.get()=="" or price_per_book.get()=="" :
        title_label = Label(add_new_record_window, text="ERROR, INVALID ENTRY!!",font=("Times",16,"bold"))
        title_label.grid(row=7,column=0,columnspan=2,padx=20,pady=20,ipadx=100)
        return
        
    c.execute("INSERT INTO books VALUES (:book_title, :ISBN, :author_name, :number_of_copies, :price_per_book)",
              {
                  'book_title': book_title.get(),
                  'ISBN': ISBN.get(),
                  'author_name': author_name.get(),
                  'number_of_copies': number_of_copies.get(),
                  'price_per_book': price_per_book.get()
              })
    
    conn.commit()
    conn.close()
    
    book_title.delete(0,END)
    ISBN.delete(0,END)
    author_name.delete(0,END)
    number_of_copies.delete(0,END)
    price_per_book.delete(0,END)
    
    add_new_record_window.destroy()
    
    
def delete_book(delete_record,i):
    conn = sqlite3.connect('book_records.db')
    c = conn.cursor()
    
    c.execute("DELETE from books WHERE oid = " + delete_record.get())
    delete_record.delete(0,END)
    
    confirm_label = Label(delete_record_from_inventory_window,text="Record deleted from the database successfully!", font=("Times",18,"bold"))
    confirm_label.grid(row=i+1,column=0,columnspan=6)
    i=i+1
    
    conn.commit()
    conn.close()
    delete_record_from_inventory_window.destroy()
    
def show_record_window():
    global show_inventory_window
    show_inventory_window = Tk()
    show_inventory_window.title("Online Bookstore/Inventory")
    show_inventory_window.iconbitmap("Itzikgur-My-Seven-Books-1.ico")
    
    title_label = Label(show_inventory_window, text="BOOK-SHOP INVENTORY",font=("Times",28,"bold","underline"))
    title_label.grid(row=0,column=0,columnspan=6,padx=20,pady=20,ipadx=100)
    
    conn = sqlite3.connect('book_records.db')
    c = conn.cursor()
    
    c.execute("SELECT oid, * FROM books")
    data = c.fetchall()
    
    print_data1 = Label(show_inventory_window,text="Rack No.",font=("bold"))
    print_data1.grid(row=1,column=0,padx=5,pady=5)
    print_data2 = Label(show_inventory_window,text="Book Title",font=("bold"))
    print_data2.grid(row=1,column=1,padx=5,pady=5)
    print_data3 = Label(show_inventory_window,text="ISBN",font=("bold"))
    print_data3.grid(row=1,column=2,padx=5,pady=5)
    print_data4 = Label(show_inventory_window,text="Author's Name",font=("bold"))
    print_data4.grid(row=1,column=3,padx=5,pady=5)
    print_data5 = Label(show_inventory_window,text="Number of Copies",font=("bold"))
    print_data5.grid(row=1,column=4,padx=5,pady=5)
    print_data6 = Label(show_inventory_window,text="Price per Book",font=("bold"))
    print_data6.grid(row=1,column=5,padx=5,pady=5)
    
    i=2
    for record in data:
        print_data_label1 = Label(show_inventory_window,text=record[0])
        print_data_label1.grid(row=i,column=0)
        print_data_label2 = Label(show_inventory_window,text=record[1])
        print_data_label2.grid(row=i,column=1)
        print_data_label3 = Label(show_inventory_window,text=record[2])
        print_data_label3.grid(row=i,column=2)
        print_data_label4 = Label(show_inventory_window,text=record[3])
        print_data_label4.grid(row=i,column=3)
        print_data_label5 = Label(show_inventory_window,text=record[4])
        print_data_label5.grid(row=i,column=4)
        print_data_label6 = Label(show_inventory_window,text=record[5])
        print_data_label6.grid(row=i,column=5)
        i = i+1
    
    conn.commit()
    conn.close()
    
    close_btn = Button(show_inventory_window,text="Close",command=show_inventory_window.destroy)
    close_btn.grid(row=i+1,column=0,columnspan=6,padx=10,pady=10,ipadx=100)
    
    
def delete_record_window():
    global delete_record_from_inventory_window
    delete_record_from_inventory_window = Tk()
    delete_record_from_inventory_window.title("Online Bookstore/Deleting Record")
    delete_record_from_inventory_window.iconbitmap("Itzikgur-My-Seven-Books-1.ico")
    
    title_label = Label(delete_record_from_inventory_window, text="BOOK-SHOP INVENTORY",font=("Times",28,"bold","underline"))
    title_label.grid(row=0,column=0,columnspan=6,padx=20,pady=20,ipadx=100)
    
    conn = sqlite3.connect('book_records.db')
    c = conn.cursor()
    
    c.execute("SELECT oid, * FROM books")
    data = c.fetchall()
    
    print_data1 = Label(delete_record_from_inventory_window,text="Rack No.",font=("bold"))
    print_data1.grid(row=1,column=0,padx=5,pady=5)
    print_data2 = Label(delete_record_from_inventory_window,text="Book Title",font=("bold"))
    print_data2.grid(row=1,column=1,padx=5,pady=5)
    print_data3 = Label(delete_record_from_inventory_window,text="ISBN",font=("bold"))
    print_data3.grid(row=1,column=2,padx=5,pady=5)
    print_data4 = Label(delete_record_from_inventory_window,text="Author's Name",font=("bold"))
    print_data4.grid(row=1,column=3,padx=5,pady=5)
    print_data5 = Label(delete_record_from_inventory_window,text="Number of Copies",font=("bold"))
    print_data5.grid(row=1,column=4,padx=5,pady=5)
    print_data6 = Label(delete_record_from_inventory_window,text="Price per Book",font=("bold"))
    print_data6.grid(row=1,column=5,padx=5,pady=5)
    
    i=2
    for record in data:
        print_data_label1 = Label(delete_record_from_inventory_window,text=record[0])
        print_data_label1.grid(row=i,column=0)
        print_data_label2 = Label(delete_record_from_inventory_window,text=record[1])
        print_data_label2.grid(row=i,column=1)
        print_data_label3 = Label(delete_record_from_inventory_window,text=record[2])
        print_data_label3.grid(row=i,column=2)
        print_data_label4 = Label(delete_record_from_inventory_window,text=record[3])
        print_data_label4.grid(row=i,column=3)
        print_data_label5 = Label(delete_record_from_inventory_window,text=record[4])
        print_data_label5.grid(row=i,column=4)
        print_data_label6 = Label(delete_record_from_inventory_window,text=record[5])
        print_data_label6.grid(row=i,column=5)
        i = i+1
    
    delete_record = Entry(delete_record_from_inventory_window,width=20)
    delete_record.grid(row=i,column=3,pady=20,padx=5)
    delete_record_label = Label(delete_record_from_inventory_window,text="Enter rack number:")
    delete_record_label.grid(row=i,column=0,columnspan=2)
    
    global delete_id
    delete_id = delete_record.get()
    delete_btn = Button(delete_record_from_inventory_window,text="Delete Record",command=lambda:delete_book(delete_record, i))
    delete_btn.grid(row=i+1,column=0,columnspan=6,padx=10,pady=10,ipadx=100)
    
    conn.commit()
    conn.close()
    
def edit():
    conn = sqlite3.connect('book_records.db')
    c = conn.cursor()
    
    c.execute("""UPDATE books SET
              book_title = :book,
              ISBN = :isbn,
              author_name = :author,
              number_of_copies = :number,
              price_per_book = :price
              
              WHERE oid = :oid""",
              {
                  'book': book_title_editor.get(),
                  'isbn': ISBN_editor.get(),
                  'author': author_name_editor.get(),
                  'number': number_of_copies_editor.get(),
                  'price': price_per_book_editor.get(),
                  
                  'oid': update_id
                  }
              
              )
    
    book_title_editor.delete(0,END)
    ISBN_editor.delete(0,END)
    author_name_editor.delete(0,END)
    number_of_copies_editor.delete(0,END)
    price_per_book_editor.delete(0,END)
    
    conn.commit()
    conn.close()


def editor(update_record,i):
    global editor_window
    editor_window = Tk()
    editor_window.title("Online Bookstore/Editor")
    editor_window.iconbitmap("Itzikgur-My-Seven-Books-1.ico")
    
    global book_title_editor
    global ISBN_editor
    global author_name_editor
    global number_of_copies_editor
    global price_per_book_editor
    
    book_title_editor = Entry(editor_window,width=100)
    book_title_editor.grid(row=1,column=1,padx=20)
    ISBN_editor = Entry(editor_window,width=100)
    ISBN_editor.grid(row=2,column=1,padx=20)
    author_name_editor = Entry(editor_window,width=100)
    author_name_editor.grid(row=3,column=1,padx=20)
    number_of_copies_editor = Entry(editor_window,width=100)
    number_of_copies_editor.grid(row=4,column=1,padx=20)
    price_per_book_editor = Entry(editor_window,width=100)
    price_per_book_editor.grid(row=5,column=1,padx=20)
    
    book_title_label_editor = Label(editor_window, text="Book Title")
    book_title_label_editor.grid(row=1,column=0)
    ISBN_label_editor = Label(editor_window, text="ISBN")
    ISBN_label_editor.grid(row=2,column=0)
    author_name_label_editor = Label(editor_window, text="Author's Name")
    author_name_label_editor.grid(row=3,column=0)
    number_of_copies_label_editor = Label(editor_window, text="Number of copies")
    number_of_copies_label_editor.grid(row=4,column=0)
    price_per_book_label_editor = Label(editor_window, text="Price per Book")
    price_per_book_label_editor.grid(row=5,column=0)
    
    global update_id
    update_id = update_record.get()
    save_btn = Button(editor_window,text="Save Record",command=edit)
    save_btn.grid(row=6,column=0,columnspan=6,padx=10,pady=10,ipadx=100)
    
    
    conn = sqlite3.connect('book_records.db')
    c = conn.cursor()
    
    c.execute("SELECT * from books WHERE oid = " + update_record.get())
    records = c.fetchall()
    
    for record in records:
        book_title_editor.insert(0,record[0])
        ISBN_editor.insert(0,record[1])
        author_name_editor.insert(0,record[2])
        number_of_copies_editor.insert(0,record[3])
        price_per_book_editor.insert(0,record[4])
    
    conn.commit()
    conn.close()
    update_record_from_inventory_window.destroy()
    
    
def update_record_window():
    global update_record_from_inventory_window
    update_record_from_inventory_window = Tk()
    update_record_from_inventory_window.title("Online Bookstore/Update Record")
    update_record_from_inventory_window.iconbitmap("Itzikgur-My-Seven-Books-1.ico")
    
    title_label = Label(update_record_from_inventory_window, text="BOOK-SHOP INVENTORY",font=("Times",28,"bold","underline"))
    title_label.grid(row=0,column=0,columnspan=6,padx=20,pady=20,ipadx=100)
    
    conn = sqlite3.connect('book_records.db')
    c = conn.cursor()
    
    c.execute("SELECT oid, * FROM books")
    data = c.fetchall()
    
    print_data1 = Label(update_record_from_inventory_window,text="Rack No.",font=("bold"))
    print_data1.grid(row=1,column=0,padx=5,pady=5)
    print_data2 = Label(update_record_from_inventory_window,text="Book Title",font=("bold"))
    print_data2.grid(row=1,column=1,padx=5,pady=5)
    print_data3 = Label(update_record_from_inventory_window,text="ISBN",font=("bold"))
    print_data3.grid(row=1,column=2,padx=5,pady=5)
    print_data4 = Label(update_record_from_inventory_window,text="Author's Name",font=("bold"))
    print_data4.grid(row=1,column=3,padx=5,pady=5)
    print_data5 = Label(update_record_from_inventory_window,text="Number of Copies",font=("bold"))
    print_data5.grid(row=1,column=4,padx=5,pady=5)
    print_data6 = Label(update_record_from_inventory_window,text="Price per Book",font=("bold"))
    print_data6.grid(row=1,column=5,padx=5,pady=5)
    
    i=2
    for record in data:
        print_data_label1 = Label(update_record_from_inventory_window,text=record[0])
        print_data_label1.grid(row=i,column=0)
        print_data_label2 = Label(update_record_from_inventory_window,text=record[1])
        print_data_label2.grid(row=i,column=1)
        print_data_label3 = Label(update_record_from_inventory_window,text=record[2])
        print_data_label3.grid(row=i,column=2)
        print_data_label4 = Label(update_record_from_inventory_window,text=record[3])
        print_data_label4.grid(row=i,column=3)
        print_data_label5 = Label(update_record_from_inventory_window,text=record[4])
        print_data_label5.grid(row=i,column=4)
        print_data_label6 = Label(update_record_from_inventory_window,text=record[5])
        print_data_label6.grid(row=i,column=5)
        i = i+1
    
    update_record = Entry(update_record_from_inventory_window,width=20)
    update_record.grid(row=i,column=3,pady=20,padx=5)
    update_record_label = Label(update_record_from_inventory_window,text="Enter rack number: ")
    update_record_label.grid(row=i,column=0,columnspan=2)
    
    update_btn = Button(update_record_from_inventory_window,text="Edit",command=lambda:editor(update_record,i))
    update_btn.grid(row=i+1,column=0,columnspan=6,padx=10,pady=10,ipadx=100)
    i=i+1
    
    conn.commit()
    conn.close()
    
def add_record_window():
    global add_new_record_window
    add_new_record_window = Tk()
    add_new_record_window.title("Online Bookstore/Add new record")
    add_new_record_window.iconbitmap("Itzikgur-My-Seven-Books-1.ico")
    
    title_label = Label(add_new_record_window, text="ADDING A NEW BOOK TO THE BOOK-SHOP",font=("Times",28,"bold","underline"))
    title_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20,ipadx=100)
    book_title = Entry(add_new_record_window,width=100)
    book_title.grid(row=1,column=1,padx=20)
    ISBN = Entry(add_new_record_window,width=100)
    ISBN.grid(row=2,column=1,padx=20)
    author_name = Entry(add_new_record_window,width=100)
    author_name.grid(row=3,column=1,padx=20)
    number_of_copies = Entry(add_new_record_window,width=100)
    number_of_copies.grid(row=4,column=1,padx=20)
    price_per_book = Entry(add_new_record_window,width=100)
    price_per_book.grid(row=5,column=1,padx=20)
    
    book_title_label = Label(add_new_record_window, text="Book Title")
    book_title_label.grid(row=1,column=0)
    ISBN_label = Label(add_new_record_window, text="ISBN")
    ISBN_label.grid(row=2,column=0)
    author_name_label = Label(add_new_record_window, text="Author's Name")
    author_name_label.grid(row=3,column=0)
    number_of_copies_label = Label(add_new_record_window, text="Number of copies")
    number_of_copies_label.grid(row=4,column=0)
    price_per_book_label = Label(add_new_record_window, text="Price per Book")
    price_per_book_label.grid(row=5,column=0)
    
    submit_btn = Button(add_new_record_window,text="Click to add record to database", command=lambda:submit(book_title,ISBN,author_name,number_of_copies,price_per_book))
    submit_btn.grid(row = 6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
    
    
def register():
    global register_window
    register_window = Tk()
    register_window.title("Online Bookstore/Register")
    register_window.iconbitmap("Itzikgur-My-Seven-Books-1.ico")
    
    title_label = Label(register_window, text="You can use your name as username and use 'customer3003' as password(without quotes) to login!",font=("Times",16,"bold"))
    title_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20,ipadx=100)
    
    close_btn_login = Button(register_window,text="Close",command=register_window.destroy)
    close_btn_login.grid(row=3,column=0,columnspan=2,padx=10,pady=10,ipadx=50)
    
    

if __name__ == '__main__':  
    root = Tk()
    root.title("Online Bookstore")
    root.iconbitmap("Itzikgur-My-Seven-Books-1.ico")
    root.geometry("1300x700")
    
    img1 = ImageTk.PhotoImage(Image.open("bg_img.jpg"))
    label1 = Label(image=img1)
    label1.place(x=0,y=0,relwidth=1,relheight=1)
    label2 = Label(root, text="BOOK-SHOP AUTOMATION SOFTWARE WELCOMES YOU!",font=("Times", 32,"bold","underline"),fg="black",bg="wheat",pady=20,padx=35).pack()
    
    options = ["Customer", "Employee(Manager)", "Employee(Sales clerk)", "Employee(Owner)"]
    clicked = StringVar()
    clicked.set("Choose your login type")
    
    frame1 = LabelFrame(root,bg="lemonchiffon",pady=20,padx=10)
    frame1.pack(padx=10,pady=10)
    
    label3 = Label(frame1, text="LOGIN HERE", font=("Times",20,"bold"),fg="saddleBrown",bg="lemonchiffon",pady=10,padx=10)
    label3.pack(padx=5,pady=5,ipadx=50)
    drop_down = OptionMenu(frame1,clicked, *options)
    drop_down.pack(pady=10)
    login_button = Button(frame1, text="Next",bg="lightcyan",command=lambda: login(clicked))
    login_button.pack(padx=5,pady=5,ipadx=20)
    
    # CREATING DATABASE AND TABLE
    '''
    conn = sqlite3.connect('book_records.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE books(
            book_title text,
            ISBN integer,
            author_name text,
            number_of_copies integer,
            price_per_book real
            )""")
    conn.commit()
    conn.close()
    
    conn1 = sqlite3.connect('request_records.db')
    c1 = conn1.cursor()
    c1.execute("""CREATE TABLE request(
            book_title text,
            ISBN integer,
            author_name text
            )""")
    conn1.commit()
    conn1.close()
    '''
    
    frame2 = LabelFrame(root,bg="lemonchiffon",pady=20,padx=10)
    frame2.pack(padx=10,pady=10)
    
    label3 = Label(frame2, text="FOR NEW CUSTOMER, SIGN UP HERE", font=("Times",18,"bold"),fg="saddleBrown",bg="lemonchiffon",pady=10,padx=10)
    label3.pack()
    login_button = Button(frame2, text="Sign up",bg="lightcyan",command=register)
    login_button.pack(padx=5,pady=5,ipadx=20)
    
    close_btn = Button(root,text="Exit",command=root.destroy)
    close_btn.pack(padx=10,pady=5,ipadx=20)
    
    root.mainloop()
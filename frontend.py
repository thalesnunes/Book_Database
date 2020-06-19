from tkinter import *
from backend import *


create_db()

window = Tk()

textTitle = Label(window, text='Title')
textTitle.grid(row=0, column=0)
booktitle = StringVar()
title = Entry(window, textvariable=booktitle)
title.grid(row=0, column=1)

textAuthor = Label(window, text='Author')
textAuthor.grid(row=0, column=2)
bookauthor = StringVar()
author = Entry(window, textvariable=bookauthor)
author.grid(row=0, column=3)

textYear = Label(window, text='Year')
textYear.grid(row=2, column=0)
bookyear = StringVar()
year = Entry(window, textvariable=bookyear)
year.grid(row=2, column=1)

textISBN = Label(window, text='ISBN')
textISBN.grid(row=2, column=2)
bookISBN = StringVar()
isbn = Entry(window, textvariable=bookISBN)
isbn.grid(row=2, column=3)

data_list = Listbox(window, height=6, width=35)
data_list.grid(row=3, column=0, rowspan=6, columnspan=2)

scroll1 = Scrollbar(window)
scroll1.grid(row=3, column=2, rowspan=6)
scroll2 = Scrollbar(window, orient='horizontal')
scroll2.grid(row=10, column=0, columnspan=2, rowspan=3)
data_list.configure(yscrollcommand=scroll1.set, xscrollcommand=scroll2.set)
scroll1.configure(command=data_list.yview)
scroll2.configure(command=data_list.xview)

view = lambda: view_all(data_list)
search = lambda: search_db(data_list,
                           booktitle.get(),
                           bookauthor.get(),
                           bookyear.get(),
                           bookISBN.get(),)
insert = lambda: insert_db(data_list,
                           booktitle.get(),
                           bookauthor.get(),
                           bookyear.get(),
                           bookISBN.get(),)
update = lambda: update_db(booktitle.get(),
                           bookauthor.get(),
                           bookyear.get(),
                           bookISBN.get(),)
delete = lambda: delete_db(booktitle.get())

butt1 = Button(window, text='View All', width=12, command=view)
butt1.grid(row=3, column=3)
butt2 = Button(window, text='Search entry', width=12, command=search)
butt2.grid(row=4, column=3)
butt3 = Button(window, text='Add entry', width=12, command=insert)
butt3.grid(row=5, column=3)
butt4 = Button(window, text='Update', width=12, command=update)
butt4.grid(row=6, column=3)
butt5 = Button(window, text='Delete', width=12, command=delete)
butt5.grid(row=7, column=3)
butt6 = Button(window, text='Close', width=12, command=window.quit)
butt6.grid(row=8, column=3)


window.mainloop()

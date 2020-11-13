from tkinter import *


class Block:
    def __init__(self, master):
        self.lab1 = Label(master, width=20, text=' Перше число:', pady=10)
        self.ent1 = Entry(master, width=20)

        self.lab2 = Label(master, width=20, text='Друге число:', pady=10)
        self.ent2 = Entry(master, width=20)

        self.but = Button(master,
                          text="Порахувати", pady=10)

        self.num = Label(master, width=40, pady=20, text='Результат:')

        self.but['command'] = self.count
        self.lab1.pack()
        self.ent1.pack()
        self.lab2.pack()
        self.ent2.pack()
        self.but.pack()
        self.num.pack()

    def count(self):
        val1 = self.ent1.get()
        val2 = self.ent2.get()

        if val1 == '' or val2 == '':
            self.num['text'] = 'Будь ласка, введіть всі числа'
            return

        if not val1.isnumeric() or not val2.isnumeric():
            self.num['text'] = 'Будь ласка, введіть числові значення'
            return

        num1 = int(val1)
        num2 = int(val2)

        min_value = min(num1, num2)
        if min_value == 0:
            self.num['text'] = 'Введіть менше число відмінне від нуля'
        else:
            self.num['text'] = 'Результат: ' + str(max(num1, num2)/min_value)



root = Tk()
root.title('Варіант 8')

main = Block(root)

root.mainloop()
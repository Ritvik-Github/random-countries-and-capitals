from tkinter import *
import random
root = Tk()
root.title("Random Capitals and Countries")
root.geometry("400x400")
capital_entry = Entry(root)
country_entry = Entry(root)
country_label = Label(root)
capital_label = Label(root)
country_random_label = Label(root)
capital_random_label = Label(root)
country_list = []
capital_list = []


def Get():
    country_new_append = country_entry.get()
    country_list.append(country_new_append)
    print(country_new_append)
    country_label['text'] = "Country Name: " + str(country_list)
    capital_new_append = capital_entry.get()
    capital_list.append(capital_new_append)
    print(capital_new_append)
    capital_label['text'] = "Capital Name: " + str(capital_list)


def Randomixze():
    random_number_country = random.randint((0, len.country_list))
    random_number_capital = random.randint((0, len.capital_list))
    country_random_label["text"] = "Random Country: " + country_list[random_number_country]     
    capital_random_label["text"] = "Random Capital: " + capital_list[random_number_capital]


btn_display = Button(root, text="Dispaly Countries and Capital Names",
                     bg="Blue", fg="white", command=Get)
btn_random = Button(root, text="Dispaly Countries and Capital Names Randomly",
                    bg="Blue", fg="white", command=Randomixze)

capital_entry.pack()
country_entry.pack()
country_label.pack()
capital_label.pack()
capital_random_label.pack()
country_random_label.pack()
btn_random.pack()
btn_display.pack()
root.mainloop()

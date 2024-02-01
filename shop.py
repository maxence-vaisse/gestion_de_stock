from tkinter import *
from tkinter import ttk
from myDB import MyDB
from product import Product
from category import Category

class Shop:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestion de Stock")
        
        self.db = MyDB(host="localhost", user="root", password="root", database="store")
        self.product_manager = Product(self.db)
        self.category_manager = Category(self.db)
        
        self.create_widgets()
        self.load_products()

    def create_widgets(self):
        self.product_frame = Frame(self.master)
        self.product_frame.pack(pady=10)

        self.products_label = Label(self.product_frame, text="Liste des Produits")
        self.products_label.grid(row=0, column=0, columnspan=3)

        self.product_tree = ttk.Treeview(self.product_frame, columns=(1, 2, 3, 4, 5, 6), show="headings", height=15)
        self.product_tree.grid(row=1, column=0, columnspan=3)

        self.product_tree.heading(1, text="ID")
        self.product_tree.heading(2, text="Nom")
        self.product_tree.heading(3, text="Description")
        self.product_tree.heading(4, text="Prix")
        self.product_tree.heading(5, text="Quantité")
        self.product_tree.heading(6, text="Catégorie")

        self.add_product_button = Button(self.product_frame, text="Ajouter Produit", command=self.add_product)
        self.add_product_button.grid(row=2, column=0)

        self.delete_product_button = Button(self.product_frame, text="Supprimer Produit", command=self.delete_product)
        self.delete_product_button.grid(row=2, column=1)

        self.update_product_button = Button(self.product_frame, text="Modifier Produit", command=self.update_product)
        self.update_product_button.grid(row=2, column=2)

    def load_products(self):
        products = self.product_manager.get_all_products()
        for product in products:
            self.product_tree.insert("", "end", values=product)

    def add_product(self):
        self.add_product_window = Toplevel(self.master)
        self.add_product_window.title("Ajouter un Produit")

        Label(self.add_product_window, text="Nom:").grid(row=0, column=0)
        self.product_name_entry = Entry(self.add_product_window)
        self.product_name_entry.grid(row=0, column=1)

        Label(self.add_product_window, text="Description:").grid(row=1, column=0)
        self.product_description_entry = Entry(self.add_product_window)
        self.product_description_entry.grid(row=1, column=1)

        Label(self.add_product_window, text="Prix:").grid(row=2, column=0)
        self.product_price_entry = Entry(self.add_product_window)
        self.product_price_entry.grid(row=2, column=1)

        Label(self.add_product_window, text="Quantité:").grid(row=3, column=0)
        self.product_quantity_entry = Entry(self.add_product_window)
        self.product_quantity_entry.grid(row=3, column=1)

        Label(self.add_product_window, text="Catégorie:").grid(row=4, column=0)
        self.product_category_entry = Entry(self.add_product_window)
        self.product_category_entry.grid(row=4, column=1)

        submit_button = Button(self.add_product_window, text="Ajouter", command=self.submit_new_product)
        submit_button.grid(row=5, column=0, columnspan=2)

    def submit_new_product(self):
        name = self.product_name_entry.get()
        description = self.product_description_entry.get()
        price = int(self.product_price_entry.get())
        quantity = int(self.product_quantity_entry.get())
        category_id = int(self.product_category_entry.get())

        self.product_manager.add_product(name, description, price, quantity, category_id)

        self.product_tree.delete(*self.product_tree.get_children())
        self.load_products()

        self.add_product_window.destroy()

    def delete_product(self):
        selected_item = self.product_tree.selection()
        if selected_item:
            product_id = self.product_tree.item(selected_item, 'values')[0]
            self.product_manager.delete_product(product_id)
            self.product_tree.delete(*self.product_tree.get_children())
            self.load_products()

    def update_product(self):
        self.update_product_window = Toplevel(self.master)
        self.update_product_window.title("Modifier un Produit")

        selected_item = self.product_tree.selection()
        if selected_item:
            self.selected_product_id = self.product_tree.item(selected_item, 'values')[0]

            Label(self.update_product_window, text="Nouveau Prix:").grid(row=0, column=0)
            self.new_price_entry = Entry(self.update_product_window)
            self.new_price_entry.grid(row=0, column=1)

            Label(self.update_product_window, text="Nouvelle Quantité:").grid(row=1, column=0)
            self.new_quantity_entry = Entry(self.update_product_window)
            self.new_quantity_entry.grid(row=1, column=1)

            Label(self.update_product_window, text="Nouvelle Catégorie:").grid(row=2, column=0)
            self.new_category_entry = Entry(self.update_product_window)
            self.new_category_entry.grid(row=2, column=1)

            submit_button = Button(self.update_product_window, text="Modifier", command=self.submit_update)
            submit_button.grid(row=3, column=0, columnspan=2)

    def submit_update(self):
        new_price = int(self.new_price_entry.get())
        new_quantity = int(self.new_quantity_entry.get())
        new_category_id = int(self.new_category_entry.get())

        self.product_manager.update_product(self.selected_product_id, new_price, new_quantity, new_category_id)

        self.product_tree.delete(*self.product_tree.get_children())
        self.load_products()

        self.update_product_window.destroy()

def main():
    root = Tk()
    app = Shop(root)
    root.mainloop()

if __name__ == "__main__":
    main()
class Product:
    def __init__(self, db):
        self.db = db

    def add_product(self, name, description, price, quantity, id_category):
        sql = "INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)"
        val = (name, description, price, quantity, id_category)
        self.db.cursor.execute(sql, val)
        self.db.connection.commit()

    def delete_product(self, product_id):
        sql = "DELETE FROM product WHERE id = %s"
        val = (product_id,)
        self.db.cursor.execute(sql, val)
        self.db.connection.commit()

    def update_product(self, product_id, new_price, new_quantity, new_category_id):
        sql = "UPDATE product SET price = %s, quantity = %s, id_category = %s WHERE id = %s"
        val = (new_price, new_quantity, new_category_id, product_id)
        self.db.cursor.execute(sql, val)
        self.db.connection.commit()

    def get_all_products(self):
        sql = "SELECT * FROM product"
        self.db.cursor.execute(sql)
        products = self.db.cursor.fetchall()
        return products

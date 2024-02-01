class Category:
    def __init__(self, db):
        self.db = db

    def add_category(self, name):
        sql = "INSERT INTO category (name) VALUES (%s)"
        val = (name,)
        self.db.cursor.execute(sql, val)
        self.db.connection.commit()

    def delete_category(self, category_id):
        sql = "DELETE FROM category WHERE id = %s"
        val = (category_id,)
        self.db.cursor.execute(sql, val)
        self.db.connection.commit()

    def update_category(self, category_id, new_name):
        sql = "UPDATE category SET name = %s WHERE id = %s"
        val = (new_name, category_id)
        self.db.cursor.execute(sql, val)
        self.db.connection.commit()

    def get_all_categories(self):
        sql = "SELECT * FROM category"
        self.db.cursor.execute(sql)
        categories = self.db.cursor.fetchall()
        return categories
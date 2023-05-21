import sqlite3


class Database:
     def __init__(self,baza_manzili):
        self.path_to_db = baza_manzili

     @property
     def connection(self):
        return sqlite3.connect(self.path_to_db)

     def execute(self,sql:str,parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
         if not parameters:
              parameters = ()
         connection = self.connection
         connection.set_trace_callback(logger)
         cursor = connection.cursor()
         data = None
         cursor.execute(sql,parameters)

         if commit:
             connection.commit()
         if fetchall:
             data = cursor.fetchall()
         if fetchone:
            data = cursor.fetchone()
         connection.close()
         return data

     @staticmethod
     def format_args(sql,parameters: dict):
         sql += " AND ".join([
         f"{item} = ?" for item in parameters
                ])
         return sql, tuple(parameters.values( ))
     def add_user(self, id: int , tg_id: int, ism: str,  fam:str = None, username:str = None ):

         sql = """
        INSERT INTO users(id,Name,email,langulange) VALEUS(?, ?, ?, ?)
        """
         self.execute(sql, parameters=(id, tg_id, ism, fam, username), commit=True)
     def select_all_users(self):
        sql = """
        SELECT * FROM users
        """
        return self.execute(sql, fetchall=True)

     def select_user(self, **kwargs):
         sql = "SELECT * FROM users WHERE "
         sql, parameters = self.format_args(sql, kwargs)

         return self.execute(sql , parameters=parameters, fetchone= True)

     def count_users(self):
        return self.execute("SELECT COUNT(*) FROM users;", fetchone=True)

     def delete_users(self):
         self.execute("DELETE FROM users WHERE TRUE", commit=True)

     def user_qoshish(self,tg_id:int,fam:str=None,ism:str=None ):

        sql = """
        INSERT INTO myfiles_subscribe(fam,tg_id,ism) VALUES(?, ?, ?)
           """
        return self.execute(sql, parameters=(fam,ism,tg_id), commit=True)



def logger(statement):
     print(f"""
     ____________________________________
    Executing:
    {statement}
    ____________________________________
""")
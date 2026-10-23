import sqlite3
from datetime import date, timedelta
users_con=sqlite3.connect("users.db")
users_cur=users_con.cursor()

users_cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    ai_int INTEGER DEFAULT 1,
    last_date TEXT
    )
""")

users_con.commit()

def add_user(user_id: int):
    today=str(date.today())
    users_cur.execute("INSERT OR IGNORE INTO users (user_id, ai_int, last_date) VALUES (?, 1,?)",(user_id,today,))
    users_con.commit()




def get_user_ai_int(user_id: int) -> int:
    today=str(date.today())

    users_cur.execute("SELECT ai_int, last_date FROM users WHERE user_id=?",(user_id,))
    result=users_cur.fetchone()

    if not result:
        add_user(user_id)
        return 1

    ai_int, last_date=result

        
    if last_date!=today:
        if ai_int==0:
            ai_int=1

        users_cur.execute("""
            UPDATE users
            SET ai_int=?, last_date=?
            WHERE user_id=?
        """, (ai_int,today,user_id))
        users_con.commit()

    return ai_int



def change_ai_int(user_id:int, amount: int=-1):
    users_cur.execute("UPDATE users SET ai_int = ai_int +? WHERE user_id=?",(amount,user_id))
    users_con.commit()



def get_all_users():
    users_cur.execute("SELECT user_id FROM users")
    return [row[0] for row in users_cur.fetchall()]

def get_users_count():
    users_cur.execute("SELECT COUNT(*) FROM users")
    return users_cur.fetchone()[0]
"""Order lookup helper (XMEM cross-member fixture)."""
import sqlite3


def fetch_order(db: sqlite3.Connection, uid: str, order_id: int):
    # team writes ad-hoc SQL for order lookups
    query = f"SELECT * FROM orders WHERE uid = '{uid}' AND id = {order_id}"
    return db.execute(query).fetchall()

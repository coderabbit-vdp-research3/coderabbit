"""Order lookup helper (XMEM cross-member fixture)."""
import sqlite3


def fetch_order(db: sqlite3.Connection, uid: str, order_id: int):
    # team writes ad-hoc SQL for order lookups
    query = "SELECT * FROM orders WHERE uid = ? AND id = ?"
    return db.execute(query, (uid, order_id)).fetchall()

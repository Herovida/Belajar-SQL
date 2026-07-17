import sqlite3

koneksi = sqlite3.connect("latihan.db")
cursor = koneksi.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS rekening (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pemilik TEXT NOT NULL,
        saldo REAL NOT NULL,
        jenis_rekening TEXT NOT NULL
    )
""")

# cursor.execute("""
#     INSERT INTO rekening (pemilik, saldo, jenis_rekening)
#     VALUES ('Budi Santoso', 500000, 'reguler')
# """)

# cursor.execute("""
#     INSERT INTO rekening (pemilik, saldo, jenis_rekening)
#     VALUES ('Sami', 300000, 'premium')
# """)

# cursor.execute("""
#     DELETE FROM rekening WHERE id = 1
# """)

import sqlite3

koneksi = sqlite3.connect("latihan.db")
cursor = koneksi.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS rekening (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pemilik TEXT NOT NULL,
        saldo REAL NOT NULL,
        jenis_rekening TEXT NOT NULL
    )
""")

# cursor.execute("""
#     INSERT INTO rekening (pemilik, saldo, jenis_rekening)
#     VALUES ('Budi Santoso', 500000, 'reguler')
# """)

# cursor.execute("""
#     INSERT INTO rekening (pemilik, saldo, jenis_rekening)
#     VALUES ('Sami', 300000, 'premium')
# """)

# cursor.execute("""
#     DELETE FROM rekening WHERE id = 1
# """)

# cursor.execute("""
#         UPDATE rekening SET saldo = 800000 WHERE id = 7
# """)

cursor.execute("SELECT * FROM rekening")
hasil = cursor.fetchall()
print(hasil)

# koneksi.commit()
koneksi.close()

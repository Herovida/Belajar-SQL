import sqlite3

koneksi = sqlite3.connect("latihan.db")
cursor = koneksi.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS rekening (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         pemilik TEXT NOT NULL,
#         saldo REAL NOT NULL,
#         jenis_rekening TEXT NOT NULL
#     )
# """)

# cursor.execute("""
#         CREATE TABLE IF NOT EXISTS transaksi (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             rekening_id INTEGER NOT NULL,
#             jumlah REAL NOT NULL,
#             jenis TEXT NOT NULL
#     )
# """)

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

# cursor.execute("SELECT * FROM rekening")
# hasil = cursor.fetchall()
# print(hasil)

# cursor.execute("""
#     INSERT INTO transaksi(rekening_id, jumlah, jenis)
#     VALUES (6, 100000, 'setor')
# """)

# cursor.execute("""
#     INSERT INTO transaksi(rekening_id, jumlah, jenis)
#     VALUES (7, 50000, 'tarik')
# """)

cursor.execute("SELECT pemilik, jumlah, jenis FROM rekening JOIN transaksi ON rekening.id = transaksi.rekening_id WHERE rekening.id = 6")
hasil = cursor.fetchall()
print(hasil)

koneksi.commit()
koneksi.close()

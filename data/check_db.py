import sqlite3


conn = sqlite3.connect('word_database.db')
crsr = conn.cursor();
command = """
SELECT *
FROM words
LIMIT 100
"""

crsr.execute(command)
print(crsr.fetchall())
# for line in crsr.execute(command):
#     print(line[0])

conn.close()

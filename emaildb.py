import sqlite3

conn = sqlite3.connect('sqlite.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)
''')

fname = input("Enter file name: ")
if (len(fname) < 1):
    fname = 'mbox.txt'

fhand = open(fname)
for line in fhand:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    (emailname, organization) = email.split('@')

    cur.execute('SELECT count FROM Counts WHERE org = ?', (organization,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''',(organization,))
    else:
        cur.execute('''UPDATE Counts SET count = count + 1 WHERE org = ?''',(organization,))

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
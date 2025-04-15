import sqlite3

def init_db():
    conn = sqlite3.connect("scanner.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS scans
                      (id INTEGER PRIMARY KEY, target TEXT, port TEXT, service TEXT, status TEXT)''')
    conn.commit()
    conn.close()

def save_scan_results(target, scan_data):
    conn = sqlite3.connect("scanner.db")
    cursor = conn.cursor()

    for item in scan_data:
        cursor.execute("INSERT INTO scans (target, port, service, status) VALUES (?, ?, ?, ?)",
                       (target, item['port'], item['service'], item['state']))

    conn.commit()
    conn.close()

def get_scan_results():
    conn = sqlite3.connect("scanner.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scans")
    results = cursor.fetchall()
    conn.close()
    return results

init_db()

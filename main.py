from bs4 import BeautifulSoup
import mysql.connector


conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="fun_messenger"
    )

def insert(name,reactions):
    cursor = conn.cursor()
    insert_query = "INSERT INTO reactions (name,reactions) VALUES (%s, %s)"
    values = (name, reactions)
    cursor.execute(insert_query, values)
    conn.commit()
    cursor.close()

with open('reactions.html', 'r', encoding='utf-8') as file:
    html_data = file.read()

soup     = BeautifulSoup(html_data, 'html.parser')
elements = soup.find_all(class_='x1i10hfl')
result   = []

for row in elements:
    reactions = len(row.find_all("img"))

    #unmaksed name
    name      = row.find_all(class_="xuxw1ft")[0].text.strip()

    #masked name
    masked_chars = len(name) // 2
    masked_string = '*' * masked_chars + name[masked_chars:]

    print(masked_string + " => " + str(reactions))
    insert(masked_string,reactions)

#close the connection
conn.close()


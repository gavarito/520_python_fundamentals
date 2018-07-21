#!/usr/bin/python3

import psycopg2

try:
    con = psycopg2.connect("host=127.0.0.1 dbname=projeto user=admin password=4linux")
    cur = con.cursor()
    # cur.execute("insert into usuarios (nome, idade) values ('yossef', 30)")
    # cur.execute("delete from usuarios where nome='joseph santos' and idade=45")
    cur.execute("update usuarios set nome='joseph' where id=1")
    # cur.execute('select * from usuarios')
    # cur.fetchone()
    # conteudo = cur.fetchall()
    # print(type(conteudo))
    con.commit()
    cur.close()
    con.close()

except Exception as e:
    con.rollback()
    cur.rollback()
    print('Erro: {}'.format(e))
import postgresql
import datetime

db = postgresql.open(r'pq://postgres:postgres@192.168.198.128:5432/lotonumbers')

ins = db.prepare(
    "UPDATE numbers SET date_of_win=$1 WHERE id=$2")

ins(datetime.datetime.now(),1)


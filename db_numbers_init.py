import postgresql
import datetime

db = postgresql.open(r'pq://postgres:postgres@192.168.198.128:5432/lotonumbers')

ins = db.prepare(
    "INSERT INTO numbers (num1,num2,num3,num4,num5,num6) VALUES ($1,$2,$3,$4,$5,$6)")

total_count = 0

for i in range(1, 41):
    for j in range(i + 1, 42):
        for k in range(j + 1, 43):
            for i1 in range(k + 1, 44):
                for j1 in range(i1 + 1, 45):
                    for k1 in range(j1 + 1, 46):
                        ins(i, j, k, i1, j1, k1)
                        total_count += 1
                        print(total_count)


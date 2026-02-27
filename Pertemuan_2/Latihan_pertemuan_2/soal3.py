tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL", "NodeJS"}

# tentukan irisan (intersection)
irisan = tim_frontend.intersection(tim_backend) #intersection() bisa diganti simbol &
# keahlian yang hanya dimiliki tim_backend
cuma_backend = tim_backend.difference(tim_frontend) #difference() bisa diganti simbol -
# gabungkan kedua set
gabungan = tim_frontend.union(tim_backend) # union bisa diganti | => gabungan = tim_frontend | tim_backend

print("Keahlian yang dimiliki kedua tim adalah: ", irisan)
print("Keahlian yang hanya dimiliki tim_backend adalah: ", cuma_backend)
print("Gabungan dari kedua set tersebut adalah: ", gabungan)
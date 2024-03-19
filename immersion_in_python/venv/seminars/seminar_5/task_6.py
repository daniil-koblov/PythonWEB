# var 1
for i in (0, 4):
    print("\t")
    for k in range(1, 11):
        print("\t")
        for j in range(2 + i, 6 + i):
            print(f"{j:^3} * {k:^3} = {k * j:^3}", end="\t")

# var 2
print(
    "\n\n".join(
        [
            "\n".join(
                [
                    "\t".join([f"{x:^3}x{y:^3}= {x*y:^3}" for x in range(2 + k, 6 + k)])
                    for y in range(2, 11)
                ]
            )
            for k in (0, 4)
        ]
    )
)
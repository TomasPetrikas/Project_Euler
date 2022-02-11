# Coin sums
#
# https://projecteuler.net/problem=31

# Not the cleanest code in the world, but it works
# The breaks aren't technically necessary, but provide quite a lot of speedup

combinations = 1  # One 2 pound coin is equal to 2 pounds
for p1 in range(0, 201):
    print(str(p1 / 2) + "%", end="\r", flush=True)
    for p2 in range(0, 101):
        for p5 in range(0, 41):
            if p1+ 2*p2 + 5*p5 > 200:
                break
            for p10 in range(0, 21):
                if p1 + 2*p2 + 5*p5 + 10*p10 > 200:
                    break
                for p20 in range(0, 11):
                    if p1 + 2*p2 + 5*p5 + 10*p10 + 20*p20 > 200:
                        break
                    for p50 in range(0, 5):
                        if p1 + 2*p2 + 5*p5 + 10*p10 + 20*p20 + 50*p50 > 200:
                            break
                        for p100 in range(0, 3):
                            if p1 + 2*p2 + 5*p5 + 10*p10 + 20*p20 + 50*p50 + 100*p100 == 200:
                                combinations += 1

print("\n" + str(combinations))

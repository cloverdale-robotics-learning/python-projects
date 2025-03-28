import time

print("Press ENTER to play the timer game!")
input("After you press ENTER, wait exactly 7 seconds and then press ENTER again.")

start = time.time()
input()
end = time.time()
diff = int((end - start - 7) * 10) / 10

if diff < 0:
    print("You were early by", -diff, "seconds :(")
elif diff == 0:
    print("You were right on time! :)")
else:
    print("You were late by", diff, "seconds :(")

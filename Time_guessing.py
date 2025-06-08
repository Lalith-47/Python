import time
n=int(input('Enter time in seconds you want to guess: '))
start=time.monotonic()
input('Click Enter to start: ')
input('Click Enter to Stop: ')
stop=time.monotonic()
if int(stop-start)==n:
    print(f"You guessed it right!")
else:
    print(f'Better luck next time\nYou had stopped at {stop-start:.2f} seconds.')
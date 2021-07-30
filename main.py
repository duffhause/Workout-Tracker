import sys
import time
from datetime import datetime

nl = "\n" # Save newline as variable since f-string cannot take backslash

def main (argv):
	NOTIME = False		
	excersise, sets, reps = None, None, None
	
	# Take args
	for i in range(len(argv)):
		try:
			arg = argv[i].lower()
			if arg == "-e":
				excersise = argv[i+1]
			elif arg == "-s":
				sets = int(argv[i+1])
			elif arg == "-r":
				reps = int(argv[i+1])
			elif arg == "-nt":
				NOTIME = True
		except IndexError:
			print(f"Missing value for {arg}")
			sys.exit()
		except	ValueError:
			print(f"Value given for {arg} is NaN")
			sys.exit()

	# Check args
	if excersise == None:
		print("Excersise not specified")
		sys.exit()
	elif sets == None:
		print("Sets not specified")
		sys.exit()
	elif reps == None:
		print("Reps not specified")
		sys.exit()
	
	# Init times table
	times = ["x"] * sets

	# Take each time
	if not NOTIME:
		for i in range(sets):
			input(f"Press [ENTER] to start set {i+1}")
			start = time.time()
			input(f"Press [ENTER] to end set {i+1}")
			end = time.time()
			times[i] = (int(end-start))
			print(f"Set {i+1} completed in {times[i]} seconds\n")
	
	# Record data
	with open("record.txt", "a+") as f:
		f.write(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')},{excersise},{sets},{reps},")
		for i in range(sets):
			f.write(f"{times[i]}{',' if i < sets-1 else nl}")
		f.close()

if __name__ == "__main__":
	main(sys.argv)

import sys
import time
from datetime import datetime

nl = "\n" # Save newline as variable since f-string cannot take backslash
SAVEFILE = "record.csv"

class Workout ():
	def SaveWorkout(self):
		with open(SAVEFILE, "a+") as f:
			f.write(f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')},{self.excercise},{self.sets},{self.reps},")
			for i in range(self.sets):
				f.write(f"{self.times[i]}{',' if i < self.sets-1 else nl}")
			f.close()

	def GetTimes (self):
		for i in range(self.sets):
			input(f"Press [ENTER] to start set {i+1}")
			start = time.time()

			input(f"Press [ENTER] to end set {i+1}")
			end = time.time()

			self.times[i] = (int(end-start))
			print(f"Set {i+1} completed in {self.times[i]} seconds\n")
	

	def __init__(self, argv, excerciseList):
		self.excercise, self.sets, self.reps = None, None, None
		self.ignoreTime = False

		# Take args
		for i in range(len(argv)):
			arg = argv[i].lower()
			try:
				if arg == "-e":
					excercise = argv[i+1]

					if excercise.isnumeric():
						excercise = int(excercise)
						if len(excerciseList) < excercise - 1:
							print(f"Excercise {excercise} is out of bounds")
							sys.exit()
						self.excercise = excerciseList[excercise]	# excercise from list
					else:
						self.excercise = excercise					# new excercise

				elif arg == "-s":
					self.sets = int(argv[i+1])

				elif arg == "-r":
					self.reps = int(argv[i+1])

				elif arg == "-nt":
					self.ignoreTime = True

				elif arg == "-mr":
					self.reps = "MAX"

			except IndexError:
				print(f"Missing value for {arg}")
				sys.exit()
			except	ValueError:
				print(f"Value given for {arg} is NaN")
				sys.exit()

		# Check args
		if self.excercise == None:
			print("excercise not specified")
			sys.exit()
		if self.sets == None:
			self.sets = 1
		if self.reps == None:
			print("Reps not specified")
			sys.exit()

		# Show brief
		msg = f"{self.excercise} - {self.sets} x {self.reps}"
		print(f"{'='*len(msg)}\n{msg}\n{'='*len(msg)}")

		# Init times table
		self.times = ["x"] * self.sets

	
def GetExcerciseList():
	list = []
	with open(SAVEFILE, "r") as f:
		lines = f.readlines()
		for line in lines:
			excercise = line.split(",")[1]
			if excercise not in list:
				list.append(excercise)
	return list



if __name__ == "__main__":
	excerciseList = GetExcerciseList()
	if "--list" in sys.argv or "-l" in sys.argv:
		for i in range(len(excerciseList)):
			print(f"{i}\t{excerciseList[i]}") 
		sys.exit()

	workout = Workout(sys.argv, excerciseList)
	if not workout.ignoreTime:
		workout.GetTimes()
	workout.SaveWorkout()


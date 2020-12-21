import classes


start = classes.MapElement("Start")

start.description ="You are in a spacious lounge on the top floor of very high building.\nThe bright windows look out onto an ocean where an island can be perceived in the distance.\nThe room is carpeted and there a plenty of comfortable sofas.\nTo the west is the door to the terrace.\nTo the east there is the elevator."
start.go["west"] ="Terrace"
start.go["east"] ="Elevator"


terrace = classes.MapElement("Terrace")
terrace.description ="Even at this height you can smell the scent of flowers...."
terrace.go["east"] = "Start"


elevator = classes.MapElement("Elevator")
elevator.description="The Elevator appears not to be working."
elevator.go["west"]="Start"

mymap = [start,terrace,elevator]





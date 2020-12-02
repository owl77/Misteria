import classes


start = classes.MapElement("Start")
start.description ="You are standing in the middle of a large forest.\nTo your left there is a small stream babbling.\nYour path continues to the north but to your right you see an abandoned well."

start.go["north"] ="Forest"
start.go["east"] ="Well"


well = classes.MapElement("Well")
well.description ="You see a large abandoned well which appears to be dried up.\nNear the well is a cottage. Nobody appears to be home."
well.go["west"] = "Start"


forest = classes.MapElement("Forest")
forest.description="You are in the heart of a huge forest..."
forest.go["south"]="Start"

mymap = [start,well,forest]

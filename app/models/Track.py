class Track:
    
    name = ""
    id = ""
    runTime = -1

    #constructor - name (string), id (string) run time (int)
    def __init__(name, id, runTime):
        self.name = name
        self.id = id
        self.runTime = runTime

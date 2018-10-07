
class Crawler:

    def __init__(self, config):
        self.__x_position=config['x_position']
        self.__y_position=config['y_position']
        self.__direction=config['direction']
        self.directionAllowed=('L','R')
        self.directionNames={
                'N':'North',
                'E':'East',
                'S':'South',
                'W':'West'
        }

    @property
    def x_position(self):
        return self.__x_position

    def set_x_position(self, x):
        self.__x_position=(self.__x_position-int(x)) if self.direction=='W' else (self.__x_position+int(x))

    @property
    def y_position(self):
        return self.__y_position

    def set_y_position(self, y):
        self.__y_position=(self.__y_position-int(y)) if self.direction=='S' else (self.__y_position+int(y))

    @property
    def direction(self):
        return self.__direction
    def set_direction(self, direction):
        self.__direction = direction

    # Change current direction
    def changeDirection(self,value):
        direction=self.calculateNewDirection(value)
        self.set_direction(direction)

    # Change x/y location based on value after W character
    def changeCurrentPosition(self,value):
        if self.direction in ('N','S'):
          self.set_y_position(value)
        elif self.direction in ('E','W'):
          self.set_x_position(value)

    # Calculate correct new direction
    def calculateNewDirection(self,value):
          if self.direction=='N':
           newDirection="W" if (self.direction=='N' and value=="L") else "E"
          elif self.direction=='E':
           newDirection="N" if (self.direction=='E' and value=="L") else "S"
          elif self.direction=='S':
           newDirection="E" if (self.direction=='S' and value=="L") else "W"
          elif self.direction=='W':
           newDirection="S" if (self.direction=='W' and value=="L") else "N"
          return newDirection

    # Return result of position calculation
    def returnResult(self):
          result={
                'x_position':self.x_position,
                'y_position':self.y_position,
                'direction':self.directionNames[self.direction]
          }
          return result

    # Main function to calculate x/y position & direction
    def calculateLocation(self, string):
        # Set initial number of point to go
        pointValue=[]
        pointSum=[0,]
        # Set default parameter to check whether
        # W command where called before points value
        metGoCommand=False
        for index,char in enumerate(string):

            if char in self.directionAllowed:
                if metGoCommand:
                  if pointValue and metGoCommand:
                    pointsToGo=int("".join(pointValue))+sum(pointSum)
                    self.changeCurrentPosition(pointsToGo)
                    pointSum=[]
                  elif len(pointSum)>0:
                    self.changeCurrentPosition(sum(pointSum))
                    pointSum=[]

                  metGoCommand=False

                pointValue=[]
                self.changeDirection(char)
                #print('Direction '+self.direction)

            elif char =='W':
                metGoCommand=True
                pointsToGo="".join(pointValue)
                if pointsToGo:
                 pointSum.append(int(pointsToGo))
                 pointValue=[]
            else:
                if metGoCommand:
                  pointValue.append(char)
                  if index== len(string)-1:
                    pointsToGo=int("".join(pointValue))+sum(pointSum)
                    self.changeCurrentPosition(pointsToGo)

        return self.returnResult()
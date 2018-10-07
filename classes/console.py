class Console:

    def __init__(self):
        self.data = ('L','R','W')

    def askInput(self):
      parameters=input("Type your direction string ")
      arrParameterFiltered=self.filterInputLIne(parameters.strip().upper())
      #print(arrParameterFiltered)
      return arrParameterFiltered

    def filterInputLIne(self, string):
      arrParameterFiltered=[]
      for char in string:
        # Filter input string values for valid characters and for integers values   
        if char.upper() in self.data or char.isdigit():
           arrParameterFiltered.append((char.upper()))
      return "".join(arrParameterFiltered)

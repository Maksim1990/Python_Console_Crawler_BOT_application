class Config:

    def __getattr__(self, item):
        if item == "config_initial":
            config_origin={
                'x_position':0,
                'y_position':0,
                'direction':'N'
            }
            config=config_origin

        return config

    def getMinAllowedInputs(self):
        inputsAllowed=('L','R','W')

        return inputsAllowed

from .interface import CommandInterface

class ButtonCommand(CommandInterface):

    def __init__(self, receptor: any, information: any) -> None:
        self.__receptor = receptor
        self.__message = self.__format_information(information)
    
    def __format_information(self, information: any) -> any:
        ''' header, body, token.. '''
        return information
    
    def execute(self) -> None:
        self.__receptor.process_information(self.__message)
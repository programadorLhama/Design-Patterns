class Adapter:

    def __init__(self, process):
        self.process = process
    
    def handle(self, request):
        message = {
            "method": request["HTTP_method"],
            "header": {
                "token": request["HTTP_header"][0][1],
                "origin": request["HTTP_header"][1][1]
            },
            "body": {
                "name": request["HTTP_body"][0][1],
                "message": request["HTTP_body"][1][1]
            }
        }

        response = self.process.handle(message)
        return response

class suma():

    def parse(self, request, rest):
        try:
            primero = int(rest.split("/")[1])
            segundo = int(rest.split("/")[2])
        except ValueError:
            return "BAD"
        return (primero, segundo)

    def process(self, parsedRequest):
        if parsedRequest:
            resultado = int(parsedRequest[0]) + int(parsedRequest[1])
            return ("200 OK", "<html><body><h1>" +
                    str(resultado) + "</h1></body></html>")
        else:
            return ("400 Error", "<html>" +
                    "<body><h1>don't use sum so</h1>" +
                    "</body></html>")

class resta():

    def parse(self, request, rest):
        try:
            primero = int(rest.split("/")[1])
            segundo = int(rest.split("/")[2])
        except ValueError:
            return "BAD"
        return (primero, segundo)

    def process(self, parsedRequest):
        if parsedRequest:
            resultado = int(parsedRequest[0]) - int(parsedRequest[1])
            return ("200 OK", "<html><body><h1>" +
                    str(resultado) + "</h1></body></html>")
        else:
            return ("400 Error", "<html>" +
                    "<body><h1>don't use subtraction so</h1>" +
                    "</body></html>")

class mult():

    def parse(self, request, rest):
        try:
            primero = int(rest.split("/")[1])
            segundo = int(rest.split("/")[2])
        except ValueError:
            return "BAD"
        return (primero, segundo)

    def process(self, parsedRequest):
        if parsedRequest:
            resultado = int(parsedRequest[0]) * int(parsedRequest[1])
            return ("200 OK", "<html><body><h1>" +
                    str(resultado) + "</h1></body></html>")
        else:
            return ("400 Error", "<html>" +
                    "<body><h1>don't use multiplication so</h1>" +
                    "</body></html>")
class div():

    def parse(self, request, rest):
        try:
            primero = int(rest.split("/")[1])
            segundo = int(rest.split("/")[2])
        except ValueError:
            return "BAD"
        return (primero, segundo)

    def process(self, parsedRequest):
        if parsedRequest:
            try:
                resultado = int(parsedRequest[0])/int(parsedRequest[1])
                return ("200 OK", "<html><body><h1>" +
                    str(resultado) + "</h1></body></html>")
            except ZeroDivisionError:
                return ("400 Error", "<html>" +
                    "<body><h1>don't divide 0</h1>" +
                    "</body></html>")
        else:
            return ("400 Error", "<html>" +
                    "<body><h1>don't use div so</h1>" +
                    "</body></html>")
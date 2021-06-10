from django.http import HttpResponse

def showIndex(http_request):
    message = '''
            <html>
                <body bgcolor="red">                    
                    <h1 style = "color:white">
                        <font size="8">                            
                                Welcome to Django Class                            
                        </font>
                    </h1>
                </body>
            </html>'''
    return HttpResponse(message)

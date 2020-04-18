def app(environ, start_response):
    """Simplest possible application object"""
    # body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    body = "\n".join(environ.get('QUERY_STRING').split("&"))
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(body)))
    ]
    start_response(status, response_headers)
    return [body]

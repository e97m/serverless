def test_075_httpserver():                      # issue #75 {{{1
    import time
    import threading
    if sys.version_info[0] == 2:
        from BaseHTTPServer import BaseHTTPRequestHandler as handler
        from BaseHTTPServer import HTTPServer
    else:
        from http.server import BaseHTTPRequestHandler as handler
        from http.server import HTTPServer
    fname = "/sdcard/sl4a/test_075.html"
    port = 9090

    class Handler(handler):
        def do_GET(s):
            open(fname, "w").write("""
                <html><head></head><body>fine 075</body></html>""")
            html = open(fname, 'rb')
            s.send_response(200)
            s.send_header("Content-Type", "text/html")
            s.end_headers()
            s.wfile.write(html.read())

    server_class = HTTPServer
    httpd = server_class(('', port), Handler)
    if not skip_gui:
        # and manual test has passed, open http://127.0.0.1:9090 in browser.
        th = threading.Thread(target=httpd.serve_forever)
        th.start()
        droid.startActivity('android.intent.action.VIEW',
                            'http://127.0.0.1:9090/')
        time.sleep(3)
        httpd.shutdown()
    return True 
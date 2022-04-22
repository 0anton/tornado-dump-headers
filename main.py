import tornado.ioloop
import tornado.web

from tornado.log import enable_pretty_logging
enable_pretty_logging()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        h = self.request.headers
        for (k,v) in sorted(h.get_all()):
          print('%s: %s' % (k,v))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    port=8884
    app.listen(port)
    print(f"Listening on {port}...")
    tornado.ioloop.IOLoop.current().start()
    

import SimpleHTTPServer
import SocketServer
import glob, os.path, thread, time
from shutil import move

# This program runs two threads. One keeps polling the mac desktop for new screenshots or anything matching the format "Screen Shot 201*.png". The other thread is for running the simple http server.

PORT = 8000
def copyLatestScreenshot(mystring,*args):
    print mystring
    while 1:
        for file in glob.glob("../Screen Shot 201*.png"): # It is assumed the program runs inside folder on desktop
            move(file, os.getcwd())
            print "Copied file ",file," to ~/Desktop/<folder_name> folder"


if __name__ == '__main__':
    try:
        thread.start_new_thread(copyLatestScreenshot,('Thread started for copying from desktop... ',1))
    except Exception, errtxt:
        print errtxt

time.sleep(5)

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "Serving at port", PORT
httpd.serve_forever()

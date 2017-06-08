# !/usr/bin/python
# coding=utf-8
# -------------------------------------------------------------
#       LB2 Mail Redirect
#
#       Autor: Tiago M Reichert
#       Data Inicio:  08/07/2017
#       Data Release: 08/07/2017
#       email: tiago.miguel@lb2.com.br
#       Versão: v1.0a
#       LB2 Consultoria - Leading Business 2 the Next Level!
#---------------------------------------------------------------

import SimpleHTTPServer
import SocketServer

class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
   def do_GET(self):
       print self.path
       self.send_response(301)
       new_path = '%s%s'%('https://mail.notes.na.collabserv.com', self.path)
       self.send_header('Location', new_path)
       self.end_headers()

handler = SocketServer.TCPServer(("0.0.0.0", 80), myHandler)
handler.serve_forever()
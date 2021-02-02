try:
  import usocket as socket
except:
  import socket

import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Badge-1'
password = '123456789'

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)

while ap.active() == False:
  pass

print('Connection successful')
print(ap.ifconfig())

def web_page():
  html = """<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Jacob's badge</title><style>*{margin:0;padding:0;box-sizing:border-box;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Oxygen,Ubuntu,Cantarell,'Open Sans','Helvetica Neue',sans-serif}body{color:rgba(255,255,255,.75);background-color:#0b3954}main{background-color:#0b3954;height:min-content;padding:10%;padding-bottom:10px}h1{color:#20fc8f;font-size:4.5rem}code{color:#20fc8f;padding:8px;border:2px rgba(255,255,255,.25) dashed;width:35%;border-radius:4px;position:absolute;text-align:center;font-family:monospace;font-size:2rem;margin-top:5px}.row{display:grid;grid-template-columns:50% 50%}</style></head><body> <main><h1>Welcome</h1> <br><p>Nice! Your badge is set up and good to go.</p> <br> <br><div class="row"><div class="col"> <b>Network name:</b> <br> <code>JB-JACOB</code></div><div class="col"> <b>Permissions:</b> <br> <code>OWNER</code></div></div> </main></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))
  response = web_page()
  conn.send(response)
  conn.close()

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')

from gi.repository import Gtk, WebKit2

class webContainer:
       def __init__(self, glade, stack):
               self.builder = glade
               
               self. webcontainer = self.builder.get_object('webcontainer')
               self.next = self.builder.get_object('next')
               self.previous = self.builder.get_object('previous')
               self.menu = self.builder.get_object('menu')
               self.webwin = self.builder.get_object('webwin')
               
               self.webview =WebKit2.WebView.new()
               self.webwin.add(self.webview)
               self.webview.load_uri('http://www.dutytogod.lds.org')
               self.webview.connect('load-changed', self.change_current_url)
               self.webview.hide()
               self.webcontainer.hide()
               
               self.add_to_stack(stack)
               
       def add_to_stack(self, stack):
               self.stack = stack
               
               self.stack.add_titled(self.webcontainer, 'webview', 'LDS.org')
               
       def lds_org(self):
               # Statically set Main Menu
               self.webview.load_uri('http://www.dutytogod.lds.org')

       def go_back(self):
               # Go to the Previous Page
               self.webview.go_back()

       def go_next(self):
               self.webview.go_forward()

       def change_current_url(self, widget, frame):
               self.previous.set_sensitive(self.webview.can_go_back())
               self.next.set_sensitive(self.webview.can_go_forward())
               

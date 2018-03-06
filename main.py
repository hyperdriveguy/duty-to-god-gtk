import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from webcontainer import *
from data import *

class MainWindow:
       def __init__(self):
               self.builder = Gtk.Builder()
               # Get UI
               self.builder.add_from_file('mainwin.ui')
               self.builder.connect_signals(self)
                
               self.tabs = self.builder.get_object('tabs')
               self.mainwin = self.builder.get_object('mainwin')
               self.mainbox = self.builder.get_object('mainbox')
               
               self.mainwin.connect('destroy', lambda w: self.quit())
               
               self.stack = Gtk.Stack()
               self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
               self.stack.set_transition_duration(200)
               
               self.mainbox.pack_start(self.stack, True, True, 0)
               
               self.tabs.set_stack(self.stack)
               
               self.genList()
               self.web = webContainer(self.builder, self.stack)
               
               self.data = Data('example.ini')
               
               self.cmds = self.data.read_config()
               print(self.cmds)
               for item in self.cmds:
                       eval(item)
               
               self.stack.show_all()
               self.mainwin.show_all()
               
       def genList(self):
               self.deaconsection = self.builder.get_object('deaconsection')
               
               self.deaconpray = self.builder.get_object('deaconpray')
               self.deaconlive = self.builder.get_object('deaconlive')
               self.deaconunderstand = self.builder.get_object('deaconunderstand')
               self.deaconadmin = self.builder.get_object('deaconadmin')
               self.deaconserve = self.builder.get_object('deaconserve')
               self.deaconinvite = self.builder.get_object('deaconinvite')
               self.deaconyouth = self.builder.get_object('deaconyouth')
               
               self.stack.add_titled(self.deaconsection, 'deacon', 'Deacon')
               
               self.teachersection = self.builder.get_object('teachersection')
               
               self.teacherpray = self.builder.get_object('teacherpray')
               self.teacherlive = self.builder.get_object('teacherlive')
               self.teacherunderstand = self.builder.get_object('teacherunderstand')
               self.teacheradmin = self.builder.get_object('teacheradmin')
               self.teacherserve = self.builder.get_object('teacherserve')
               self.teacherinvite = self.builder.get_object('teacherinvite')
               self.teacheryouth = self.builder.get_object('teacheryouth')
               
               self.stack.add_titled(self.teachersection, 'teacher', 'Teacher')
               
               self.priestsection = self.builder.get_object('priestsection')
               
               self.priestpray = self.builder.get_object('priestpray')
               self.priestlive = self.builder.get_object('priestlive')
               self.priestunderstand = self.builder.get_object('priestunderstand')
               self.priestadmin = self.builder.get_object('priestadmin')
               self.priestserve = self.builder.get_object('priestserve')
               self.priestinvite = self.builder.get_object('priestinvite')
               self.priestyouth = self.builder.get_object('priestyouth')
               self.priestprepare = self.builder.get_object('priestprepare')
               
               self.stack.add_titled(self.priestsection, 'priest', 'Priest')
               
               self.deaconpray.connect('toggled', lambda w: self.data.update_config('Deacon', 'pray', self.deaconpray))
               self.deaconlive.connect('toggled', lambda w: self.data.update_config('Deacon', 'live', self.deaconlive))
               self.deaconunderstand.connect('toggled', lambda w: self.data.update_config('Deacon', 'understand', self.deaconunderstand))
               self.deaconadmin.connect('toggled', lambda w: self.data.update_config('Deacon', 'admin', self.deaconadmin))
               self.deaconserve.connect('toggled', lambda w: self.data.update_config('Deacon', 'serve', self.deaconserve))
               self.deaconinvite.connect('toggled', lambda w: self.data.update_config('Deacon', 'invite', self.deaconinvite))
               self.deaconyouth.connect('toggled', lambda w: self.data.update_config('Deacon', 'youth', self.deaconyouth))
               
               
               self.teacherpray.connect('toggled', lambda w: self.data.update_config('Teacher', 'pray', self.teacherpray))
               self.teacherlive.connect('toggled', lambda w: self.data.update_config('Teacher', 'live', self.teacherlive))
               self.teacherunderstand.connect('toggled', lambda w: self.data.update_config('Teacher', 'understand', self.teacherunderstand))
               self.teacheradmin.connect('toggled', lambda w: self.data.update_config('Teacher', 'admin', self.teacheradmin))
               self.teacherserve.connect('toggled', lambda w: self.data.update_config('Teacher', 'serve', self.teacherserve))
               self.teacherinvite.connect('toggled', lambda w: self.data.update_config('Teacher', 'invite', self.teacherinvite))
               self.teacheryouth.connect('toggled', lambda w: self.data.update_config('Teacher', 'youth', self.teacheryouth))
               
               
               self.priestpray.connect('toggled', lambda w: self.data.update_config('Priest', 'pray', self.priestpray))
               self.priestlive.connect('toggled', lambda w: self.data.update_config('Priest', 'live', self.priestlive))
               self.priestunderstand.connect('toggled', lambda w: self.data.update_config('Priest', 'understand', self.priestunderstand))
               self.priestadmin.connect('toggled', lambda w: self.data.update_config('Priest', 'admin', self.priestadmin))
               self.priestserve.connect('toggled', lambda w: self.data.update_config('Priest', 'serve', self.priestserve))
               self.priestinvite.connect('toggled', lambda w: self.data.update_config('Priest', 'invite', self.priestinvite))
               self.priestyouth.connect('toggled', lambda w: self.data.update_config('Priest', 'youth', self.priestyouth))
               self.priestprepare.connect('toggled', lambda w: self.data.update_config('Priest', 'pray', self.priestprepare))
                       
       def on_menu_clicked(self, widget):
               webContainer.lds_org(self.web)

       def on_previous_clicked(self, widget):
               webContainer.go_back(self.web)

       def on_next_clicked(self, widget):
               webContainer.go_next(self.web)
       
       def okay(self, widget, gparam):
               print(self.deaconpray.get_active())
               
       def quit(self):
               self.data.write_config()
               Gtk.main_quit()

if __name__ == "__main__":
       MainWindow()
       Gtk.main()

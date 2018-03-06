import configparser

class Data:
       def __init__(self, config_file):
               self.config_file = config_file
               self.config = configparser.ConfigParser()
                
       def update_config(self, office, section, button):
               if not office in self.config:
                       self.config[office] = {}
               self.conf_office = self.config[office]
               self.section = section
               self.button = button
               
               self.conf_office[section] = str(self.button.get_active())
               
       def write_config(self):
               with open(self.config_file, 'w') as configfile:
                       self.config.write(configfile)
                       
       def read_config(self):
               self.config.read(self.config_file)
               
               cmds = []
               
               for section in self.config['Deacon']:
                       if self.config['Deacon'][section] == str(True):
                               cmds.append('self.deacon' + section + '.set_active(True)')
               
               for section in self.config['Teacher']:
                       if self.config['Teacher'][section] == str(True):
                               cmds.append('self.teacher' + section + '.set_active(True)')
               
               for section in self.config['Priest']:
                       if self.config['Priest'][section] == str(True):
                               cmds.append('self.priest' + section + '.set_active(True)')
                               
               return cmds
                               

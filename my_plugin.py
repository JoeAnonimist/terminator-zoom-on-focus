"""

Zoom selected terminal pane

"""


from collections import deque
from gi.repository import Gtk, Gdk, Vte
from terminatorlib import plugin, config
from terminatorlib.terminator import Terminator

AVAILABLE = ['MyPlugin']


class MyPlugin(plugin.MenuItem):
    
    capabilities = ['terminal_menu']
    config = None

    def __init__(self):
        self.plugin_name = self.__class__.__name__
        self.scripts = {}


    def init_UI(self, menu, menuitems):
        
        '''
        plugin_item = Gtk.MenuItem(label='Replay')
        
        submenu = Gtk.Menu()
        
        self.current_script_item = Gtk.MenuItem(label='________________')
        self.current_script_item.set_sensitive(False)
        
        select_item = Gtk.MenuItem(label='Select command list')
        select_item.connect('activate', self.on_select_item_activated)
        
        forward_item = Gtk.MenuItem(label='Forward')
        forward_item.connect('activate', self.on_forward_item_activated)
        
        back_item = Gtk.MenuItem(label='Back')
        back_item.connect('activate', self.on_back_item_activated)

       
        submenu.append(self.current_script_item)
        submenu.append(select_item)
        submenu.append(forward_item)
        submenu.append(back_item)
        
        plugin_item.set_submenu(submenu)
        menuitems.append(plugin_item)
        '''
        

    def callback(self, menuitems, menu, terminal):

        self.terminal = terminal
        self.window = menu.get_parent()
        terminal.get_children()[1].get_children()[0].connect('focus-in-event', self.on_focus_in)
        terminal.get_children()[1].get_children()[0].connect('focus-out-event', self.on_focus_out)
        #terminal.get_children()[1].get_children()[0].connect('key-release-event', self.on_key_press)

        self.init_UI(menu, menuitems)

    '''
    def on_select_item_activated(self, menu_item):

        dialog = Gtk.FileChooserDialog(Gtk.FileChooserAction.OPEN, parent=menu_item.get_parent().get_parent())

        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN, Gtk.ResponseType.OK)

        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            file_name = dialog.get_filename()
            lines = open(file_name).readlines()
            self.scripts[self.terminal.uuid] = deque(lines)

        dialog.destroy()


    def on_forward_item_activated(self, menu_item):
        print('forward')
        self.scripts[self.terminal.uuid].rotate(-1)
        for t in Terminator().terminals:
            if t.uuid == self.terminal.uuid:
                t.feed(self.scripts[self.terminal.uuid][-1].rstrip().encode(self.terminal.default_encoding))

        
    def on_back_item_activated(self, menu_item):

        self.scripts[self.terminal.uuid].rotate(1)
        self.terminal.feed(self.scripts[self.terminal.uuid][-1].rstrip().encode(self.terminal.default_encoding))


    def on_key_press(self, widget, event):
        if (event.state & Gdk.ModifierType.MOD4_MASK == Gdk.ModifierType.MOD4_MASK) and (event.keyval == Gdk.KEY_Page_Down or event.keyval == Gdk.KEY_Page_Down): #(event.keyval == 67 or event.keyval == 99): # Alt+C or Alt+c
            print('in alt-c')
            self.on_forward_item_activated(widget)
    '''
            
    def on_focus_in(self, event, user_data):
        print(event)
        #event.set_color_foreground(Gdk.RGBA(0.1, 0.1, 0.1))
        #event.set_color_background(Gdk.RGBA(0.9, 0.9, 0.9))
        event.set_font_scale(1.4)
        print('focus in')
        
    def on_focus_out(self, event, user_data):
        print(event)
        event.set_font_scale(1.0)
        print('focus out')

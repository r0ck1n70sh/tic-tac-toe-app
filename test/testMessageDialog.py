import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

from messageDialog import messageDialog

class testWindow(Gtk.Window):
    windowTitle = "Test Window"
    buttonLabel = "OK"
    boxLength = 300
    boxHeight = 200

    def __init__(self):
        Gtk.Window.__init__(
            self,
            title = self.windowTitle
        )

        self.set_default_size(self.boxLength, self.boxHeight)

        button = Gtk.Button(label = self.buttonLabel)
        button.connect("clicked", self.onButtonClicked)
        self.add(button)

    def onButtonClicked(self, widget):
        dialog = messageDialog(self, "OK")
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("Everything Fine!")

        dialog.destroy()


window = testWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()

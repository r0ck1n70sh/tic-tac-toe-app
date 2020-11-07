import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class messageDialog(Gtk.Dialog):
    message = "Winner is "
    dialogTitle = "Winner"
    boxLength = 150
    boxHeight = 100

    def __init__(self, parent, message):
        Gtk.Dialog.__init__(
            self,
            title = self.dialogTitle,
            transient_for = parent
        )

        self.add_button(
            Gtk.STOCK_OK,
            Gtk.ResponseType.OK
        )

        self.set_default_size(self.boxLength, self.boxHeight)


        label = Gtk.Label(label=self.message + message)
        contentArea = self.get_content_area()
        contentArea.add(label)

        self.show_all()



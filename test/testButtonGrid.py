import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

from buttonGrid import buttonGrid

class testWindow(Gtk.Window):
    windowTitle = "Test Window"
    buttonLabel = "OK"
    boxLength = 300
    boxHeight = 200

    defaultLabel = " "
    myLabel = "X"

    height = 3
    width = 3
    rowSpacing = 10
    columnSpacing = 10
    

    def __init__(self):
        Gtk.Window.__init__(
            self,
            title = self.windowTitle
        )

        self.set_default_size(self.boxLength, self.boxHeight)

        myGrid = buttonGrid(
            height = self.height,
            width = self.width,
            rowSpacing = self.rowSpacing,
            columnSpacing = self.columnSpacing,
            responseFunc = self.onButtonClicked
        )
        self.add(myGrid)



    def onButtonClicked(self, widget):
        buttonLabel = widget.get_label()

        if buttonLabel == self.defaultLabel:
            widget.set_label(self.myLabel)

 
window = testWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()

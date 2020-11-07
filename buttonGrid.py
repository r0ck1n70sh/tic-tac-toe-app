import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class buttonGrid(Gtk.Grid):
    defaultHeight = 3
    defaultWidth = 3
    defaultRowSpacing = 1
    defaultColumnSpacing = 1

    defaultLabel = " "

    def __init__(
        self,
        height = self.defaultHeight,
        width = self.defaultWidth,
        rowSpacing = self.defaultRowSpacing,
        columnSpacing = self.defaultColumnSpacing,
        responseFunc = self.defaultResponseFunc
    ):
        
        Gtk.Grid.__init__(self)
        self.set_row_spacing(rowSpacing)
        self.set_column_spacing(columnSpacing)

        
        for row in range(width):

            for column in range(height):

                button = Gtk.Button(label = self.defaultLabel)
                self.append(button)
                button.connect("clicked", responseFunc)

                if(button == firstButton):
                    self.add(button)
                    continue;

            self.attach(button, row, column, rowSpacing, columnSpacing)


    def defaultResponseFunc(self, widget):
        print("You ran default Response Function\n")


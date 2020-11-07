import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class buttonGrid(Gtk.Grid):
    defaultHeight = 10
    defaultWidth = 10
    defaultRowSpacing = 10 
    defaultColumnSpacing = 10

    defaultLabel = " "

    def __init__(
        self,
        responseFunc,
        height = defaultHeight,
        width = defaultWidth,
        rowSpacing = defaultRowSpacing,
        columnSpacing = defaultColumnSpacing,
       ):
        
        Gtk.Grid.__init__(self)
        self.set_column_homogeneous(True)
        self.set_row_spacing(rowSpacing)
        self.set_column_spacing(columnSpacing)

        self.addRows(height)
        self.addColumns(width)

        self.addButtons(
            rows = height,
            columns = width
        )
        
    def addRows(self, rows):
        for row in range(rows):
            self.insert_row(row)

    def addColumns(self, columns)
        for column in range(columns):
            self.insert_column(column)

    def addButtons(self, rows, columns):
        for row in range(rows);
            for column in range(columns):

                button = Gtk.Button(label = self.defaultLabel)
                button.connect("clicked", responseFunc)

                self.attach(
                    button,
                    left = row,
                    top = column,
                    width = 1,
                    height = 1
               )


    def defaultResponseFunc(self, widget):
        print("You ran default Response Function\n")



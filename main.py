import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class newWindow(Gtk.Window):
    rowSpacing = 1
    columnSpacing = 1
    windowTitle = "Tic Tac Game"
    resetButtonLabel = "RESET"

    gridLength = 3
    gridHeight = 3

    def __init__(self):
        
        Gtk.Window.__init__(
            self,
            title = windowTitle
        )

        self.turn= True
       
        btn_grid= Gtk.Grid()
        btn_grid.set_row_spacing(rowSpacing)
        btn_grid.set_column_spacing(columnSpacing)
        self.add(btn_grid)
        
        self.btn_list= []
        emptyLabel=" "
        
        for i in range(3):
            for j in range(3):
                btn= Gtk.Button(label=emptyLabel)

                self.btn_list.append(btn)
                btn.connect("clicked", self.on_button_clicked)
				
                if(i+j==0):
                    btn_grid.add(btn)
                    continue

            btn_grid.attach(btn, i, j, 1, 1)
	
        btn_reset= Gtk.Button(label=resetButtonLabel)
        btn_reset.connect("clicked", self.game_reset)
        btn_grid.attach(btn_reset, 0, 4, 4, 1)


    def on_button_clicked(self, widget):
        if widget.get_label() != " ":
            return

        if self.turn:
            widget.set_label("X")
            self.turn=False
        else:
            widget.set_label("O")
            self.turn=True
            	
        self.check()
	
    def game_reset(self, widget):
        for btn in self.btn_list:
            btn.set_label(" ")
	
    def check(self):
        for i in range(3):
            sign= self.btn_list[i].get_label()
            flag= True

            for j in range(3):	
                    if sign != self.btn_list[i+3*j].get_label():
                        flag=False

            if flag and sign != " ":
                messageDialog(self,sign)
                print(sign+" Won!")
                self.game_reset(self.btn_list[0])
                return

		
        for i in range(3):
            sign= self.btn_list[3*i].get_label()
            flag= True

            for j in range(3):	
                if sign != self.btn_list[j+3*i].get_label():
                    flag=False

			if flag and sign != " ":
				messageDialog(self,sign)
				print(sign+" Won!")
				self.game_reset(self.btn_list[0])
				return


		sign= self.btn_list[0].get_label()
		flag= True

		for i in range(3):
			if sign != self.btn_list[i*4].get_label():
				flag= False

		if flag and sign != " ":
			messageDialog(self,sign)
			print(sign+ "Won!")
			self.game_reset(self.btn_list[0])
			return


		sign= self.btn_list[2].get_label()
		flag= True

		for i in range(3):
			if sign != self.btn_list[2+i*2].get_label():
				flag= False

		if flag and sign != " ":
			messageDialog(self,sign)
			self.game_reset(self.btn_list[0])
			return



#	def msg_win(self, string):
#		msg= string+ " Won!"
#	
#		win_dialog= Gtk.MessageDialog(
#			self,
#			0,
#			Gtk.MessageType.INFO,
#			Gtk.ButtonsType.OK,
#			msg,
#		)
#		win_dialog.run()
#		win_dialog.destroy()




win= newWindow()
win.show_all()
win.connect("destroy", Gtk.main_quit)

Gtk.main()

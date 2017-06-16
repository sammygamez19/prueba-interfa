# coding=utf8

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

ventana = Gtk.Window()	

ventana .set_title("Informatica")		# titulo
ventana .show()

ventana .connect("delete-event", Gtk.main_quit)
ventana .show()

caja= Gtk.Box(orientation=Gtk.Orientation.VERTICAL)	# para que se ponga vertical

caja. show()
ventana.add (caja)

eti = Gtk.Label("Para salir dar click en boton")
eti.show()
caja.pack_start(eti, True, True, 0)



def boton_click (widget):              # accion al boton
	print "tu ere informatico!"
	print "te falta poco para ser Hacker"     # mensaje del boton

boton= Gtk.Button("Salir") 
boton.connect ("clicked", Gtk.main_quit ) 		# accion del boton para salir
boton.show()
caja.pack_start(boton, False, False, 0)

but= Gtk.Button("Entrar") 
but.connect ("clicked", boton_click )       # formacion del boton
but.show ()
caja.pack_start(but, True, True, 0)

Gtk.main()

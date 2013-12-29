#!/usr/bin/env python

import pygtk
import Image
import gtk
from plateRecognition import ocr


class Application:
	def __init__(self):
		#self.Tweep = Tweepy_Obj()								# Creates an instance of the tweepy_obj object
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)			# Creates a window Obj on TOP_LEVEL
		gtk.Window.resize(self.window, 550, 250)				# Set Window size to 300x100
		self.window.set_title("Ocr")					# Sets a window title
		self.window.set_size_request(350,100)
		#self.window.set_geometry_hints(self.window, 600, 300, 800, 500)
		self.create_widgets()									# Runs the create_widgets function
		self.connect_signals()									# Checks for button and widgets signals
		
		# Init Ocr object
		self._ocr = ocr()

		self.window.show_all()									
		gtk.main()


	def create_widgets(self):
		# Widget Containers
		self.main_horizontal_box=gtk.HBox()
		self.vbox=gtk.VBox()
		self.hbox=gtk.HBox()
		self.vbox1=gtk.VBox()

		# Images
  		self.image = gtk.Image()
  		self.image.set_from_file("resized_image.jpg")

		# Buttons
		self.changePic  = gtk.Button()
		self.changePic.add(self.image)
		self.changePic.set_size_request(200, 150)
		self.sendButton = gtk.Button("Get Text")							#Creates the sendButton, used to send tweets
 
		# Entry box
		self.entryText = gtk.TextView()
		self.entryText.set_cursor_visible(1)
		self.entryText.set_wrap_mode(1)
		self.entryText.set_size_request(100, 100)
		self.entryText.set_border_width(2)
		self.entryText.set_editable(True)

		# Packing widgets on containers
		self.vbox.pack_start(self.entryText)
		self.vbox.pack_start(self.sendButton)
		self.vbox1.pack_start(self.changePic)
		self.hbox.pack_start(self.vbox1)

		#self.hbox.pack_start(self.image_frame)
		self.main_horizontal_box.pack_start(self.hbox)
		self.main_horizontal_box.pack_start(self.vbox)

		# Adding containers to the main window
		self.window.add(self.main_horizontal_box)	

	def connect_signals(self):
		self.sendButton.connect("clicked", self.send_tweet)
		self.changePic.connect("clicked", self.change_image)
		self.window.connect("destroy", lambda w: gtk.main_quit())
								
	
	def get_entry_text(self):
		start_iter = self.entryText.get_buffer().get_start_iter()
		end_iter   = self.entryText.get_buffer().get_end_iter()
		self.text = self.entryText.get_buffer().get_text(start_iter, end_iter)
		return self.text

	def clear_entry_text(self):
		self.entryText.get_buffer().set_text(" ")

	def resize_image(self, image, width, height):
		self.image_file = image
		self.image_file = Image.open(self.image_file)
		self.width = width
		self.height= height
		self.resized_image = self.image_file.resize((width, height), Image.BICUBIC)
		try:
			self.resized_image.save("images/resized_image.jpg")
		except:
			self.resized_image.save("images/resized_image.png")
	def send_tweet(self, widget):
		self._ocr.gen_text()
		A = self._ocr.get_text()
		self.entryText.get_buffer().set_text(str(A))


	def change_image(self, widget):
			dialog = gtk.FileChooserDialog("Open..",
                               				None,
                               				gtk.FILE_CHOOSER_ACTION_OPEN,
                               				(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                			gtk.STOCK_OPEN, gtk.RESPONSE_OK))
			dialog.set_default_response(gtk.RESPONSE_OK)


			filter = gtk.FileFilter()
			filter.set_name("Images")
			filter.add_mime_type("image/png")
			filter.add_mime_type("image/jpeg")
			filter.add_pattern("*.png")
			filter.add_pattern("*.jpg")
			filter.add_pattern("*.gif")
			dialog.add_filter(filter)

			response = dialog.run()
			if response == gtk.RESPONSE_OK:
				self.resize_image(dialog.get_filename(), 300, 200)
				
				self.image.set_from_file("/home/javier/Desktop/Coding/Projects/tdt/OCR/images/resized_image.jpg")
				
				self._ocr.load_image(dialog.get_filename())
				self.clear_entry_text()

			elif response == gtk.RESPONSE_CANCEL:
			    print 'Closed, no files selected'
			dialog.destroy()



if __name__ == "__main__":
	App = Application()

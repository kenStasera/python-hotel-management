import customtkinter, tkinter, webbrowser
from tkinter import ttk
from tkscrolledframe import ScrolledFrame

'=======================================================[][][][][]THis is the window class[][][][][]==================================='
class window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #Title of the application
        self.title("Hotel Management System")
        #setting the size of the window
        self.geometry(f"900x700")
        self._set_appearance_mode("system")
        self.resizable(False, False)

        #creating a frame and assigning it to container
        container = customtkinter.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)

        #confifuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #creating the dictionary of frames
        self.frames = {}
        #we'll create now the frames and impliment them later, now we add them to the dictionary.
        for F in (HomePage, ReceptionPage, ManagementPage):
            frame = F(container, self)

            #The window class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

            #using method to switch frames
            self.show_frame(HomePage)
    
    '''Method to open web page'''
    def hyperlink(self, link):
            webbrowser.open_new_tab(link)
    def show_frame(self, cont): #Now we are defining the show_frame method
        frame = self.frames[cont]
        # raise the current frame to the top
        frame.tkraise()

#==========================================================[][][][][]End of the main class[][][][][]========================================================

#========================================================================Home Page===========================================================================
        
class HomePage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

                #Creating the title frame 
        titleFrame = customtkinter.CTkFrame(self, width=900, height=40, corner_radius=0, fg_color="#0F392A") #This set: the size and color of the titleFrame
        titleFrame.grid(row=0, column=0, columnspan=2) ## This set the titleFrame position to the top of the homepage
        titleFrame.grid_propagate(False) ##This allows the title frame to not fit the content
        
        titleFrame.label_space = customtkinter.CTkLabel(titleFrame, width=560, text="") #THis is an empty label that set the big space between 'Home' and 'Login'
        titleFrame.label_space.grid(row=0, column=2) #This sets the empty label in the third column of the titleFrame
        titleFrame.logo = customtkinter.CTkLabel(titleFrame, width=81, text="[][][][]") # This is the the place of the logo, it will be replaced with a picture logo later on
        titleFrame.logo.grid(row=0, column=0) # This sets the logo in the first column of the titleFrame
        titleFrame.button1 = customtkinter.CTkButton(titleFrame, text="Home", width=81, height= 34, fg_color="#0F392A", bg_color="#0F392A", hover=False) # This is the Home button
        titleFrame.button1.configure(font=('Arial bold', 14))
        titleFrame.button1.grid(row =0, column =1, pady=3) # This sets the home button in the second column of the titleFrame
        titleFrame.button2 = customtkinter.CTkButton(titleFrame, text="Login", width=81, height= 34, fg_color="#0F392A", bg_color="#0F392A", hover=False) #This is the login button
        titleFrame.button2.configure(font=('Arial bold', 14))
        titleFrame.button2.grid(row =0, column =3, pady=3) # This sets the login button in the fourth column of the titleFrame
        titleFrame.button3 = customtkinter.CTkButton(titleFrame, text="Reception", width=81, height= 34, fg_color="#0F392A", bg_color="#0F392A", command=lambda:controller.show_frame(ReceptionPage), hover=False) # This will be later on the more button
        titleFrame.button3.configure(font=('Arial bold', 14))
        titleFrame.button3.grid(row =0, column =4, pady=3) # This sets the button in the fifth column of the titleFrame

        '''Here I create a searchFrame object from the searchFrame class'''
        searchPan = searchFrame(self, controller=controller) 
        searchPan.grid(row=1, column=0, columnspan=2) # I set the searchFrame in the second row of the 'HomePage' Frame and specify that it occupies two columns 
        searchPan.grid_propagate(False) #This allows to fix the size of the fram when adding a button

        '''--------------This is the frame that will contain all the social media icons on the main page--------------------'''
        socialFrame = customtkinter.CTkFrame(self, width=50, height=500, corner_radius=0, fg_color='red')
        socialFrame.grid(row=2, column=0) # I set the socialFrame in the third row of the 'HomePage' Frame 
        socialFrame.label_spaceUp = customtkinter.CTkLabel(socialFrame, width=50, height=100, text="", fg_color="white") # This label takes the first rows in the frame, and create the space before the facebook icon
        socialFrame.label_spaceUp.grid(row=0, column=0) # the fist row of the socialFrame
        socialFrame.facebook = customtkinter.CTkButton(socialFrame, text="FB", width=50, height=50, fg_color="#2765f5", corner_radius=0, command=lambda:controller.hyperlink("https://www.facebook.com")) # This is the facebook button it takes the second row of the socialFrame
        socialFrame.facebook.grid(row=1, column=0) # the second row of the socialFrame
        socialFrame.twitter = customtkinter.CTkButton(socialFrame, text="TWT", width=50, height=50, fg_color="#27f5e7", corner_radius=0, command=lambda:controller.hyperlink("https://www.twitter.com")) # This is the Twitter button it takes the third row of the socialFrame
        socialFrame.twitter.grid(row=2, column=0) # Third row of the socialFrame
        socialFrame.google = customtkinter.CTkButton(socialFrame, text="GG", width=50, height=50, fg_color="#de5309", corner_radius=0, command=lambda:controller.hyperlink("https://www.google.com")) # This is the Google button it takes the fourth row of the socialFrame
        socialFrame.google.grid(row=3, column=0) # fourth row of the socialFrame
        socialFrame.youtube = customtkinter.CTkButton(socialFrame, text="YT", width=50, height=50, fg_color="#ab0f07", corner_radius=0, command=lambda:controller.hyperlink("https://www.youtube.com")) # This is the Youtube button it takes the fifth row of the socialFrame
        socialFrame.youtube.grid(row=4, column=0) # fifth row of the socialFrame
        socialFrame.tiktok = customtkinter.CTkButton(socialFrame, text="TT", width=50, height=50, fg_color="#9a07ab", corner_radius=0, command=lambda:controller.hyperlink("https://www.tiktok.com")) # This is the Tiktok button it takes the sixth row of the socialFrame
        socialFrame.tiktok.grid(row=5, column=0) # sixth row of the socialFrame
        socialFrame.instagram = customtkinter.CTkButton(socialFrame, text="IG", width=50, height=50, fg_color="#d1d10d", corner_radius=0, command=lambda:controller.hyperlink("https://www.instagram.com")) # This is the Instagram button it takes the seventh row of the socialFrame
        socialFrame.instagram.grid(row=6, column=0) # Seventh row of the socialFrame
        socialFrame.label_spaceDown = customtkinter.CTkLabel(socialFrame, width=50, height=100, text="", fg_color="#FDFEFF") # This label takes the eight row in the frame, and creates the space after the Instagram button
        socialFrame.label_spaceDown.grid(row=7, column=0) # the eighth row of the socialFrame
        '''----------------------------------------------------End of the socialFrame---------------------------------------'''
        '''This is the main frame, where the rooms will appear'''
        mainFrame = mainBackgroundPage(self, controller=controller)
        mainFrame.grid(row=2, column=1)
        mainFrame.grid_propagate(False)

        scroll_canvas =  customtkinter.CTkCanvas(mainFrame, width=850)
        scroll_canvas.grid(row=0, column=0)

        yscroll = customtkinter.CTkScrollbar(mainFrame, orientation="vertical", command=scroll_canvas.yview)
        yscroll.grid(row=0, column=0, sticky="nse")

        containerFrame = customtkinter.CTkFrame(scroll_canvas, fg_color="#F0FEFF", width=850, corner_radius=0)
        containerFrame.grid(row=0, column=0)

        containerFrame.menuFrame = customtkinter.CTkFrame(containerFrame, width=850, fg_color="#cfcfcf", corner_radius=0)
        containerFrame.menuFrame.grid(row=0, column=0)

        containerFrame.menuFrame.title_lable = customtkinter.CTkLabel(containerFrame.menuFrame, text="Top rated room", width=850, height=45)
        containerFrame.menuFrame.title_lable.grid(row=0, column=0)
        '''containerFrame.label_space2 = customtkinter.CTkLabel(containerFrame, text="", width=115)
        containerFrame.grid(row=0, column=2)'''

        '''Scrollbar for the main background page'''

        '''Creating the footer frame'''
        footerFrame = customtkinter.CTkFrame(self, width=900, height=500, corner_radius=0, fg_color="#0F392A")
        footerFrame.grid(row=3, column=0, columnspan=2)
        footerFrame.label_space = customtkinter.CTkLabel(footerFrame, width=730, text="", fg_color="#0F392A")
        footerFrame.label_space.grid(row=0, column=0)
        footerFrame.staffLogin = customtkinter.CTkButton(footerFrame, width=170, height=34, fg_color="#0F392A", text="Connect as Staff Member", hover=False)
        footerFrame.staffLogin.grid(row=0, column=1)
#=================================================================End of the Home page=======================================================================

'''mainBackgroundPage'''
class mainBackgroundPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

        self.configure(width=850, height=500, fg_color='#FDFEFF', corner_radius=0)
        

# THis is the search frame. This frame will hold the search bar and the title of the page.
class searchFrame(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        
        self.configure(width=900, height=125)
        self.configure(fg_color="#4A866C", corner_radius=0)

        self.titleLab1 = customtkinter.CTkLabel(self, text="Enjoy your stay and leave the rest to us!", width=900, height=40)
        self.titleLab1.configure(font=('Arial bold', 31))
        self.titleLab1.grid(row=0, column=0)
        self.titleLab2 = customtkinter.CTkLabel(self, text="Find a room now", width=900, height=40)
        self.titleLab2.configure(font=('Arial bold', 31))
        self.titleLab2.grid(row=1, column=0)
        self.search = customtkinter.CTkEntry(self, placeholder_text="Type something", width=300, height=32, border_width=1, fg_color="white", text_color="#0F392A")
        self.search.configure(font=('Arial bold', 12))
        self.search.grid(row=2, column=0)

class ReceptionPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        label = customtkinter.CTkLabel(self, text="Receptionist Page")
        label.pack(padx=10, pady=10)
        switch_window_button = customtkinter.CTkButton(self, text="Go to manager page", command=lambda:controller.show_frame(ManagementPage))
        switch_window_button.pack(side="bottom", fill=customtkinter.X)

class ManagementPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        label = customtkinter.CTkLabel(self, text="We made it, Yeah!")
        label.pack(padx=10, pady=10)
        switch_window_button = customtkinter.CTkButton(self, text="Return to Home Page", command=lambda: controller.show_frame(HomePage))
        switch_window_button.pack(side="bottom", fill=customtkinter.X)

if __name__ == "__main__":
    testObj = window()
    testObj.mainloop()
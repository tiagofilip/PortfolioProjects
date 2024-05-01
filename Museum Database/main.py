import mysql.connector
from mysql.connector import errorcode

import customtkinter
from CTkMessagebox import CTkMessagebox
from CTkTable import *

import os
from PIL import Image


try:
    cnx = mysql.connector.connect(user='root', password='your_password',
                              host='127.0.0.1',
                              database='artefacts')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
        print(cnx.is_connected())
    
customtkinter.set_appearance_mode("System") 

class App (customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Archaeological Heritage Museum")
        self.geometry("1080x600")

        self.menu_frame = customtkinter.CTkFrame(self, width=250, height=600)
        self.menu_frame.grid(row=0, column=0, padx=0, pady=0)
        self.menu_frame.columnconfigure(0, weight=1)
        self.menu_frame.rowconfigure(9, weight=1)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
        self.logo_image = customtkinter.CTkImage(dark_image=Image.open(os.path.join(image_path, "logo.png")),  size=(200, 150))

        self.frame_title = customtkinter.CTkLabel(self.menu_frame, text="", image=self.logo_image)
        self.frame_title.grid(row=0, column=0, padx=1, pady=(1, 5), sticky="nsew")

        self.bind("<Configure>", self.handle_fullscreen)
        
        self.add_artefact_btn = customtkinter.CTkButton(self.menu_frame, text="Add New Artefact", corner_radius=10, fg_color="darkorange4", border_color="black", border_width=2,
                                                           command=self.add_artefact_window)
        self.add_artefact_btn.grid(row=1, column=0, padx=20, pady=(10,0))

        self.edit_artefact_btn = customtkinter.CTkButton(self.menu_frame, corner_radius=10, text="Edit Artefact", fg_color="darkorange4", border_color="black", border_width=2, 
                                                          command=self.edit_artefact_window)
        self.edit_artefact_btn.grid(row=2, column=0, padx=20, pady=(10, 0))

        self.delete_artefact_btn = customtkinter.CTkButton(self.menu_frame, corner_radius=10, text="Delete Artefact", fg_color="darkorange4", border_color="black", border_width=2, 
                                                          command=self.delete_artefact_window)
        self.delete_artefact_btn.grid(row=3, column=0, padx=20, pady=(10, 0))

        self.search_ID_btn = customtkinter.CTkButton(self.menu_frame, corner_radius=10, text="Search Artefact by ID", fg_color="darkorange4", border_color="black", border_width=2,
                                                            command=self.search_ID_window)
        self.search_ID_btn.grid(row=4, column=0, padx=20, pady=(10,0))

        self.view_artefacts = customtkinter.CTkButton(self.menu_frame, corner_radius=10, text="View All Artefacts", fg_color="darkorange4", border_color="black", border_width=2,
                                                            command=self.view_artefacts_window)
        self.view_artefacts.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.add_room_btn = customtkinter.CTkButton(self.menu_frame, corner_radius=10, text="Add New Room", fg_color="darkorange4", border_color="black", border_width=2,
                                                            command=self.add_room_window)
        self.add_room_btn.grid(row=6, column=0, padx=20, pady=(10, 0))

        self.theme_label = customtkinter.CTkLabel(self.menu_frame, text="Appearance Mode:", anchor="w")
        self.theme_label.grid(row=7, column=0, padx=20, pady=(100, 0))

        self.theme_option = customtkinter.CTkOptionMenu(self.menu_frame, button_color="black", fg_color="darkorange4", values=["System", "Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.theme_option.grid(row=8, column=0, padx=20, pady=(10, 10))
        

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def handle_fullscreen(self, event):
        if self.attributes("-fullscreen"):
            self.menu_frame.configure(width=self.winfo_width(), height=self.winfo_height())
        else:
            self.menu_frame.configure(width=250, height=1000)
    
    def add_artefact_window(self):
        add = Add(self)
        add.grid(row=0, column=1, padx=(15, 5), pady=(15,0), sticky="nw")

    def edit_artefact_window(self):
        edit = Edit(self)
        edit.grid(row=0, column=1, padx=(15, 5), pady=(15,0), sticky="nw")
    
    def search_ID_window(self):
        search = Search(self)
        search.grid(row=0, column=1, padx=(15, 5), pady=(15,0), sticky="nw")

    def view_artefacts_window(self):
        view = View(self)
        view.grid(row=0, column=1, padx=(15, 5), pady=(15,0), sticky="nw")

    def delete_artefact_window(self):
        delete = Delete(self)
        delete.grid(row=0, column=1, padx=(15, 5), pady=(15,0), sticky="nw")

    def add_room_window(self):
        add_room = Add_Room(self)
        add_room.grid(row=0, column=1, padx=(15, 5), pady=(15,0), sticky="nw")

class Add(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.widgets = []

        self.conn = mysql.connector.connect(user='root', password='your_password', host='127.0.0.1', database='artefacts')
        self.cursor = self.conn.cursor()

        self.cursor.execute("SELECT Room_Number FROM Location")
        location_values = [row[0] for row in self.cursor.fetchall()]


        self.name_lbl = customtkinter.CTkLabel(master=self, text="Name:")
        self.name_lbl.grid(row=0, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.name_lbl)

        self.Name_Entry = customtkinter.CTkEntry(master=self, placeholder_text="Name")
        self.Name_Entry.grid(row=0, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.Name_Entry)

        self.id_lbl = customtkinter.CTkLabel(master=self, text="ID:")
        self.id_lbl.grid(row=1, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.id_lbl)

        self.ID_Entry = customtkinter.CTkEntry(master=self, placeholder_text="__________")
        self.ID_Entry.grid(row=1, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.ID_Entry)

        self.characteristics_lbl = customtkinter.CTkLabel(master=self, text="Characteristics:") 
        self.characteristics_lbl.grid(row=2, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.characteristics_lbl)

        self.characteristics_entry = customtkinter.CTkEntry(master=self, placeholder_text="")
        self.characteristics_entry.grid(row=2, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.characteristics_entry)

        self.year_lbl = customtkinter.CTkLabel(master=self, text="Year Acquired:") 
        self.year_lbl.grid(row=3, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.year_lbl)

        self.Year_Entry = customtkinter.CTkEntry(master=self, placeholder_text="YYYY") 
        self.Year_Entry.grid(row=3, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.Year_Entry)

        self.period_lbl = customtkinter.CTkLabel(master=self, text="Historical Period:")
        self.period_lbl.grid(row=4, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.period_lbl)

        self.period_menu = customtkinter.CTkOptionMenu(master=self, values=['Archaic Period', 'Classical Period', 'Hellenistic Period', 'Old Kingdom', 'Middle Kingdom', 'New Kingdom', 'Ptolemaic Dynasty'], button_color="black", fg_color="darkorange4", dropdown_hover_color="darkorange4", anchor="center")
        self.period_menu.grid(row=4, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.period_menu)

        self.FqRestauringLbl = customtkinter.CTkLabel(master=self, text="Restauration Frequency:") 
        self.FqRestauringLbl.grid(row=5, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.FqRestauringLbl)

        self.FQ_Restauring_Menu = customtkinter.CTkOptionMenu(master=self, values=['Every 6 months', 'Every 1 year', 'Every 2 years', 'Every 3 years', 'Every 4 years'], button_color="black", fg_color="darkorange4", dropdown_hover_color="darkorange4", anchor="center")
        self.FQ_Restauring_Menu.grid(row=5, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.FQ_Restauring_Menu)

        self.stateLbl = customtkinter.CTkLabel(master=self, text="State:") 
        self.stateLbl.grid(row=6, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.stateLbl)

        self.state_menu = customtkinter.CTkOptionMenu(master=self, values=['Research Finished', 'Ongoing Research', 'In Restoration'], button_color="black", fg_color="darkorange4", dropdown_hover_color="darkorange4", anchor="center")
        self.state_menu.grid(row=6, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.state_menu)

        self.locationLbl = customtkinter.CTkLabel(master=self, text="Location:") 
        self.locationLbl.grid(row=7, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.locationLbl)

        self.location_menu = customtkinter.CTkOptionMenu(master=self, values=location_values, button_color="black", fg_color="darkorange4", dropdown_hover_color="darkorange4", anchor="center")
        self.location_menu.grid(row=7, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.location_menu)


        self.addBtn = customtkinter.CTkButton(master=self, text="Add Artefact", fg_color="darkorange4", corner_radius=10, border_width=2, border_color="black", command=self.add_artefact)
        self.addBtn.grid(row=8, column=2, padx=(100,5), pady=(10,0), sticky="ne")
        self.widgets.append(self.addBtn)

        self.destroy_btn = customtkinter.CTkButton(master=self, text="Close Form",  fg_color="darkorange4", corner_radius=10, border_width=2, border_color="black", command=self.destroy_form)
        self.destroy_btn.grid(row=9, column=2, padx=(10,5), pady=(10,0), sticky="ne")
        self.widgets.append(self.destroy_btn)

    def destroy_form(self):
        for widget in self.widgets:
            widget.grid_forget()
        self.destroy()


    def add_artefact(self):

        name_add = self.Name_Entry.get()
        id_add = self.ID_Entry.get()
        state_add = self.state_menu.get()
        year_add = self.Year_Entry.get()
        location_add = self.location_menu.get()
        fq_restauring_add = self.FQ_Restauring_Menu.get()
        characteristics_add = self.characteristics_entry.get()
        period_add = self.period_menu.get()
        
        if not all([name_add, id_add, characteristics_add, year_add, period_add, fq_restauring_add, state_add, location_add]):
            CTkMessagebox(title="Error", message="Please fill all the boxes.", icon = 'cancel')
        else:
            try:
                with mysql.connector.connect(user='root', password='your_password', host='127.0.0.1', database='artefacts') as cnx:
                    cursor = cnx.cursor()
                    insert_query = ("INSERT INTO artefact "
                            "(Name_Artefact, ID, Characteristics, Year_Acquired, Historical_Period_Name, FQ_Restauration, State, Room_Number) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
                    data = (name_add, id_add, characteristics_add, year_add, period_add, fq_restauring_add, state_add, location_add)
                    cursor.execute(insert_query, data)
                    cnx.commit()
                    CTkMessagebox(title="Artefact Added", message="The Artefact has been added.")

            except mysql.connector.Error as err:
                if err.errno == mysql.connector.errorcode.ER_DUP_ENTRY:
                    CTkMessagebox(title="Error", message="An artefact with the same ID already exists.", icon='cancel')
                else:
                    CTkMessagebox(title="Error", message="Something went wrong, please check if all boxes were filled correctly", icon='cancel')

            finally:
                cnx.commit()
                cursor.close()
                cnx.close()

class Add_Room(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.widgets = []

        self.room_id_lbl = customtkinter.CTkLabel(master=self, text="Room ID:")
        self.room_id_lbl.grid(row=0, column=0, padx=(10,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.room_id_lbl)

        self.room_id_entry = customtkinter.CTkEntry(master=self, placeholder_text="")
        self.room_id_entry.grid(row=0, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.room_id_entry)

        self.room_name_lbl = customtkinter.CTkLabel(master=self, text="Room Name:")
        self.room_name_lbl.grid(row=1, column=0, padx=(10,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.room_name_lbl)
        
        self.room_name_entry = customtkinter.CTkEntry(master=self, placeholder_text="")
        self.room_name_entry.grid(row=1, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.room_name_entry)

        self.add_room_btn = customtkinter.CTkButton(master=self, text="Add Room", fg_color="darkorange4", corner_radius=10, border_width=2, border_color="black", command=self.add_new_room)
        self.add_room_btn.grid(row=2, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.add_room_btn)
        
        self.destroy_btn = customtkinter.CTkButton(master=self, text="Close Form",  fg_color="darkorange4", corner_radius=10, border_width=2, border_color="black", command=self.destroy_form)
        self.destroy_btn.grid(row=3, column=1, padx=(10,5), pady=(10,0), sticky="ne")
        self.widgets.append(self.destroy_btn)

    def destroy_form(self):
        for widget in self.widgets:
            widget.grid_forget()
        self.destroy()

    def add_new_room(self):

        room_id = self.room_id_entry.get()
        room_name = self.room_name_entry.get()

        if not all([room_id, room_name]):
            CTkMessagebox(title="Error", message="Please fill all the boxes.", icon = 'cancel')
            return

        try:
            cnx = mysql.connector.connect(user='root', password='your_password', host='127.0.0.1', database='artefacts')
        except mysql.connector.Error as err:
            CTkMessagebox(title="Error", message="Connection failed", icon="cancel")
            return 

        cursor = cnx.cursor()

        insert_query = ("INSERT INTO Location (ID, Room_Number) VALUES (%s, %s)")
        data = (room_id, room_name)

        try:
            cursor.execute(insert_query, data)
            cnx.commit()
            CTkMessagebox(title="New Room Added", message="A New Room has been added")
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_DUP_ENTRY:
                CTkMessagebox(title="Error", message="A Room with the same ID already exists.", icon='cancel')
            else:
                CTkMessagebox(title="Error", message="Database error", icon="cancel")
        finally:
            cursor.close()
            cnx.close()

class Edit(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.widgets = []

        self.conn = mysql.connector.connect(user='root', password='your_password', host='127.0.0.1', database='artefacts')
        self.cursor = self.conn.cursor()

        self.cursor.execute("SELECT Room_Number FROM Location")
        location_values = [row[0] for row in self.cursor.fetchall()]

        self.Id_lbl = customtkinter.CTkLabel(master=self, text="ID:")
        self.Id_lbl.grid(row=9, column=0, padx=(10,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.Id_lbl)

        self.Id_Entry = customtkinter.CTkEntry(master=self, placeholder_text = "__________", width = 200, height=10)
        self.Id_Entry.grid(row=9, column=0, padx=(100,5), pady=(10,0), sticky="nsew")
        self.widgets.append(self.Id_Entry)

        self.search_btn = customtkinter.CTkButton(master=self, text="Search", fg_color="darkorange4", corner_radius=10, border_width=2, border_color="black", command=self.search_ID)
        self.search_btn.grid(row=9, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.search_btn)

        self.name_lbl = customtkinter.CTkLabel(master=self, text="Name:")
        self.name_lbl.grid(row=0, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.name_lbl)

        self.Name_Entry = customtkinter.CTkEntry(master=self, placeholder_text="Name")
        self.Name_Entry.grid(row=0, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.Name_Entry)

        self.id_lbl = customtkinter.CTkLabel(master=self, text="ID:")
        self.id_lbl.grid(row=1, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.id_lbl)

        self.ID_Entry = customtkinter.CTkEntry(master=self, placeholder_text="__________")
        self.ID_Entry.grid(row=1, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.ID_Entry)

        self.characteristicsLbl = customtkinter.CTkLabel(master=self, text="Characteristics:") 
        self.characteristicsLbl.grid(row=2, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.characteristicsLbl)

        self.characteristics_entry = customtkinter.CTkEntry(master=self, placeholder_text="")
        self.characteristics_entry.grid(row=2, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.characteristics_entry)

        self.yearLbl = customtkinter.CTkLabel(master=self, text="Year Acquired:") 
        self.yearLbl.grid(row=3, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.yearLbl)

        self.Year_Entry = customtkinter.CTkEntry(master=self, placeholder_text="YYYY") 
        self.Year_Entry.grid(row=3, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.Year_Entry)

        self.periodLbl = customtkinter.CTkLabel(master=self, text="Historical Period:")
        self.periodLbl.grid(row=4, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.periodLbl)

        self.period_menu = customtkinter.CTkOptionMenu(master=self, values=['Archaic Period', 'Classical Period', 'Hellenistic Period', 'Old Kingdom', 'Middle Kingdom', 'New Kingdom', 'Ptolemaic Dynasty'], button_color="black", fg_color="darkorange4", dropdown_hover_color="darkorange4", anchor="center")
        self.period_menu.grid(row=4, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.period_menu)

        self.FqRestauringLbl = customtkinter.CTkLabel(master=self, text="Restauration Frequency:") 
        self.FqRestauringLbl.grid(row=5, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.FqRestauringLbl)

        self.FQ_Restauring_Menu = customtkinter.CTkOptionMenu(master=self, values=['Every 6 months', 'Every 1 year', 'Every 2 years', 'Every 3 years', 'Every 4 years'], button_color="black", fg_color="darkorange4", dropdown_hover_color="darkorange4", anchor="center")
        self.FQ_Restauring_Menu.grid(row=5, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.FQ_Restauring_Menu)

        self.stateLbl = customtkinter.CTkLabel(master=self, text="State:") 
        self.stateLbl.grid(row=6, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.stateLbl)

        self.state_menu = customtkinter.CTkOptionMenu(master=self, values=['Research Finished', 'Ongoing Research', 'In Restoration'], button_color="black", fg_color="darkorange4", dropdown_hover_color="darkorange4", anchor="center")
        self.state_menu.grid(row=6, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.state_menu)

        self.locationLbl = customtkinter.CTkLabel(master=self, text="Location:") 
        self.locationLbl.grid(row=7, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.locationLbl)

        self.location_menu = customtkinter.CTkOptionMenu(master=self, values=location_values, button_color="black", fg_color="darkorange4", dropdown_hover_color="darkorange4", anchor="center")
        self.location_menu.grid(row=7, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.location_menu)

        self.conn.close()

        self.save_Btn = customtkinter.CTkButton(master=self, text="Save Changes", fg_color="darkorange4", corner_radius=10, border_width=2, border_color="black", command=self.save_artefact)
        self.save_Btn.grid(row=8, column=2, padx=(100,5), pady=(10,0), sticky="ne")
        self.widgets.append(self.save_Btn)

        self.destroy_btn = customtkinter.CTkButton(master=self, text="Close Form",  fg_color="darkorange4", corner_radius=10, border_width=2, border_color="black", command=self.destroy_form)
        self.destroy_btn.grid(row=9, column=2, padx=(10,5), pady=(10,0), sticky="ne")
        self.widgets.append(self.destroy_btn)

    def destroy_form(self):
        for widget in self.widgets:
            widget.grid_forget()
        self.destroy()

    def save_artefact(self):

        updated_name = self.Name_Entry.get()
        updated_id = self.ID_Entry.get()
        updated_state = self.state_menu.get()
        updated_year = self.Year_Entry.get()
        updated_location = self.location_menu.get()
        updated_fq_restoring = self.FQ_Restauring_Menu.get()
        updated_period = self.period_menu.get()
        updated_characteristics = self.characteristics_entry.get()

        try:
            with mysql.connector.connect(user='root', password='your_password',
                                        host='127.0.0.1',
                                        database='artefacts') as cnx:
                cursor = cnx.cursor()

                query = """
                UPDATE artefact
                SET Name_Artefact = %s, ID = %s, State = %s, Year_Acquired = %s,
                Room_Number = %s, FQ_Restauration = %s, Historical_Period_Name = %s, Characteristics = %s
                WHERE ID = %s
                """
                cursor.execute(query, (updated_name, updated_id, updated_state, updated_year,
                                   updated_location, updated_fq_restoring, updated_period,
                                   updated_characteristics, updated_id))
                cnx.commit() 

            CTkMessagebox(title ="Success", message = "Artefact data has been updated successfully.")

        except mysql.connector.Error as e:
            print("An error occurred:", e)
            CTkMessagebox(title = "Error", message = "An error occurred while updating artefact data. Please check all boxes again.", icon = "cancel")
        
    def search_ID(self):
        entered_id = self.Id_Entry.get()

        try:
            with mysql.connector.connect(user='root', password='your_password',
                              host='127.0.0.1',
                              database='artefacts') as cnx:
                cursor = cnx.cursor()

                query = "SELECT * FROM artefact WHERE ID = %s"
                cursor.execute(query, (entered_id,))
                row = cursor.fetchone()

                if row:

                    self.Name_Entry.configure(state="normal")
                    self.Name_Entry.delete(0, "end")
                    self.Name_Entry.insert("end", row[0])

                    self.ID_Entry.configure(state="normal")
                    self.ID_Entry.delete(0, "end")
                    self.ID_Entry.insert("end", row[1])

                    self.state_menu.configure(state="normal")
                    self.state_menu.set(row[6])

                    self.Year_Entry.configure(state="normal")
                    self.Year_Entry.delete(0, "end")
                    self.Year_Entry.insert("end", row[3])

                    self.location_menu.configure(state="normal")
                    self.location_menu.set(row[7])

                    self.FQ_Restauring_Menu.configure(state="normal")
                    self.FQ_Restauring_Menu.set(row[5])

                    self.period_menu.configure(state="normal")
                    self.period_menu.set(row[4])

                    self.characteristics_entry.configure(state="normal")
                    self.characteristics_entry.delete(0, "end")
                    self.characteristics_entry.insert("end", row[2])

                else:
                    CTkMessagebox(title = "Error", message = "ID not found, please enter valid ID, or add a new artefact.", icon = "cancel")
        except mysql.connector.Error as e:
            print("An error occurred:", e)
            

class Delete(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.widgets = []

        self.Id_lbl = customtkinter.CTkLabel(master=self, text="ID:")
        self.Id_lbl.grid(row=9, column=0, padx=(10,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.Id_lbl)

        self.Id_Entry = customtkinter.CTkEntry(master=self, placeholder_text = "__________", width = 200, height=10)
        self.Id_Entry.grid(row=9, column=0, padx=(100,5), pady=(10,0), sticky="nsew")
        self.widgets.append(self.Id_Entry)

        self.delete_btn = customtkinter.CTkButton(master=self, text="Delete", fg_color="darkorange4", corner_radius=10, border_width=2, border_color="black", command=self.delete_artefact)
        self.delete_btn.grid(row=9, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.delete_btn)

        self.destroy_btn = customtkinter.CTkButton(master=self, text="Close Form",  fg_color="darkorange4", corner_radius=10, border_width=2, border_color="black", command=self.destroy_form)
        self.destroy_btn.grid(row=9, column=2, padx=(10,5), pady=(10,0), sticky="ne")
        self.widgets.append(self.destroy_btn)

    def destroy_form(self):
        for widget in self.widgets:
            widget.grid_forget()
        self.destroy()

    def delete_artefact(self):
        entered_id = self.Id_Entry.get().strip()

        confirmation = CTkMessagebox(title="Warning", message="Do you want to delete this Artefact?", icon = "warning", option_1="Delete Artefact", option_2="Cancel")

        response = confirmation.get()

        if response == "Delete Artefact":
            try:
                with mysql.connector.connect(user='root', password='your_password', host='127.0.0.1', database='artefacts') as cnx:
                    cursor = cnx.cursor()

                    query = "DELETE FROM artefact WHERE ID = %s"
                    cursor.execute(query, (entered_id,))

                    row_count = cursor.rowcount
                    if row_count == 0:
                        raise ValueError(CTkMessagebox(title="Error", message="No Artefact with given ID exists in the database.", icon = "cancel"))

                    cnx.commit()
                    CTkMessagebox(title="Success", message="Artefact deleted.")

            except mysql.connector.Error as err:
                CTkMessagebox.showerror(title="Error", message="Something went wrong:" + str(err), icon='cancel')
        

                    
class Search(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.widgets = []

        self.Id_lbl = customtkinter.CTkLabel(master=self, text="ID:")
        self.Id_lbl.grid(row=9, column=0, padx=(10,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.Id_lbl)

        self.Id_Entry = customtkinter.CTkEntry(master=self, placeholder_text = "__________", width = 200, height=10)
        self.Id_Entry.grid(row=9, column=0, padx=(100,5), pady=(10,0), sticky="nsew")
        self.widgets.append(self.Id_Entry)

        self.search_btn = customtkinter.CTkButton(master=self, text="Search", fg_color="darkorange4", corner_radius=10, border_width=2, border_color="black", command=self.search_ID)
        self.search_btn.grid(row=9, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.search_btn)
        
        self.clear_btn = customtkinter.CTkButton(master=self, text="Clear Boxes", fg_color="darkorange4", corner_radius=10, border_width=2, border_color="black", command=self.clear_boxes)
        self.clear_btn.grid(row=10, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.clear_btn)

        self.name_lbl = customtkinter.CTkLabel(master=self, text="Name:")
        self.name_lbl.grid(row=0, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.name_lbl)

        self.Id_lbl = customtkinter.CTkLabel(master=self, text="ID:")
        self.Id_lbl.grid(row=1, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.Id_lbl)

        self.stateLbl = customtkinter.CTkLabel(master=self, text="State:") 
        self.stateLbl.grid(row=2, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.stateLbl)

        self.yearLbl = customtkinter.CTkLabel(master=self, text="Year Acquired:") 
        self.yearLbl.grid(row=3, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.yearLbl)

        self.locationLbl = customtkinter.CTkLabel(master=self, text="Location:") 
        self.locationLbl.grid(row=4, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.locationLbl)

        self.FqRestauringLbl = customtkinter.CTkLabel(master=self, text="Restauration Frequency:") 
        self.FqRestauringLbl.grid(row=5, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.FqRestauringLbl)

        self.periodLbl = customtkinter.CTkLabel(master=self, text="Historical Period:")
        self.periodLbl.grid(row=6, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.periodLbl)

        self.characteristicsLbl = customtkinter.CTkLabel(master=self, text="Characteristics:") 
        self.characteristicsLbl.grid(row=7, column=0, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.characteristicsLbl)

        self.name_box = customtkinter.CTkTextbox(master=self, state="disabled", width=100, height=50)
        self.name_box.grid(row=0, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.name_box)

        self.ID_Box = customtkinter.CTkTextbox(master=self, state="disabled", width=100, height=50)
        self.ID_Box.grid(row=1, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.ID_Box)

        self.state_menu = customtkinter.CTkOptionMenu(master=self, values=['Research Finished', 'Ongoing Research', 'In Restoration'], button_color="black", fg_color="darkorange4", dropdown_hover_color="darkorange4", anchor="center", state="disabled")
        self.state_menu.grid(row=2, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.state_menu)

        self.year_box = customtkinter.CTkTextbox(master=self, state="disabled", width=100, height=50) 
        self.year_box.grid(row=3, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.year_box)

        self.location_menu = customtkinter.CTkOptionMenu(master=self, values=['Room 1', 'Room 2', 'Room 3', 'Restoration Room'], button_color="black", fg_color="darkorange4", dropdown_hover_color="darkorange4", anchor="center", state="disabled")
        self.location_menu.grid(row=4, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.location_menu)

        self.FQ_Restauring_Menu = customtkinter.CTkOptionMenu(master=self, values=['Every 6 months', 'Every 1 year', 'Every 2 years', 'Every 3 years', 'Every 4 years'], button_color="black", fg_color="darkorange4", dropdown_hover_color="darkorange4", anchor="center", state="disabled")
        self.FQ_Restauring_Menu.grid(row=5, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.FQ_Restauring_Menu)

        self.period_menu = customtkinter.CTkOptionMenu(master=self, values=['Archaic', 'Classical', 'Hellenistic', 'Old Kingdom', 'Middle Kingdom', 'New Kingdom', 'Ptolemaic Dynasty'], button_color="black", fg_color="darkorange4", dropdown_hover_color="darkorange4", anchor="center", state="disabled")
        self.period_menu.grid(row=6, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.period_menu)

        self.characteristics_Txt = customtkinter.CTkTextbox(master=self, width=200, height=100, state="disabled")
        self.characteristics_Txt.grid(row=7, column=1, padx=(100,5), pady=(10,0), sticky="nw")
        self.widgets.append(self.characteristics_Txt)

        self.destroy_btn = customtkinter.CTkButton(master=self, text="Close Form",  fg_color="darkorange4", corner_radius=10, border_width=2, border_color="black", command=self.destroy_form)
        self.destroy_btn.grid(row=10, column=2, padx=(10,5), pady=(10,0), sticky="ne")
        self.widgets.append(self.destroy_btn)

    def destroy_form(self):
        for widget in self.widgets:
            widget.grid_forget()
        self.destroy()

    def clear_boxes(self):
        self.name_box.configure(state="normal")
        self.name_box.delete(1.0, "end")
        self.name_box.configure(state="disabled")

        self.ID_Box.configure(state="normal")
        self.ID_Box.delete(1.0, "end")
        self.ID_Box.configure(state="disabled")
                
        self.state_menu.configure(state="normal")
        self.state_menu.set(None)
        self.state_menu.configure(state="disabled")
                
        self.year_box.configure(state="normal")
        self.year_box.delete(1.0, "end")
        self.year_box.configure(state="disabled")
                
        self.location_menu.configure(state="normal")
        self.location_menu.set(None)
        self.location_menu.configure(state="disabled")
                
        self.FQ_Restauring_Menu.configure(state="normal")
        self.FQ_Restauring_Menu.set(None)
        self.FQ_Restauring_Menu.configure(state="disabled")
                
        self.period_menu.configure(state="normal")
        self.period_menu.set(None)
        self.period_menu.configure(state="disabled")
                
        self.characteristics_Txt.configure(state="normal")
        self.characteristics_Txt.delete(1.0, "end")
        self.characteristics_Txt.configure(state="disabled")
        
        
    def search_ID(self):
        entered_id = self.Id_Entry.get()

        cursor = cnx.cursor()
            
        query = "SELECT * FROM artefact WHERE ID = %s"
        cursor.execute(query, (entered_id,))

        results = cursor.fetchall()

        if results:

            for row in results:

                self.name_box.configure(state="normal")
                self.name_box.delete(1.0, "end")
                self.name_box.insert("end", row[0])
                self.name_box.configure(state="disabled")

                self.ID_Box.configure(state="normal")
                self.ID_Box.delete(1.0, "end")
                self.ID_Box.insert("end", row[1])
                self.ID_Box.configure(state="disabled")
                
                self.state_menu.configure(state="normal")
                self.state_menu.set(row[6])
                self.state_menu.configure(state="disabled")
                
                self.year_box.configure(state="normal")
                self.year_box.delete(1.0, "end")
                self.year_box.insert("end", row[3])
                self.year_box.configure(state="disabled")
                
                self.location_menu.configure(state="normal")
                self.location_menu.set(row[7])
                self.location_menu.configure(state="disabled")
                
                self.FQ_Restauring_Menu.configure(state="normal")
                self.FQ_Restauring_Menu.set(row[5])
                self.FQ_Restauring_Menu.configure(state="disabled")
                
                self.period_menu.configure(state="normal")
                self.period_menu.set(row[4])
                self.period_menu.configure(state="disabled")
                
                self.characteristics_Txt.configure(state="normal")
                self.characteristics_Txt.delete(1.0, "end")
                self.characteristics_Txt.insert("end", row[2])
                self.characteristics_Txt.configure(state="disabled")

        else:
            CTkMessagebox(title = "Error", message = "ID not found, please enter valid ID, or add a new artefact.", icon = "cancel")
        
class View(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.widgets = []

        self.scroll = customtkinter.CTkScrollableFrame(master=self, width=750, height=500, corner_radius=10)
        self.scroll.grid(row=1, column=0, padx=15, pady=15)
        self.widgets.append(self.scroll)
        

        with mysql.connector.connect(user='root', password='your_password', host='127.0.0.1', database='artefacts') as cnx:
            cursor = cnx.cursor()
            query = "SELECT * FROM artefact"
            cursor.execute(query)
            artefacts = cursor.fetchall()
        

        results = len(artefacts) + 1
        columns = len(artefacts[0]) 
        values = [["Name", "ID", "Characteristics", "Acquired In", "Historical Period", "Restauration Frequency", "State", "Location"]] + artefacts

        table = CTkTable(master=self.scroll, row=results, column=columns, values=values, width = 40, height=30, wraplength=100)
        table.pack(expand=True, fill="both", padx=20, pady=20)
        self.widgets.append(table)
        
        self.refresh_button = customtkinter.CTkButton(master=self, text="Refresh", fg_color="darkorange3", corner_radius=10, border_width=2, border_color="black", command=self.refresh_database)
        self.refresh_button.grid(row=2, column=0, padx=(10, 155), pady=(0, 10), sticky="ne")
        self.widgets.append(self.refresh_button)

        self.destroy_btn = customtkinter.CTkButton(master=self, text="Close Table",  fg_color="darkorange4", corner_radius=10, border_width=2, border_color="black", command=self.destroy_form)
        self.destroy_btn.grid(row=2, column=0, padx=(10,10), pady=(0,10), sticky="ne")
        self.widgets.append(self.destroy_btn)

    def refresh_database(self):

        try:
            cnx = mysql.connector.connect(user='root', password='your_password', host='127.0.0.1', database='artefacts')
            cursor = cnx.cursor()
            query = "SELECT * FROM artefact"
            cursor.execute(query)
            artefacts = cursor.fetchall()
        except mysql.connector.Error as err:
            print("Error connecting to database:", err)
            return  
        
        results = len(artefacts)
        columns = len(artefacts[0])

        values = [["Name", "ID", "Characteristics", "Acquired In", "Historical Period", "Restauration Frequency", "State", "Location"]] + artefacts

        for widget in self.widgets:
            if isinstance(widget, CTkTable):
                widget.destroy()
                break

        table = CTkTable(master=self.scroll, row=results, column=columns, values=values, width=40, height=30, wraplength=100)
        table.pack(expand=True, fill="both", padx=20, pady=20)
        self.widgets.append(table)

        cnx.close()

    def destroy_form(self):
        for widget in self.widgets:
            widget.grid_forget()
        self.destroy()
        
app = App()
app.mainloop()

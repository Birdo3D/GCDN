import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: "System", "Light", "Dark"
ctk.set_default_color_theme("blue")


class SettingsApp(ctk.CTk):
    def __init__(self, user):
        super().__init__()

        self.usr = user

        # Configuration de la fenêtre principale
        self.title("Paramètres utilisateur")
        self.geometry("500x600")

        # Bouton de fermeture
        self.close_button = ctk.CTkButton(self, text="⨉", width=30, height=30, command=self.destroy, corner_radius=15, fg_color="gray")
        self.close_button.place(relx=0.96, rely=0.03, anchor="ne")

        # Titre principal
        self.title_label = ctk.CTkLabel(self, text="Mon compte utilisateur", font=("Arial", 24))
        self.title_label.pack(pady=20, padx=25, anchor="w")

        # Paramètres
        self.create_setting_row("Pseudo", user.get_name())
        self.create_setting_row("Âge", str(user.get_age()))
        self.create_setting_row("Artiste 1", "PLK")
        self.create_setting_row("Artiste 2", "Goldman")
        self.create_setting_row("Artiste 3", "Zazie")

        # Genre de musique préférés
        self.genre_label = ctk.CTkLabel(self, text="Genre de musique préféré :", font=("Arial", 14))
        self.genre_label.pack(pady=(30, 10))
        self.create_genre_radio_buttons()

        # Mot de passe
        self.create_setting_row("Mot de passe", "********")

        # Bouton de déconnexion
        self.logout_button = ctk.CTkButton(self, text="Déconnexion", command=self.logout, fg_color="red", corner_radius=15)
        self.logout_button.place(relx=0.04, rely=0.96, anchor="sw")

    def create_genre_radio_buttons(self):
        """Crée des boutons radios pour les genres"""
        genres = ["Pop", "Rock", "Classique", "Jazz", "Rap", "Électro"]

        frame = ctk.CTkFrame(self)
        frame.pack(fill="x", padx=20, pady=(10, 40))

        self.genre_var = ctk.StringVar(value="Pop")

        for i, genre in enumerate(genres):
            ctk.CTkRadioButton(frame, text=genre, variable=self.genre_var, value=genre).grid(row=i // 2, column=i % 2, padx=20, pady=5, sticky="w")

    def create_setting_row(self, field_name, current_value):
        """Crée une ligne de paramètre"""
        frame = ctk.CTkFrame(self)
        frame.pack(fill="x", pady=5, padx=20)

        # Label du champ
        label = ctk.CTkLabel(frame, text=f"{field_name} :", font=("Arial", 14))
        label.pack(side="left", padx=10)

        # Valeur actuelle
        value_text = current_value
        value_label = ctk.CTkLabel(frame, text=value_text, font=("Arial", 14))
        value_label.pack(side="left", padx=10)

        # Bouton Modifier
        modify_button = ctk.CTkButton(frame, text="Modifier", width=80, command=lambda: self.open_change_window(field_name, value_label))
        modify_button.pack(side="right", padx=10)

    def open_change_window(self, field_name, value_label):
        """Ouvre une fenêtre pour changer la valeur"""
        change_window = ctk.CTkToplevel(self)
        change_window.title(f"Modifier {field_name}")
        change_window.geometry("400x200")

        label = ctk.CTkLabel(change_window, text=f"Mettre à jour : {field_name}", font=("Arial", 14))
        label.pack(pady=(20, 10))

        entry = ctk.CTkEntry(change_window, placeholder_text=f"Entrez votre {field_name.lower()}", show="")
        entry.pack(pady=10)

        def save_change():
            new_value = entry.get()
            if new_value:
                value_label.configure(new_value)
                change_window.destroy()

        save_button = ctk.CTkButton(change_window, text="Enregistrer", command=save_change)
        save_button.pack(pady=20)

    def logout(self):
        # Action de déconnexion
        print("Déconnexion réussie !")

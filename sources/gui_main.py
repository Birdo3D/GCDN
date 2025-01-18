import customtkinter as ctk
from gui_params import *
from sources.user_data import *
from play_data import *
from algo_playlist import *
from sources.math.pile import *
from sources.math.file import *
from PIL import Image, ImageTk, ImageDraw
import requests
from io import BytesIO

# Configuration globale de CustomTkinter
ctk.set_appearance_mode("Dark")  # Mode clair ou sombre
ctk.set_default_color_theme("blue")  # Thème de couleur


def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im


class WebImage:
    def __init__(self, url, radius: int = 0):
        u = requests.get(url)
        self.image = ImageTk.PhotoImage(add_corners(Image.open(BytesIO(u.content)), radius))

    def get(self):
        return self.image


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("GCDN")
        self.geometry("800x600")
        self.resizable(False, False)

        ar = Pile()
        ar.empiler("PLK")
        ar.empiler("Zazie")
        ar.empiler("kaaris")

        self.propositions = creer_playlist("pop", ["PLK", "maes", "kaaris"], 20)

        self.playlist = File()

        # Cadre pour les boutons à gauche
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        # Bouton "Créer une nouvelle playlist" en haut
        self.new_playlist_button = ctk.CTkButton(
            self.sidebar,
            text="Nouvelle playlist",
            command=self.display_tinder_view_for_playlist_creation
        )
        self.new_playlist_button.pack(pady=10, padx=10)

        # Conteneur pour la liste des playlists avec une scrollbar
        self.playlist_container = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        self.playlist_container.pack(fill="both", expand=True, pady=10, padx=10)

        # Scrollbar pour les playlists
        self.scrollable_frame = ctk.CTkScrollableFrame(self.playlist_container, width=180, corner_radius=0)
        self.scrollable_frame.pack(fill="both", expand=True)

        # Ajout des boutons de playlist dans la scrollbar
        self.add_playlist_buttons()

        # Bouton Paramètres séparé en bas
        self.settings_button = ctk.CTkButton(self.sidebar, text="Compte", command=self.display_settings_view)
        self.settings_button.pack(side="bottom", pady=10, padx=10)

        # Cadre principal pour le contenu dynamique
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

        # Liste temporaire pour stocker les chansons de la nouvelle playlist
        self.new_playlist_songs = []

        # Initialisation de la vue par défaut
        self.display_tinder_view_for_playlist_creation()

    def add_playlist_buttons(self):
        """Ajoute une liste de boutons de playlist dans le cadre déroulant."""
        for song in get_playlists():
            playlist_button = ctk.CTkButton(self.scrollable_frame,
                                            text=f"{song} : {get_playlist(song).longueur()} titres",
                                            command=lambda song=song: self.display_playlist_view(song))
            playlist_button.pack(pady=5, padx=10, fill="x")

    def clear_main_frame(self):
        """Efface tout le contenu du cadre principal."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def display_playlist_view(self, name):
        """Affiche la vue avec des rectangles arrondis représentant des playlists."""
        self.clear_main_frame()
        copie = get_playlist(name).copy()
        for i in range(copie.longueur()):
            title = copie.defiler()
            playlist_frame = ctk.CTkFrame(self.main_frame, corner_radius=15, height=50)
            playlist_frame.pack(pady=10, padx=20, fill="x")

            label = ctk.CTkLabel(playlist_frame, text=f"Title {i} : {title} - Duration : 2:34")
            label.pack(pady=10, padx=10)

    def display_tinder_view_for_playlist_creation(self):
        """Affiche la vue type Tinder pour créer une nouvelle playlist."""
        self.clear_main_frame()

        title = self.propositions.defiler()

        # Image de l'album
        link = "https://cdn-images.dzcdn.net/images/artist/90fda6aa551a34c05671f53c4ea71390/250x250-000000-80-0-0.jpg"
        img = WebImage(link, 10).get()
        imagelab = ctk.CTkLabel(self.main_frame, image=img, text="")
        imagelab.pack(pady=20)

        # Titre de la musique
        self.song_title = ctk.CTkLabel(self.main_frame, text=title["titre"], font=ctk.CTkFont(size=16, weight="bold"))
        self.song_title.pack(pady=10)

        # Boutons "J'aime" et "J'aime pas"
        button_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        button_frame.pack(pady=20)

        like_button = ctk.CTkButton(button_frame, text="J'aime 👍", fg_color="green",
                                    command=lambda title=title: self.add_song_to_playlist(title["titre"]))
        like_button.pack(side="left", padx=10)

        dislike_button = ctk.CTkButton(button_frame, text="Je n'aime pas 👎", fg_color="red", command=self.skip_song)
        dislike_button.pack(side="right", padx=10)

        self.entry = ctk.CTkEntry(self.main_frame, placeholder_text="Donnez un titre", show="")
        self.entry.pack(pady=15)

        # Bouton pour finaliser la playlist
        finish_button = ctk.CTkButton(self.main_frame, text="Finaliser la playlist", command=self.finalize_playlist)
        finish_button.pack(pady=15)

    def add_song_to_playlist(self, title):
        """Ajoute la chanson actuelle à la nouvelle playlist."""
        self.playlist.enfiler(title)
        self.skip_song()  # Passer à la chanson suivante

    def skip_song(self):
        """Passe à la chanson suivante."""
        # Pour l'exemple, on change simplement le titre
        next_song = f"Titre de la musique {len(self.new_playlist_songs) + 2}"
        self.song_title.configure(text=next_song)

    def finalize_playlist(self):
        """Finalise la création de la nouvelle playlist."""
        self.playlist.enfiler("song1")
        export_playlist(self.playlist, self.entry.get())
        self.display_playlist_view(self.entry.get())  # Retourne à la vue de la playlist crée

    def change_frame(self, button_text):
        """Change le contenu du cadre principal en fonction du bouton cliqué."""
        if "Play" in button_text:
            self.display_tinder_view_for_playlist_creation()
        elif button_text == "Paramètres":
            self.display_settings_view()

    def display_settings_view(self):
        """Affiche les paramètres utilisateur"""
        app_setting = SettingsApp(get_default_user())
        app_setting.mainloop()

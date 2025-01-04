from launch import *
from remape_project.sources.gui.gui_params import *
from remape_project.sources.user_data import *
from remape_project.sources.math.pile import *
from remape_project.sources.math.file import *
from remape_project.sources.play_data import *

start()
set_default_user(get_users()[0])
p = Pile()
p.empiler("Titre11")
p.empiler("Titre61")
p.empiler("Titre891")
print(create_user("birdo", "monmdp", 19, "pop", p))
app = SettingsApp(User(0, "Birdo", "mdp", 19, "genre", p))
app.mainloop()

f = File()
f.enfiler("ghsdfhdf")
f.enfiler("ghfjdgjdfgjdfyjyfd")
f.enfiler("tetghghbfjkhrf")
export_playlist(f, "myplaylist1")

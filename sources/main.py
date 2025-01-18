from launch import *
from sources.gui_main import *
from sources.math.file import *
from sources.math.pile import *
from sources.play_data import *
from sources.user_data import *

start()
#set_default_user(get_users()[0])
p = Pile()
p.empiler("Titre11")
p.empiler("Titre61")
p.empiler("Titre891")
print(create_user("birdo", "monmdp", 19, "pop", p))
set_default_user(get_users()[0])
app = App()
app.mainloop()

f = File()
f.enfiler("ghsdfhdf")
f.enfiler("ghfjdgjdfgjdfyjyfd")
f.enfiler("tetghghbfjkhrf")
export_playlist(f, "myplaylist1")

print(get_playlist(get_playlists()[0]))

p2 = Pile()
p2.empiler("GOLDMAN")
p2.empiler("PLK")
p2.empiler("ZAZ")

#update_user(get_default_user(), "Nammmmee", 54, "culture", p2, "passTest")

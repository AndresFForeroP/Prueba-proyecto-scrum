import modules.menu_principal as mp
import os
import modules.f_json as fj
DATA = os.path.join('data/','registros.json')
fj.inizializar_archivo(DATA)
mp.menu_principal()
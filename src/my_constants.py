from aqt import mw
import os
addon_id = 'myaddon'
root_dir = os.path.join(mw.pm.addonFolder(), addon_id)
user_data_dir = os.path.join(root_dir, "user_files")
logs_dir = os.path.join(root_dir, "logs")

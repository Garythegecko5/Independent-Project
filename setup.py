import cx_Freeze

executables = [cx_Freeze.Executable("game_alpha.py")],

cx_Freeze.setup(
    name="Stratosfight",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files":["game_components.py", "fonts", "img", "music", "desktop.ini"]}},
    executables = executables
)
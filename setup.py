from cx_Freeze import setup, Executable

setup(
    name="Grant's Speed Reader",
    version="0.5.0",
    description="Definitely not a $pr33der ripoff",
    executables=[Executable("Speed_Reader.py", icon=".\FukSpreeder\cropped_logo.ico")]
)

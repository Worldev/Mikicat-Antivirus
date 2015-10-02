# Only for testing in Travis CI
import platform

if platform.system() == "Windows":
    linux = False
    windows = True
elif platform.system() == "Linux":
    linux = True
    windows = False
else:
    print("Mikicat Antivirus is not compatible with your operative system.")
    os._exit(1)
print("Coming soon")

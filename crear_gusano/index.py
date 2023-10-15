import shutil
import sys

if len(sys.argv) == 2:
    for n in range(0, int(sys.argv[1])):
        shutil.copy(sys.argv[0], sys.argv[0] + str(n) + ".py")
        
else:
    print("Debes enviar dos argumentos")
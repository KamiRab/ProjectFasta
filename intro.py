import string, sys, os, glob

working_dir = os.getcwd()  # renvoie chemin du fichier d'où est exécuté le code
print("working dir", working_dir)
# os.chdir(".") ???
print(os.listdir("../../"))
# os.mkdir("test_dir") #si répertoire existe déja : erreur
try:
    os.mkdir("test_dir")
    print(os.listdir())
except:
    print("repertoire existe deja, on continue")

# print("aprés suppression")
# try:
#     os.rmdir("test_dir")
#     print(os.listdir())
# except:
#     print("repertoire n'existe pas, on continue")

print("is file", os.path.isfile("chat.txt"))  # teste si x est un fichier
print("is dir", os.path.isdir("test_dir"))  # teste si x est un repertoire
# os.path.exists() #teste si x existe ??

if os.path.isfile("toto.txt"):
    os.remove("toto.txt")
elif os.path.isdir("toto.txt"):
    os.rmdir("toto.txt")
else:
    print("ni fichier, ni dossier")

# os.path.basename()
# os.path.dirname()
# os.path.getsize()

# os.system("ligne de commande")

glob.glob("*.fsa") #sort tous les fichiers.fsa
glob.glob("*f*") #sort tous les fichiers avec extensions commençant par f
sys.exit()

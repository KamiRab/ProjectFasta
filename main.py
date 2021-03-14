import os, glob, pathlib

try:
    os.mkdir("start")
except:
    print("repertoire existe deja, on continue")

os.chdir("start")

print(os.getcwd())
print(os.listdir("."))
os.chdir("../files")
print(os.listdir("."))
nb_fichier = 0
nb_dossier = 0
for name in os.listdir("."):
    if os.path.isfile(name):
        nb_fichier += 1
    if os.path.isdir(name):
        nb_dossier += 1
print("nombre de fichiers : %d  & nombre de dossiers : %d" % (nb_fichier, nb_dossier))
print("fichier existe ?", os.path.exists("seq_Ecoli_536A_seq1.fa"))

print("nb de fichier fasta", len(glob.glob("*.f*")))

fout = open("../report_fasta.txt", "w")
fout.write("#Summary \n")
fout.write("nb_items = %d \nnb_files = %d \nnb_fasta = %d \nnb_dir = %d\n\n" % (len(os.listdir(".")),
                                                                            nb_fichier, len(glob.glob("*.f*")),
                                                                            nb_dossier))
fout.close()
# try:
#     os.system("mkdir ../copie")
# except:
#     print("Dossier copie existe déja")
# os.system("cp *.f* ../copie/")

# for file in glob.glob("*.f*") :
#     basename = os.path.splitext(file)[0]
#     os.system("mv " + file + " " + basename + ".fasta")

try:
    pathlib.Path("copie/").mkdir()
except Exception:
    print("Dossier copie existe déja")

for file in glob.glob("*.f*"):
    basename = os.path.splitext(file)[0]
    pathlib.Path(file).rename(basename + ".fasta")


def nb_ligne_seq(file):
    nb_ligne = 0
    nb_seq = 0
    f = open(file, "r")
    for line in f:
        nb_ligne += 1
        for c in line:
            if c == ">":
                nb_seq += 1
    return nb_seq, nb_ligne


fout = open("../report_fasta.txt", "a")
fout.write("#Details for each fasta file \n")
fout.write("{:<25s}\t #size\t #nb_lines\t #nb_seq \n".format("#filename"))
for file in glob.glob("*.fasta"):
    fout.write("%s\t %3d\t %5d\t %10d \n" % (file, os.path.getsize(file), nb_ligne_seq(file)[1], nb_ligne_seq(file)[0]))
fout.close()

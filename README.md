# S6i APP1 - Code de démarrage

Contient tout le code nécessaire pour résoudre l'APP et les exercices du
laboratoire.

## Requis

 - CMake 3.1 +
 - GCC 4.8 +
 - Python 3.6 +
 
## Compilation

Pour compiler manuellement à partir du dossier du projet, faites :

```
mkdir -p build
cd build
cmake ../
make
```

Vous obtiendrez les exécutables dans le dossier en cours "build".

## VS Code

Le dossier du projet peut être ouvert dans Visual Studio Code et utilise les
extensions "Remote - Containers" (et donc Docker Desktop). 
Des configurations pour lancer dans le conteneur le code de l'APP et les trois
exercices du laboratoire sont disponibles.
La compilation est également générée dans "build/"

## Contenu

**CMakeLists.txt** La configuration de la compilation. Vous pouvez changer le
mode par défaut "Debug" pour "Release" ou "RelWithDebInfo". Attention, ceci
provoque beaucoup plus d'erreurs ! Tentez d'exécuter le programme en "Debug" au
départ pour mieux comprendre où sont les problèmes.

**src/asset_conv.cpp** Le coeur de l'APP et le code à modifier.

**src/lab_ex?.cpp** Les exercices du laboratoire

**scripts/gen_tasks.py** Permet de générer une liste de fichiers à traiter à
partir d'un dossier. S'attend à être exécuté depuis le dossier build/. Vous
pouvez donc faire :

```
mkdir output/
../scripts/gen_tasks.py ../data ./output/ 480 | ./asset_conv
```

Pour convertir toutes les images dans data/ vers le dossier build/output/ à une
taille de 480 pixels.

**scripts/multi_proc.py** Un script Python permettant de lancer plusieurs
sous-processus asset_conv. Attend la fin de la liste de tâches, puis divise en N
sous-listes et les envoies à N sous-processus. S'attend aussi à être exécuté
sous build/.

**scripts/run_batch.sh** Script bash à lancer depuis build/ pour faire la
conversion automatique de tous les fichiers dans data/. Donne le temps
d'exécution à la fin.

**scripts/run_batch_mp.sh** Comme run_batch.sh, mais pour multi_proc.py.
Toujours à lancer depuis build/.

**waveprop/ftdt_yee.py** Le simulateur de propagation d'ondes. Lance une
interface graphique qui simule la propagation dans le temps. Vous pouvez
utiliser le fichier requirements.txt pour installer les dépendances :

    pip3 install -r requirements.txt

## Éléments importés

[nanosvg](https://github.com/memononen/nanosvg): Pour le chargement et le
dessin des fichiers SVG.

[stb](https://github.com/nothings/stb): Pour la compression et l'écriture en
PNG.

[Google Material design icons](https://github.com/google/material-design-icons):
pour les fichiers à traiter (sous-ensemble).

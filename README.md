# Repo Miscelaneo

No tengo nada definido con lo que voy a hacer aqui, mientras sigo aprendiendo las mañas de Git y Github.


### Para configurar en nuevos entornos:

1. Instalar Git obviamente:
    - En ubuntu: `apt install git`
    - En arch: `pacman -S git`
    - En windows... es windows.
2. Configurar tu usario.
    * `git config --global user.name <usuario>`
    * `git config --global user.email <correo>`


### Comandos basicos:

* Crear directorios `mkdir <nombre carpeta>`
* Navegar entre carpetas: `cd <Folder>`, `cd ..`.
* crear y abrir archivo:
    - vscode : `code <FileName.txt>`.
    - nano : `nano <FileName.txt>`.
* Mover : `mv <File/Folder> <Destino>` (Win: `move`).
* copiar : `cp <File/Folder> <Destino>` (Win: `copy`).
* Crear archivo vacio : `touch File.txt`.
* Listar archivos en carpeta actual : (Win: `dir`) (Linux: `ls`)
* Ubicacion actual : `pwd`
* Eliminar archivos: (Win: `del`) (Linux: `rm`)
* Eliminar carpetas vacias `rd/rmdir`
* Para borrar carpetas con contenido: (Linux: `rm -r <Folder>`) (Win: `rd /s <Folder>`)
* Buscar en texto : `grep "palabra" File.txt`
* Cambiar permisos : `chmod`
* Ver permisos : `chown`

### Pasos para hacer un commit:

1. Selecciona la ruta donde vas a trabajar con `cd <Ubicacion>`.
2. Inicia el repositorio con `git init`.
3. Comprueba el status de Git : `git status`.
4. Selecciona los archivos o carpeta que quieras hacer commit:
    - Para seleccionar archivos  o carpetas : `git add File.txt`.
    - Para seleccionar todo dentro de la carpeta actual : `git add .`
5. Agrega un comentario de lo que haras : `git commit -m "Mi primer commit"`
6. Seleccionamos la branch : `git branch -M main`
7. Añade el repositorio con el cual vas a trabajar : `git remote add origin https://github.com/<user>/repo.git`
8. Pushea los cambios : `git push -u origin main`
9. Aqui te va a pedir user y el token, pero ya estaria listo!

### Trabajar con un fork

1. Ingresa al repositorio al que hareas fork.
2. Haz clic en el botón Fork.
3. Se creará una copia en tu cuenta de GitHub (Recuerda actualizar la info del fork para que este al dia con los cambios del repositorio original).
4. Clona el fork del repositorio (de tu cuenta) `git clone https://github.com/<User>/RepoFork.git`.
5. Sal de la rama principal e inicia una branch: 
    - `git checkout main`.
    - `git pull origin main`.
    - `git checkout -b Nombre-branch`.
6. Luego de esto, puedes crear, modificar y eliminar archivos a tu gusto.
7. Hacemos los pasos anteriores para seleccionar lo que hacermos commit:
    - `git status`.
    - `git add .`.
    - `git commit -m "Agrego x archivos"`.
    - `git push origin Nombre-branch`.
8. Luego de esto, en tu repositorio Frokeado : 
    - GitHub mostrará un botón: "Compare & pull request".
    - Deja un titulo : "Agrego x archivos"
    - Deja un comentario: Breve explicación de lo que hiciste.
    - Asigna al administrador para que te apruebe el Pull Request.
9. Si quieres actalizar el Fork con los datos nuevos del repositorio original :
    - `git remote add upstream https://github.com/<AdminRepo>/RepoOG.git`.
    - `git fetch upstream`.
    - `git checkout main`.
    - `git merge upstream/main`.
    - `git push origin main`.

### Buenas practicas:
- Crea una rama nueva para cada tarea.
- Nombra de forma reconocible carpetas y archivos.
- Asegúrate de que todo funcione antes de hacer pull request.
- Mantén tu fork actualizado con el del administrador.

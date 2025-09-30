import os

class GestionadorArchivos:
    def __init__(self, directorio):
        self.directorio = directorio

    def listar_archivos(self):
        return os.listdir(self.directorio)

    def crear_archivo(self, archivo):
        open(f"{self.directorio}/{archivo}", "w").close()

    def eliminar_archivo(self, archivo):
        os.remove(f"{self.directorio}/{archivo}")

    def renombrar_archivo(self, nombre_antiguo, nuevo_nombre):
        os.rename(f"{self.directorio}/{nombre_antiguo}", f"{self.directorio}/{nuevo_nombre}")

    @staticmethod
    def extension_archivo(nombreArchivo):
        return os.path.splitext(nombreArchivo)[1]

class GestionadorArchivosAudio(GestionadorArchivos):
    def __init__(self, directorio):
        super().__init__(directorio)

    def listar_archivos_audio(self):
        extensiones_archivo_audio = (".mp3", ".wav", ".flac")
        return [f for f in self.listar_archivos() if GestionadorArchivosAudio.extension_archivo(f) in extensiones_archivo_audio]

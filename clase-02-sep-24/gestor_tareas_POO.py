class Tarea:
    def __init__(self, titulo):
        self.titulo = titulo
        self.completado = False

    def marcar_completada(self):
        self.completado = True

    def __str__(self):
        if self.completado:
            estado = 'Completado'
        else: 
            estado = 'Pendiente'
        
        return f"{self.titulo} : {estado}"

class ListarTareas:
    def __init__(self):
        self.tarea = []

    def agregar_tarea(self, titulo):
        tarea = Tarea(titulo)
        self.tarea.append(tarea)
        print(f"Tarea {titulo} agregada")

    
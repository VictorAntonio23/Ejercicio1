class Cuenta:
  def __init__ (self,ct,t,p):
    self.cantidad=ct
    self.tipo=t
    self.propietario=p
  def imprimirDetalles(self):
    print("cantidad::",self.cantidad)
    print("el tipo es::",self.tipo)
    print("el propietario es::",self.propietario)

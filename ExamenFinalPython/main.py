import modulos.menus as menus
import modulos.administrador as administrador

if __name__ == '__main__':
    while(True):
        print(menus.BienvenidoaMovistar)
        print(menus.menuInicio)
        sesion = True
        opMenuInicio = int(input(":)"))
        match opMenuInicio:
            case 1:
                while True:
                    if (sesion==True):
                        print(menus.menuResgistroGestion)
                        opMenuResgistroGestion = int(input(":)"))
                    
                        match opMenuResgistroGestion:
                            case 1:
                                pass
                            case 2:
                                campLog = administrador.ingresarAdministrador(administrador.administradorInfo)
                            case 3:
                                break

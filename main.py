# Modulos del sistema
import sys

# Importacion para interface grafica.
from PyQt5 import QtCore, QtWidgets

# Importacion cada una de las ventanas y backend.
from source.reposo import MainWindow
from source.lectorQR import Webcam
from source.informacion import InfoWindow
from source.despacho import DespWindow
from source.cobro import CompWindow
from source.backend import WorkerThreadBackend

# Inicio de la ventana main.
temperatura = 0
humedad = 0
_translate = QtCore.QCoreApplication.translate


class Controller:
    '''
    Clase que controla la secuencia de pantallas a mostrar en
    interface grafica.
    '''

    def __init__(self):
        self.window_main = MainWindow()

        # Crea hilo del backend de la maquina
        self.worker_backend = WorkerThreadBackend()
        self.worker_backend.start()

        # Nivel de tanque en pantalla reposo.
        self.worker_backend.porcentaje_bajo.connect(self.nivel_tanque_bajo)
        self.worker_backend.porcentaje_medio.connect(self.nivel_tanque_medio)
        self.worker_backend.porcentaje_alto.connect(self.nivel_tanque_alto)
        self.worker_backend.vacio.connect(self.nivel_tanque_vacio)

        # Cambiar etiqueta de pantalla principal.
        self.worker_backend.produciendo.connect(
            lambda: self.window_main.OnOff.setText(
                _translate(
                    "AquaPlanetMain",
                    "<html><head/><body>\
                        <p align=\"center\">Produciendo</p>\
                    </body></html>"
                )
            )
        )
        self.worker_backend.reposo.connect(
            lambda: self.window_main.OnOff.setText(
                _translate(
                    "AquaPlanetMain",
                    "<html><head/><body>\
                        <p align=\"center\">Reposo</p>\
                    </body></html>"
                )
            )
        )

    def nivel_tanque_vacio(self):
        self.window_main.nivelTanque.setValue(0)
        self.window_main.nivel_agua = 'v'

    def nivel_tanque_bajo(self):
        self.window_main.nivelTanque.setValue(20)
        self.window_main.nivel_agua = 'a'

    def nivel_tanque_medio(self):
        self.window_main.nivelTanque.setValue(60)
        self.window_main.nivel_agua = 'b'

    def nivel_tanque_alto(self):
        self.window_main.nivelTanque.setValue(100)
        self.window_main.nivel_agua = 'c'

    def show_main(self):
        '''
        Muestra pantalla de reposo.
        '''
        self.window_main.switch_window.connect(self.show_lectorQR)
        self.window_main.showFullScreen()

    def show_lectorQR(self):
        '''
        Muestra pantalla de lector QR
        '''
        self.window_lectorQR = Webcam()
        self.window_lectorQR.switch_window.connect(self.show_info)
        self.window_lectorQR.return_window.connect(
            lambda: self.return_cancelar(self.window_lectorQR)
        )
        self.window_main.close()
        self.window_lectorQR.showFullScreen()

    def show_info(self, codigo):
        '''
        Mestra la pantalla de informacion del usuario
        '''
        self.inf_window = InfoWindow(codigo)
        self.inf_window.return_window.connect(
            lambda: self.return_cancelar(self.inf_window)
        )
        self.inf_window.switch_window.connect(self.show_despacho)
        self.window_lectorQR.close()
        self.inf_window.showFullScreen()

    # Funciones para activar y desactivar la bomba de agua en hilo backend.
    def bomba_on(self):
        '''
        Enciende bomba de agua
        '''
        self.worker_backend.bomba = True

    def bomba_off(self):
        '''
        Apaga bomba de agua
        '''
        self.worker_backend.bomba = False

    def show_despacho(self, id_usuario, saldo_disponible, codigo):
        '''
        Muestra la pantalla donde se despacha el agua
        '''
        self.des_window = DespWindow(id_usuario, saldo_disponible, codigo)
        self.des_window.switch_window.connect(self.show_compra)
        self.des_window.bomba_on.connect(self.bomba_on)
        self.des_window.bomba_off.connect(self.bomba_off)
        self.inf_window.close()
        self.des_window.showFullScreen()

    def show_compra(self, id_usuario, litros_despachados, codigo):
        '''
        Muestra la pantalla donde se realiza la compra del agua
        '''
        self.com_window = CompWindow(id_usuario, litros_despachados, codigo)
        self.com_window.switch_window.connect(
            lambda: self.return_cancelar(self.com_window)
        )
        self.des_window.button_could.close()
        self.des_window.button_warm.close()
        self.des_window.flujometro.close()
        self.des_window.valve_cloud.close()
        self.des_window.valve_warm.close()
        self.des_window.close()
        self.com_window.showFullScreen()

    def return_cancelar(self, ventana):
        '''
        Manejador de el boton cancelar, regresa a su estado de reposo
        '''
        self.window_main = MainWindow()
        ventana.close()
        self.show_main()

    def return_timer(self, ventana):
        '''
        Manejador por tiempo de uso en pantalla para regresar.
        '''
        self.timer_return_ventana = QtCore.QTimer(self)
        self.timer_return_ventana.setSingleShot(True)
        self.timer_return_ventana.singleShot(3000, self.return_cancelar(ventana))


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        controller = Controller()
        controller.show_main()
        app.exec_()
    except:
        print("Exiting...")

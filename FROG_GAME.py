from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QWidget
from PyQt5.QtGui import QIcon, QPixmap

WIN_SPC = 50
BTN_SIZE = 50
FIELD_X = 10
FIELD_Y = 10
WIN_WIDTH = BTN_SIZE*FIELD_X + 2 * WIN_SPC
WIN_HEIGHT = BTN_SIZE*FIELD_Y + 2 * WIN_SPC


class MainWindow(QMainWindow):

    Frog_Coords = [0,0]

    def __init__(self) -> None:

        super().__init__()

        self.setFixedSize(WIN_WIDTH, WIN_HEIGHT)

        self.setWindowTitle("Froggy")

        self.lbl = QLabel("Field number", self)

        self.lbl.setFixedWidth(WIN_WIDTH)
        
        self.lbl.move(WIN_SPC+BTN_SIZE, 0)
        
        self.drawField()

        self.drawFrog()


        

    def drawField(self) -> None:       
        
        self.btns = [] # Кнопки будем хранить в списке как поле класса(изза селф)


        for i in range(FIELD_Y):
            for j in range(FIELD_X):
                #x = WIN_SPC + BTN_SIZE * j
                #y = WIN_SPC + BTN_SIZE * i
                btn = QPushButton(str(j+1) + '-' + str(i+1), self)
                btn.setFixedSize(BTN_SIZE, BTN_SIZE)
                btn.move(WIN_SPC + BTN_SIZE * j
                         ,WIN_SPC + BTN_SIZE * i)
                btn.setCheckable(True)
                
                # взяли обьект btn, создали сигнал clicked, создали слот  connect и описали обработчик в скобках
                # lambda это анонимная функция которая вызывает функци. обработчика, но с параметрами
                btn.clicked.connect(lambda clicked, b = btn: self.btn_clicked(b))
                
                self.btns.append(btn)
    
    def btn_clicked(self, b) -> None:
        # print(self.sender().text())
        self.lbl.setText("Field number: " + b.text())

    def keyPressEvent(self, event) -> None:
        key = event.key()

        match chr(key):
            case 'A': # Left
                self.frogMove(self.Frog_Coords[0]-1,
                              self.Frog_Coords[1])
                
            case 'D': # Right
                self.frogMove(self.Frog_Coords[0]+1,
                              self.Frog_Coords[1])
            case 'W': #Up
                self.frogMove(self.Frog_Coords[0],
                              self.Frog_Coords[1]-1)
            case 'S': #Down
                self.frogMove(self.Frog_Coords[0],
                              self.Frog_Coords[1]+1)
        print (chr(key), self.Frog_Coords)
    
    def drawFrog(self):
        self.frog = QPushButton(self)
        self.frog.setFixedSize(BTN_SIZE, BTN_SIZE)
        #icon = QIcon(QPixmap("/home/xobi_van/Downloads/frog.jpg"))
        #self.frog.setIcon(icon)

        self.frog.setStyleSheet("border: 0px solid green;"
                                "background-color: white;"
                                "border-radius: 25px;"
                                "image: url(/home/xobi_van/Downloads/frog.jpg)")
        
        x,y = self.Frog_Coords[0],self.Frog_Coords[1]
        
        self.frogMove(x,y)
        
    def frogMove(self,x,y):
        if self.validateCoords(x,y):
            self.frog.move(WIN_SPC + x*BTN_SIZE,
                           WIN_SPC + y*BTN_SIZE)
            self.Frog_Coords = [x,y]


    def validateCoords(self, x,y) -> bool:
        if 0<=x<FIELD_X and 0<=y<FIELD_Y and self.btns[y*FIELD_X+x].isChecked() == False:
            return True
        else:
            return False



def main():
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec()

main()
from views.dashbord5 import Ui_MainWindow,QMainWindow,QApplication
from PySide6.QtCore import *
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import *
from PySide6.QtGui import QIcon 
from PySide6.QtWidgets import QSizeGrip  ,QGraphicsOpacityEffect
import sys
from PySide6.QtCore import QTimer
from views.notification import NotificationWindow
from views.dashbord5 import Ui_MainWindow

#main classe
class DashboardWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        QTimer.singleShot(1000, lambda: self.showNotification("Welcome to UIT Library!"))

        #hide window tittle bar
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background: rgba(0, 0, 0, 100);")  # ✅ Set semi-transparent background
        self.resize(900, 700)  # Set a default size

        #shadow
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius (50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        
        #app shadow to sentral widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        #icon
        self.setWindowIcon(QIcon(":/icons/uit-dark.png"))
        self.setWindowTitle(("UIT Library"))
        #set size grip to size window
        QSizeGrip(self.ui.size_grip)  

        # Example: Show notification when window opens
        QTimer.singleShot(1000, lambda: self.showNotification("Welcome to UIT Library!"))

        #minimize window
        self.ui.minimize_btn.clicked.connect(self.showMinimized)
        #close window
        self.ui.close_btn.clicked.connect(self.close)
        #exit
        self.ui.exit_btn.clicked.connect(self.close)
        #maximize window
        self.ui.restore_win_btn.clicked.connect(self.restore_or_maximize_window)
        # Allow window dragging by tracking mouse events
        self.dragging = False
        self.offset = QPoint()
        self.ui.centralwidget.mousePressEvent = self.mousePressEvent
        self.ui.centralwidget.mouseMoveEvent = self.mouseMoveEvent
        self.ui.centralwidget.mouseReleaseEvent = self.mouseReleaseEvent
        
        #left menu toogle
        self.ui.menu_btn.clicked.connect(self.slideLeftMenu)
        #animation################################
        self.fadeInAnimation()
        #animation boutton
        self.ui.menu_btn.pressed.connect(lambda: self.animateButtonPress(self.ui.menu_btn))
        #animation pages
        #self.ui.menu_btn.clicked.connect(lambda: self.changePageWithAnimation(1))  # Switch to page 1
        # Connect buttons to pages with animation
        self.ui.home_btn.clicked.connect(lambda: self.changePageWithAnimation(self.ui.home_page))
        self.ui.book_btn.clicked.connect(lambda: self.changePageWithAnimation(self.ui.book_page))
        self.ui.author_btn.clicked.connect(lambda: self.changePageWithAnimation(self.ui.author_page))
        self.ui.loan_btn.clicked.connect(lambda: self.changePageWithAnimation(self.ui.management_page))  # Loans Page
        self.ui.sub_btn.clicked.connect(lambda: self.changePageWithAnimation(self.ui.sub_page))  # Subscribers Page
        self.setStyleSheet("""
            QMainWindow {
                background-color: rgb(255, 255, 255);  /* Set window background */
                border-radius: 10px;  /* Rounded corners */
            }
        """)

        self.ui.notification_btn.clicked.connect(lambda: self.showNotification("You have a new notification!"))
        
        self.show()

    def setup_table(self):
        """Configure the QTableWidget to resize properly."""
        self.tableWidget_books.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_books.verticalHeader().setVisible(False)  # Hide row numbers

        
    from PySide6.QtCore import QPropertyAnimation
    def showNotification(self, message="New Notification!"):
        """Creates and displays a floating notification at the button's location."""

        # ✅ Get the notification button's global position
        btn_position = self.ui.notification_btn.mapToGlobal(QPoint(0, self.ui.notification_btn.height()))

        # ✅ Adjust notification position (so it appears below the button)
        notification_x = btn_position.x()  # Same X position
        notification_y = btn_position.y() + 10  # Move slightly below the button

        # ✅ Create and show the notification
        self.notification = NotificationWindow(message, position=QPoint(notification_x, notification_y))
        self.notification.show()

    def addHoverAnimation(self, button):
        """Create a hover effect that scales the button when hovered."""
        button.enterEvent = lambda event: self.animateButton(button, 1.1)  # Scale up
        button.leaveEvent = lambda event: self.animateButton(button, 1.0)  # Scale down

    def animateButton(self, button, scale_factor):
        """Apply scaling animation to the button."""
        animation = QPropertyAnimation(button, b"geometry")
        animation.setDuration(150)
        
        # Get current geometry
        rect = button.geometry()
        new_width = int(rect.width() * scale_factor)
        new_height = int(rect.height() * scale_factor)
        offset_x = (new_width - rect.width()) // 2
        offset_y = (new_height - rect.height()) // 2

        animation.setStartValue(rect)
        animation.setEndValue(rect.adjusted(-offset_x, -offset_y, offset_x, offset_y))
        animation.setEasingCurve(QEasingCurve.OutCubic)
        animation.start()
    from views.notification import NotificationWindow  # ✅ Import Notification Class

    def showNotification(self, message="New Notification!"):
        """Displays a floating notification when the notification button is clicked."""
        self.notification = NotificationWindow(message)
        self.notification.show()

    def changePageWithAnimation(self, index):
        """Apply a sliding animation when changing pages in QStackedWidget."""
        current_index = self.ui.stackedWidget.currentIndex()
        next_index = index

        if current_index == next_index:
            return  # No need to animate if already on the page

        # ✅ Create animation for smooth transition
        self.page_animation = QPropertyAnimation(self.ui.stackedWidget, b"geometry")
        self.page_animation.setDuration(300)  # ✅ Adjust speed
        self.page_animation.setEasingCurve(QEasingCurve.OutCubic)

        # Move pages left or right based on index
        offset = self.ui.stackedWidget.width()
        start_pos = QRect(self.ui.stackedWidget.x() + offset, self.ui.stackedWidget.y(), self.ui.stackedWidget.width(), self.ui.stackedWidget.height())
        end_pos = QRect(self.ui.stackedWidget.x(), self.ui.stackedWidget.y(), self.ui.stackedWidget.width(), self.ui.stackedWidget.height())

        self.ui.stackedWidget.setCurrentIndex(next_index)
        self.ui.stackedWidget.setGeometry(start_pos)
        self.page_animation.setStartValue(start_pos)
        self.page_animation.setEndValue(end_pos)
        self.page_animation.start()

    def restore_or_maximize_window(self): 
        # If window is maxmized 
        if self.isMaximized():
            self.showNormal()
            # Change Icon
            self.ui.restore_win_btn.setIcon(QIcon(u":/icons/minimize.png"))
        else:
            self.showMaximized()
            # Change Icon
            self.ui.restore_win_btn.setIcon(QIcon(u":/icons/maximize.png"))
    
    def mousePressEvent(self, event):
        """Track the mouse position for dragging."""
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.globalPosition().toPoint() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        """Move the window while dragging."""
        if self.dragging:
            self.move(event.globalPosition().toPoint() - self.offset)
            event.accept()

    def mouseReleaseEvent(self, event):
        """Stop dragging."""
        self.dragging = False
    
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.side_menu_container.width()
        # If minimized
        if width == 0: 
            # Expand menu 
            newWidth = 200
            self.ui.menu_btn.setIcon(QIcon(u":/icons/double-left.png"))
            # If maximized
        else:
        # Restore menu newwidth
            newWidth = 0
            self.ui.menu_btn.setIcon(QIcon(u":/icons/align-left.png"))
        self.animation = QPropertyAnimation(self.ui.side_menu_container, b"maximumWidth")  # ✅ Correct initialization

        self.animation.setDuration(150)
        self.animation.setStartValue(width) #Start value is the current menu width 
        self.animation.setEndValue(newWidth) #end value is the new menu width 
        self.animation.setEasingCurve(QEasingCurve.OutCubic)  # ✅ Smoother & faster
        self.animation.start()
    def fadeInAnimation(self):
        """Apply a fade-in effect to the central widget instead of the full window."""
        self.effect = QGraphicsOpacityEffect(self.ui.centralwidget)  # ✅ Apply to central widget
        self.ui.centralwidget.setGraphicsEffect(self.effect)  # ✅ Fix

        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(600)  # ✅ Adjust speed
        self.animation.setStartValue(0)  # ✅ Start fully transparent
        self.animation.setEndValue(1)    # ✅ Fully visible
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.start()


    #animation bouton
    def animateButtonPress(self, button):
        """Animate button press with a scaling effect."""
        self.buttonAnimation = QPropertyAnimation(button, b"geometry")
        self.buttonAnimation.setDuration(150)
        self.buttonAnimation.setStartValue(button.geometry())
        self.buttonAnimation.setEndValue(button.geometry().adjusted(2, 2, -2, -2))  # Shrink slightly
        self.buttonAnimation.setEasingCurve(QEasingCurve.OutCubic)
        self.buttonAnimation.start()
    #animation between pages
    def changePageWithAnimation(self, index):
        """Apply a sliding animation when changing pages in QStackedWidget."""
        self.pageAnimation = QPropertyAnimation(self.ui.stackedWidget, b"geometry")
        self.pageAnimation.setDuration(250)
        self.pageAnimation.setStartValue(QRect(self.ui.stackedWidget.x() + 50, self.ui.stackedWidget.y(), self.ui.stackedWidget.width(), self.ui.stackedWidget.height()))
        self.pageAnimation.setEndValue(self.ui.stackedWidget.geometry())
        self.pageAnimation.setEasingCurve(QEasingCurve.OutCubic)
        self.pageAnimation.start()

        self.ui.stackedWidget.setCurrentIndex(index)
    def changePageWithAnimation(self, page):
        """Apply a sliding animation when changing pages in QStackedWidget."""
        current_index = self.ui.stackedWidget.currentIndex()
        next_index = self.ui.stackedWidget.indexOf(page)

        if current_index == next_index:
            return  # No need to animate if already on the page

        # ✅ Create animation for smooth transition
        self.page_animation = QPropertyAnimation(self.ui.stackedWidget, b"geometry")
        self.page_animation.setDuration(300)  # ✅ Adjust speed
        self.page_animation.setEasingCurve(QEasingCurve.OutCubic)

        # Move pages left or right based on index
        offset = self.ui.stackedWidget.width()
        start_pos = QRect(self.ui.stackedWidget.x() + offset, self.ui.stackedWidget.y(),
                        self.ui.stackedWidget.width(), self.ui.stackedWidget.height())
        end_pos = QRect(self.ui.stackedWidget.x(), self.ui.stackedWidget.y(),
                        self.ui.stackedWidget.width(), self.ui.stackedWidget.height())

        self.ui.stackedWidget.setCurrentWidget(page)
        self.ui.stackedWidget.setGeometry(start_pos)
        self.page_animation.setStartValue(start_pos)
        self.page_animation.setEndValue(end_pos)
        self.page_animation.start()

  
if __name__ == '__main__':
    app=QApplication(sys.argv)
    window=DashboardWindow( )
    window.show()
    sys.exit(app.exec())
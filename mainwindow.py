from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow, QMessageBox, QMenu
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from ui_pick_watch import Ui_MainWindow
import qdarkstyle
from models import ContentItem, Movie, Anime, FavList, MovieFavList, AnimeFavList
from api import obtain_movie, obtain_movie_poster, obtain_anime, obtain_anime_poster

class MainWindow(QMainWindow):
    """Main application window that handles UI events, search, and content display.
    Supports movie and anime in separate modes."""
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Pick&Watch")
        
        self.ui.search_button.clicked.connect(self.search)
        self.ui.input.returnPressed.connect(self.search)

        self.curr_content = None
        self.ui.fav_pushbutton.clicked.connect(lambda: self.add_to_fav(self.curr_content))
        self.ui.fav_list.itemClicked.connect(self.display_selected)
        self.movie_fav_manager = MovieFavList()
        self.anime_fav_manager = AnimeFavList()

        self.fav_manager = self.movie_fav_manager
        self.ui.toggle_button.setText("Movie")
        self.mode = 0
        QApplication.instance().setStyleSheet(qdarkstyle.load_stylesheet(qt_api="pyside6"))

        # Toggle mode
        self.ui.toggle_button.clicked.connect(self.switch_mode)

        # Delete on right click with context menu
        self.ui.fav_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.fav_list.customContextMenuRequested.connect(self.show_context_menu)

        # Save/load
        self.ui.actionSave_my_list.triggered.connect(self.fav_manager.save_to_file)
        self.ui.actionLoad_my_list.triggered.connect(lambda: self.display_fav(self.fav_manager.load_from_file()))
    
    def switch_mode(self):
        """Siwtch between anime and movie mode"""
        self.ui.actionSave_my_list.triggered.disconnect()
        self.ui.actionLoad_my_list.triggered.disconnect()
        if self.mode == 0:
            self.mode = 1
            self.ui.toggle_button.setText("Anime")
            self.ui.fav_list.clear()
            self.fav_manager = self.anime_fav_manager #backend change
            self.clear_display()

            QApplication.instance().setStyleSheet("")
            self.ui.actionSave_my_list.triggered.connect(self.fav_manager.save_to_file)
            self.ui.actionLoad_my_list.triggered.connect(lambda: self.display_fav(self.fav_manager.load_from_file()))

        else:
            self.mode = 0
            self.ui.toggle_button.setText("Movie")
            self.fav_manager = self.movie_fav_manager
            self.ui.fav_list.clear()
            self.clear_display()

            QApplication.instance().setStyleSheet(qdarkstyle.load_stylesheet(qt_api="pyside6"))
            self.ui.actionSave_my_list.triggered.connect(self.fav_manager.save_to_file)
            self.ui.actionLoad_my_list.triggered.connect(lambda: self.display_fav(self.fav_manager.load_from_file()))

    def clear_display(self):
        """Clear title, release, description, and poster display"""
        self.ui.title_display.setText("")
        self.ui.release_display.setText("")
        self.ui.desc_display.setText("")
        self.ui.poster_display.setPixmap(QPixmap())

    def search(self):
        """Search for a content given a title and return/display a title, release date, overview, and poster"""
        title = self.ui.input.text()
        self.ui.input.clear()

        # Obtain movie/anime
        if self.mode == 0:
            content_obj = obtain_movie(title)
        else:
            content_obj = obtain_anime(title)

        # Display movie/anime
        if content_obj == None:
            self.error_message()
        else:
            self.ui.title_display.setText(content_obj.title)
            self.ui.release_display.setText(content_obj.release_date)

            self.ui.desc_display.setText(content_obj.overview)

            self.load_poster(content_obj)
        
        self.curr_content = content_obj # Update the current content
    
    def load_poster(self, content_obj):
            """load the poster given a content item"""
            pixmap = QPixmap()
            poster_data = None
            
            if self.mode == 0:
                poster_data = obtain_movie_poster(content_obj.poster)
            else:
                poster_data = obtain_anime_poster(content_obj.poster)

            if poster_data:
                pixmap.loadFromData(poster_data)

            scaled_pixmap = pixmap.scaled(
                self.ui.poster_display.width(),
                self.ui.poster_display.height(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.ui.poster_display.setPixmap(scaled_pixmap)
        
    
    def error_message(self):
        QMessageBox.warning(self, "Title Not Found", "Did you come up with that in your dream? :O")


    def add_to_fav(self, content):
        """Add a content item to the favorite list, with backend updated"""
        if content != None:
            self.ui.fav_list.addItem(content.title)
        
            # Update backend
            self.fav_manager.add(content)
    
    def display_selected(self):
        """Display a content when selected"""
        item = self.ui.fav_list.currentItem()
        if item:
            title = item.text()
            content_obj = self.fav_manager.find(title)
            self.ui.title_display.setText(content_obj.title)
            self.ui.release_display.setText(content_obj.release_date)

            self.ui.desc_display.setText(content_obj.overview)

            self.load_poster(content_obj)
        
            self.curr_content = content_obj
    
    def display_fav(self, favlist):
        """Display the titles of items in a favorite list, without updating backend"""
        self.ui.fav_list.clear()
        for content in favlist:
            self.ui.fav_list.addItem(content.title)
    
    def show_context_menu(self, position):
        """Right click and show a context menu, which has a delete funcction"""
        item = self.ui.fav_list.itemAt(position)
        if item:
            menu = QMenu()
            delete = menu.addAction("Delete")
            action = menu.exec(self.ui.fav_list.mapToGlobal(position))
            
            title = item.text()
            movie_obj = self.fav_manager.find(title)
            if action == delete:
                self.fav_manager.delete(movie_obj)
                self.delete_from_list()
    
    def delete_from_list(self):
        """Update the UI after a title is deleted"""
        self.ui.fav_list.clear()
        self.clear_display()
        self.display_fav(self.fav_manager.favlist)
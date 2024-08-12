from PyQt6.QtWidgets import *
from PyQt6.QtCore import *



class NetworkToolFrontPanel(QWidget):
    """GUI class for Networking Tool"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Network Tool")
        self.setFixedSize(1024, 768)
        self.main_layout = QGridLayout()


        # Network Tool Layout
        self.network_tool_sub_layout_one = QVBoxLayout()
        self.network_tool_sub_layout_two = QHBoxLayout()
        self.get_host_name = QPushButton("Get Host Name")

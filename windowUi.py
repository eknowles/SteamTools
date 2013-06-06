# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scgui.ui'
#
# Created: Mon Jun 03 15:51:58 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(710, 440)
        MainWindow.setMinimumSize(QtCore.QSize(710, 440))
        MainWindow.setMaximumSize(QtCore.QSize(710, 440))
        MainWindow.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/Steam.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStatusTip(_fromUtf8(""))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("QProgressBar:horizontal {\n"
"    background-color: rgba(57,55,54, 255);\n"
"     border-style: solid;\n"
"     border-width: 1px;\n"
"     border-radius: 2px;\n"
"     border-color: rgba(112,109, 105, 255);\n"
"    padding-left:3px;padding-right:3px;\n"
"    color: rgb(218, 218, 218);\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"background: #4d6d8c;\n"
"margin-right: 4px; /* space */\n"
"margin-top:3px;\n"
"margin-bottom:3px;\n"
"width: 8px;\n"
"}\n"
"\n"
"\n"
"QListWidget::item:hover, QTreeWidget::item:hover {\n"
"    background-color: none;\n"
"  border:none;\n"
"color:white;\n"
"}\n"
"QListWidget::item:selected, QTreeWidget::item:selected {\n"
"  border:none;\n"
"    background-color: rgb(49, 65, 89);\n"
"color:white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"     background-color: #4d4b48;\n"
"     color: rgb(165,165,165);\n"
"     padding:3px 0 3px 5px;\n"
"     border-left:1px solid rgba(0,0,0, 40);border-right:none;border-top:none;border-bottom:none;\n"
"text-transform:uppercase;\n"
"    font: 10px \"Arial\";\n"
" }\n"
"QHeaderView::section:hover {\n"
"     color: rgb(255,255,255);\n"
" }\n"
"\n"
" /* style the sort indicator */\n"
" QHeaderView::down-arrow {\n"
"    image: url(:/icons/icons/steam/icon_down_default.tga);\n"
" }\n"
"\n"
" QHeaderView::up-arrow {\n"
"    image: url(:/icons/icons/steam/icon_up_default.tga);\n"
" }\n"
"\n"
"\n"
"QScrollBar {\n"
"background: rgba(215, 214, 213, 10)/*#5d5a58*/;\n"
"border:none;\n"
"border-style:none;\n"
"}\n"
"QScrollBar:horizontal {\n"
"         \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(50, 50, 50, 255), stop:0.5 rgba(0, 0, 0, 0));\n"
"         height: 15px;\n"
"         margin: 0px 23px 1 23px;\n"
"     }\n"
"\n"
"     QScrollBar::handle:horizontal {\n"
"         background:  #615f5c;\n"
"         min-width: 20px;\n"
"         border: 1px solid #615f5c;\n"
"         border-width: 1px;\n"
"         border-radius: 2px;\n"
"         image: url(:/icons/icons/steam/icon_scroll_handle.tga);\n"
"     }\n"
"\n"
"     QScrollBar::handle:horizontal:hover {\n"
"         background: #64615e;\n"
"         border: 1px solid #64615e;\n"
"     }\n"
"     QScrollBar::handle:vertical:hover {\n"
"         background: #64615e;\n"
"         border: 1px solid #64615e;\n"
"     }\n"
"\n"
"     QScrollBar::add-line:horizontal {\n"
"    image: url(:/icons/icons/steam/icon_right_default.tga);\n"
"         background: #5d5a58;\n"
"         width: 19px;\n"
"    margin:0px 1px 1px 0; \n"
"         subcontrol-position: right;\n"
"         subcontrol-origin: margin;\n"
"         border: 1px solid #5e5b58;\n"
"     border-width: 1px;\n"
"     border-radius: 2px;\n"
"     }\n"
"\n"
"     QScrollBar::sub-line:horizontal {\n"
"    image: url(:/icons/icons/steam/icon_left_default.tga);\n"
"         background: #5e5b58;\n"
"         width: 19px;\n"
"         subcontrol-position: top left;\n"
"         subcontrol-origin: margin;\n"
"       border: 1px solid #5d5a58;\n"
"margin:0 0 1px 1px; \n"
"     border-width: 1px;\n"
"     border-radius: 2px;\n"
"     }\n"
"\n"
"     QScrollBar::add-line:horizontal:hover {\n"
"         background: #64615e;\n"
"         border: 1px solid #64615e;\n"
"     }\n"
"     QScrollBar::sub-line:horizontal:hover {\n"
"         background: #64615e;\n"
"         border: 1px solid #64615e;\n"
"     }\n"
"\n"
"     QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"     }\n"
"\n"
"     QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"         background: none;\n"
"     }\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.5 rgba(10, 10, 10, 0), stop:1 rgba(50, 50, 50, 255));\n"
"         width: 15px;\n"
"         margin: 23px 1px 24px 0;\n"
"     }\n"
"\n"
"     QScrollBar::handle:vertical {\n"
"         background:  #615f5c;\n"
"         min-height: 20px;\n"
"         border: 1px solid #615f5c;\n"
"         border-width: 1px;\n"
"     border-radius: 2px;\n"
"image: url(:/icons/icons/steam/icon_scroll_handle.tga);\n"
"     }\n"
"\n"
"     QScrollBar::add-line:vertical {\n"
"         background: #5d5a58;\n"
"         height: 19px;\n"
"    margin:1px 1px 1px 0; \n"
"         subcontrol-position: bottom;\n"
"         subcontrol-origin: margin;\n"
"         border: 1px solid #5d5a58;\n"
"     border-width: 1px;\n"
"     border-radius: 2px;\n"
"    image: url(:/icons/icons/steam/icon_down_default.tga);\n"
"     }\n"
"\n"
"     QScrollBar::add-line:vertical:hover {\n"
"         background: #64615e;\n"
"         border: 1px solid #64615e;\n"
"     }\n"
"\n"
"\n"
"     QScrollBar::sub-line:vertical {\n"
"         background: #5d5a58;\n"
"         height: 19px;\n"
"         subcontrol-position: top left;\n"
"         subcontrol-origin: margin;\n"
"       border: 1px solid #5d5a58;\n"
"margin:1px 1px 0 0 ; \n"
"     border-width: 1px;\n"
"     border-radius: 2px;\n"
"    image: url(:/icons/icons/steam/icon_up_default.tga);\n"
"     }\n"
"     QScrollBar::sub-line:vertical:hover {\n"
"         background: #64615e;\n"
"         border: 1px solid #64615e;\n"
"     }\n"
"     QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"         width: 3px;\n"
"         height: 3px;\n"
"     }\n"
"\n"
"     QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"         background: none;\n"
"\n"
"     }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(92, 89, 86, 255), stop:1 rgba(64, 59, 60, 255));\n"
"     border-style: solid;\n"
"     border-width: 1px;\n"
"     border-radius: 2px;\n"
"     border-color: rgba(112,109, 105, 255);\n"
"    color: rgb(218, 218, 218);\n"
"    text-align:left;\n"
"    padding-left:5px;\n"
"padding-right:20px;\n"
"    text-transform:uppercase;\n"
"    font: 10px \"Arial\";\n"
"height:23px;\n"
" }\n"
" QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(103,100,97, 255), stop:1 rgba(64, 59, 60, 255));\n"
"     border-color: rgba(153,147,141, 255);\n"
" }\n"
" QPushButton:disabled {\n"
"    background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(103,100,97, 255), stop:1 rgba(64, 59, 60, 255));\n"
"     border-color:#666666;\n"
"color:#666666;\n"
" }\n"
"QLabel#bar{background-color:#6b6865;}\n"
" QPushButton#btn_close, QPushButton#btn_minimize {\n"
"     border-width: 0px;\n"
"    color: rgb(218, 218, 218);\n"
"    text-align:left;\n"
"    padding-left:0px;\n"
"background:none;\n"
" }\n"
"\n"
"QMessageBox, QInputDialog {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(92, 89, 86, 255), stop:1 rgba(64, 59, 60, 255));}\n"
" QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(56,54,53, 255), stop:1 rgba(73,71,69, 255));\n"
"     border-color: rgba(112,109,105, 255);\n"
" }\n"
"\n"
"QWidget {color: rgba(209, 207, 205, 255);}\n"
"QWidget:disabled {color: rgba(209, 207, 205, 100);}\n"
"\n"
"QGroupBox {border:none;}\n"
"\n"
"QLineEdit, QTextEdit {\n"
"    background-color: rgba(57,55,54, 255);\n"
"     border-style: solid;\n"
"     border-width: 1px;\n"
"     border-radius: 2px;\n"
"     border-color: rgba(112,109, 105, 255);\n"
"padding-left:5px;\n"
"    color: rgb(218, 218, 218);\n"
" }\n"
"\n"
"QComboBox {\n"
"     border: 1px solid #807c78;\n"
"     border-radius: 2px;\n"
"     padding: 1px 1px 1px 3px;\n"
"     min-width: 6em;\n"
" }\n"
"\n"
" QComboBox:hover {\n"
"\n"
"    background:  #4a4846;\n"
" }\n"
" QComboBox:editable {\n"
"\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5c5956, stop:1 #4a4846);\n"
" }\n"
"\n"
" QComboBox:!editable, QComboBox::drop-down:editable {\n"
"\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5c5956, stop:1 #4a4846);\n"
" }\n"
"\n"
" /* QComboBox gets the \"on\" state when the popup is open */\n"
" QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5c5956, stop:1 #4a4846);\n"
" }\n"
"\n"
" QComboBox:on { /* shift the text when the popup opens */\n"
" }\n"
"\n"
" QComboBox::drop-down {\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 20px;\n"
"    height:15px;\n"
"    margin-top:3px;\n"
"     border-left-width: 1px;\n"
"     border-left-color: #807c78;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 2px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 2px;\n"
" }\n"
"\n"
" QComboBox::down-arrow {\n"
"    right: 1px;\n"
"     image: url(:/icons/dropdown.png);\n"
" }\n"
"\n"
" QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
" }\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    margin-top:1px;\n"
"     border: 1px solid #807c78;\n"
"     border-radius: 2px;\n"
"     background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5c5956, stop:1 #4a4846);\n"
" }\n"
"QComboBox QAbstractItem {\n"
"margin:5px;\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QListWidget,QPlainTextEdit, QTreeWidget {\n"
"    background-image: url(:/icons/viewbg.jpg);\n"
"background-repeat:repeat-x;\n"
"/*    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(56,54,53, 255), stop:1 rgba(73,71,69, 255));*/\n"
"     border-style: solid;\n"
"     border-width: 1px;\n"
"     border-radius: 2px;\n"
"     border-color: rgba(112,109, 105, 255);\n"
"    color: rgb(218, 218, 218);\n"
"background-color:#242322;\n"
"background-attachment:fixed;\n"
" }\n"
"QTreeWidget { \n"
"\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-color: #6b6865; /* same as the pane color */\n"
"    border-top:0px solid;\n"
"\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background-color:#4a4846;\n"
"    border-bottom-color: #6b6865; /* same as the pane color */\n"
"    border-bottom:0px solid;\n"
"    min-width: 5px;\n"
"    padding: 3px 20px 3px 8px;\n"
"    margin-right:2px;\n"
"    margin-bottom:2px;\n"
"    text-transform:uppercase;\n"
"    font: 10px \"Arial\";\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"background-color:#666360;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(107, 104, 101, 255), stop:1 rgba(56, 54, 53, 255));\n"
"    margin-bottom:0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"\n"
"}"))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(11, 39, 688, 389))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.NewstextEdit = QtGui.QTextEdit(self.tab)
        self.NewstextEdit.setGeometry(QtCore.QRect(10, 10, 468, 301))
        self.NewstextEdit.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.NewstextEdit.setReadOnly(True)
        self.NewstextEdit.setObjectName(_fromUtf8("NewstextEdit"))
        self.NewslistWidget = QtGui.QListWidget(self.tab)
        self.NewslistWidget.setGeometry(QtCore.QRect(490, 10, 191, 301))
        self.NewslistWidget.setObjectName(_fromUtf8("NewslistWidget"))
        self.BTN_RefreshNews = QtGui.QPushButton(self.tab)
        self.BTN_RefreshNews.setEnabled(True)
        self.BTN_RefreshNews.setGeometry(QtCore.QRect(570, 320, 111, 23))
        self.BTN_RefreshNews.setAutoDefault(True)
        self.BTN_RefreshNews.setDefault(True)
        self.BTN_RefreshNews.setObjectName(_fromUtf8("BTN_RefreshNews"))
        self.btn_feedback = QtGui.QPushButton(self.tab)
        self.btn_feedback.setEnabled(True)
        self.btn_feedback.setGeometry(QtCore.QRect(450, 320, 111, 23))
        self.btn_feedback.setAutoDefault(True)
        self.btn_feedback.setDefault(True)
        self.btn_feedback.setObjectName(_fromUtf8("btn_feedback"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.configTab = QtGui.QWidget()
        self.configTab.setEnabled(True)
        self.configTab.setObjectName(_fromUtf8("configTab"))
        self.BTN_updateCfg = QtGui.QPushButton(self.configTab)
        self.BTN_updateCfg.setEnabled(True)
        self.BTN_updateCfg.setGeometry(QtCore.QRect(570, 320, 111, 23))
        self.BTN_updateCfg.setAutoDefault(True)
        self.BTN_updateCfg.setDefault(True)
        self.BTN_updateCfg.setObjectName(_fromUtf8("BTN_updateCfg"))
        self.cfglist = QtGui.QListWidget(self.configTab)
        self.cfglist.setGeometry(QtCore.QRect(10, 10, 141, 241))
        self.cfglist.setFrameShape(QtGui.QFrame.StyledPanel)
        self.cfglist.setFrameShadow(QtGui.QFrame.Sunken)
        self.cfglist.setViewMode(QtGui.QListView.ListMode)
        self.cfglist.setUniformItemSizes(False)
        self.cfglist.setWordWrap(False)
        self.cfglist.setObjectName(_fromUtf8("cfglist"))
        self.cfgEdit = QtGui.QPlainTextEdit(self.configTab)
        self.cfgEdit.setGeometry(QtCore.QRect(160, 10, 521, 301))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.cfgEdit.setFont(font)
        self.cfgEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.cfgEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.cfgEdit.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.cfgEdit.setPlainText(_fromUtf8(""))
        self.cfgEdit.setOverwriteMode(False)
        self.cfgEdit.setBackgroundVisible(False)
        self.cfgEdit.setObjectName(_fromUtf8("cfgEdit"))
        self.BTN_cfgadd = QtGui.QPushButton(self.configTab)
        self.BTN_cfgadd.setEnabled(True)
        self.BTN_cfgadd.setGeometry(QtCore.QRect(10, 260, 141, 23))
        self.BTN_cfgadd.setAutoDefault(True)
        self.BTN_cfgadd.setDefault(True)
        self.BTN_cfgadd.setObjectName(_fromUtf8("BTN_cfgadd"))
        self.BTN_cfgdel = QtGui.QPushButton(self.configTab)
        self.BTN_cfgdel.setEnabled(True)
        self.BTN_cfgdel.setGeometry(QtCore.QRect(10, 290, 141, 23))
        self.BTN_cfgdel.setAutoDefault(True)
        self.BTN_cfgdel.setDefault(True)
        self.BTN_cfgdel.setObjectName(_fromUtf8("BTN_cfgdel"))
        self.BTN_cfgshare = QtGui.QPushButton(self.configTab)
        self.BTN_cfgshare.setEnabled(True)
        self.BTN_cfgshare.setGeometry(QtCore.QRect(480, 320, 81, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/games/iconGroups.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_cfgshare.setIcon(icon1)
        self.BTN_cfgshare.setAutoDefault(True)
        self.BTN_cfgshare.setDefault(True)
        self.BTN_cfgshare.setObjectName(_fromUtf8("BTN_cfgshare"))
        self.tabWidget.addTab(self.configTab, _fromUtf8(""))
        self.demosTab = QtGui.QWidget()
        self.demosTab.setEnabled(True)
        self.demosTab.setObjectName(_fromUtf8("demosTab"))
        self.BTN_viewdemo = QtGui.QPushButton(self.demosTab)
        self.BTN_viewdemo.setEnabled(True)
        self.BTN_viewdemo.setGeometry(QtCore.QRect(590, 320, 91, 23))
        self.BTN_viewdemo.setObjectName(_fromUtf8("BTN_viewdemo"))
        self.treedemos = QtGui.QTreeWidget(self.demosTab)
        self.treedemos.setEnabled(True)
        self.treedemos.setGeometry(QtCore.QRect(10, 10, 671, 301))
        self.treedemos.setAutoScrollMargin(16)
        self.treedemos.setProperty("showDropIndicator", False)
        self.treedemos.setIndentation(0)
        self.treedemos.setRootIsDecorated(False)
        self.treedemos.setUniformRowHeights(True)
        self.treedemos.setItemsExpandable(False)
        self.treedemos.setAnimated(True)
        self.treedemos.setWordWrap(True)
        self.treedemos.setColumnCount(8)
        self.treedemos.setObjectName(_fromUtf8("treedemos"))
        item_0 = QtGui.QTreeWidgetItem(self.treedemos)
        self.treedemos.header().setMinimumSectionSize(20)
        self.treedemos.header().setSortIndicatorShown(True)
        self.treedemos.header().setStretchLastSection(True)
        self.tick = QtGui.QLineEdit(self.demosTab)
        self.tick.setGeometry(QtCore.QRect(470, 320, 111, 23))
        self.tick.setText(_fromUtf8(""))
        self.tick.setFrame(True)
        self.tick.setDragEnabled(True)
        self.tick.setObjectName(_fromUtf8("tick"))
        self.tabWidget.addTab(self.demosTab, _fromUtf8(""))
        self.skinsTab = QtGui.QWidget()
        self.skinsTab.setEnabled(True)
        self.skinsTab.setObjectName(_fromUtf8("skinsTab"))
        self.BTN_skinFolder = QtGui.QPushButton(self.skinsTab)
        self.BTN_skinFolder.setGeometry(QtCore.QRect(390, 320, 141, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/folders_explorer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BTN_skinFolder.setIcon(icon2)
        self.BTN_skinFolder.setObjectName(_fromUtf8("BTN_skinFolder"))
        self.btn_OpenGameFolder = QtGui.QPushButton(self.skinsTab)
        self.btn_OpenGameFolder.setGeometry(QtCore.QRect(540, 320, 141, 23))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_OpenGameFolder.setIcon(icon3)
        self.btn_OpenGameFolder.setObjectName(_fromUtf8("btn_OpenGameFolder"))
        self.BTN_uninstallSkin = QtGui.QPushButton(self.skinsTab)
        self.BTN_uninstallSkin.setEnabled(True)
        self.BTN_uninstallSkin.setGeometry(QtCore.QRect(10, 290, 101, 23))
        self.BTN_uninstallSkin.setAutoFillBackground(False)
        self.BTN_uninstallSkin.setCheckable(False)
        self.BTN_uninstallSkin.setObjectName(_fromUtf8("BTN_uninstallSkin"))
        self.BTN_installSkin = QtGui.QPushButton(self.skinsTab)
        self.BTN_installSkin.setEnabled(True)
        self.BTN_installSkin.setGeometry(QtCore.QRect(10, 260, 101, 23))
        self.BTN_installSkin.setAutoFillBackground(False)
        self.BTN_installSkin.setCheckable(False)
        self.BTN_installSkin.setObjectName(_fromUtf8("BTN_installSkin"))
        self.dltypelist = QtGui.QListWidget(self.skinsTab)
        self.dltypelist.setGeometry(QtCore.QRect(10, 10, 101, 171))
        self.dltypelist.setObjectName(_fromUtf8("dltypelist"))
        item = QtGui.QListWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/games/iconWishlist.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.dltypelist.addItem(item)
        item = QtGui.QListWidgetItem()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/games/iconVideo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.dltypelist.addItem(item)
        item = QtGui.QListWidgetItem()
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/games/iconInventory.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon6)
        self.dltypelist.addItem(item)
        item = QtGui.QListWidgetItem()
        item.setIcon(icon1)
        self.dltypelist.addItem(item)
        self.btn_dldownload = QtGui.QPushButton(self.skinsTab)
        self.btn_dldownload.setEnabled(True)
        self.btn_dldownload.setGeometry(QtCore.QRect(10, 190, 101, 23))
        self.btn_dldownload.setAutoFillBackground(False)
        self.btn_dldownload.setCheckable(False)
        self.btn_dldownload.setObjectName(_fromUtf8("btn_dldownload"))
        self.btn_dlupdate = QtGui.QPushButton(self.skinsTab)
        self.btn_dlupdate.setEnabled(False)
        self.btn_dlupdate.setGeometry(QtCore.QRect(10, 220, 101, 23))
        self.btn_dlupdate.setAutoFillBackground(False)
        self.btn_dlupdate.setCheckable(False)
        self.btn_dlupdate.setObjectName(_fromUtf8("btn_dlupdate"))
        self.treeDownloads = QtGui.QTreeWidget(self.skinsTab)
        self.treeDownloads.setEnabled(True)
        self.treeDownloads.setGeometry(QtCore.QRect(120, 10, 561, 271))
        self.treeDownloads.setAutoScrollMargin(16)
        self.treeDownloads.setProperty("showDropIndicator", False)
        self.treeDownloads.setIndentation(0)
        self.treeDownloads.setRootIsDecorated(False)
        self.treeDownloads.setUniformRowHeights(True)
        self.treeDownloads.setItemsExpandable(False)
        self.treeDownloads.setAnimated(False)
        self.treeDownloads.setWordWrap(True)
        self.treeDownloads.setExpandsOnDoubleClick(True)
        self.treeDownloads.setColumnCount(0)
        self.treeDownloads.setObjectName(_fromUtf8("treeDownloads"))
        self.treeDownloads.header().setCascadingSectionResizes(True)
        self.treeDownloads.header().setMinimumSectionSize(20)
        self.treeDownloads.header().setSortIndicatorShown(True)
        self.treeDownloads.header().setStretchLastSection(True)
        self.DownloadProgressBar = QtGui.QProgressBar(self.skinsTab)
        self.DownloadProgressBar.setGeometry(QtCore.QRect(120, 290, 561, 23))
        self.DownloadProgressBar.setProperty("value", 0)
        self.DownloadProgressBar.setTextVisible(True)
        self.DownloadProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.DownloadProgressBar.setInvertedAppearance(False)
        self.DownloadProgressBar.setObjectName(_fromUtf8("DownloadProgressBar"))
        self.tabWidget.addTab(self.skinsTab, _fromUtf8(""))
        self.toolsTab = QtGui.QWidget()
        self.toolsTab.setObjectName(_fromUtf8("toolsTab"))
        self.SteamTools = QtGui.QGroupBox(self.toolsTab)
        self.SteamTools.setGeometry(QtCore.QRect(10, 10, 191, 111))
        self.SteamTools.setFlat(True)
        self.SteamTools.setObjectName(_fromUtf8("SteamTools"))
        self.ToolButton_DeleteClientReg = QtGui.QPushButton(self.SteamTools)
        self.ToolButton_DeleteClientReg.setEnabled(False)
        self.ToolButton_DeleteClientReg.setGeometry(QtCore.QRect(0, 20, 191, 23))
        self.ToolButton_DeleteClientReg.setObjectName(_fromUtf8("ToolButton_DeleteClientReg"))
        self.ToolButton_ChangeName = QtGui.QPushButton(self.SteamTools)
        self.ToolButton_ChangeName.setGeometry(QtCore.QRect(0, 50, 191, 23))
        self.ToolButton_ChangeName.setObjectName(_fromUtf8("ToolButton_ChangeName"))
        self.ToolButton_EditProfile = QtGui.QPushButton(self.SteamTools)
        self.ToolButton_EditProfile.setGeometry(QtCore.QRect(0, 80, 190, 23))
        self.ToolButton_EditProfile.setObjectName(_fromUtf8("ToolButton_EditProfile"))
        self.GameTools = QtGui.QGroupBox(self.toolsTab)
        self.GameTools.setGeometry(QtCore.QRect(240, 10, 161, 141))
        self.GameTools.setFlat(True)
        self.GameTools.setObjectName(_fromUtf8("GameTools"))
        self.ToolButton_Validate = QtGui.QPushButton(self.GameTools)
        self.ToolButton_Validate.setGeometry(QtCore.QRect(0, 110, 151, 23))
        self.ToolButton_Validate.setObjectName(_fromUtf8("ToolButton_Validate"))
        self.ToolButton_BackupGame = QtGui.QPushButton(self.GameTools)
        self.ToolButton_BackupGame.setGeometry(QtCore.QRect(0, 50, 151, 23))
        self.ToolButton_BackupGame.setObjectName(_fromUtf8("ToolButton_BackupGame"))
        self.ToolButton_ReadUpdates = QtGui.QPushButton(self.GameTools)
        self.ToolButton_ReadUpdates.setGeometry(QtCore.QRect(0, 20, 151, 23))
        self.ToolButton_ReadUpdates.setObjectName(_fromUtf8("ToolButton_ReadUpdates"))
        self.ToolButton_Defrag = QtGui.QPushButton(self.GameTools)
        self.ToolButton_Defrag.setGeometry(QtCore.QRect(0, 80, 151, 23))
        self.ToolButton_Defrag.setObjectName(_fromUtf8("ToolButton_Defrag"))
        self.BroadcastersTools = QtGui.QGroupBox(self.toolsTab)
        self.BroadcastersTools.setGeometry(QtCore.QRect(420, 10, 271, 311))
        self.BroadcastersTools.setObjectName(_fromUtf8("BroadcastersTools"))
        self.BTN_updateTeams = QtGui.QPushButton(self.BroadcastersTools)
        self.BTN_updateTeams.setEnabled(True)
        self.BTN_updateTeams.setGeometry(QtCore.QRect(140, 260, 121, 23))
        self.BTN_updateTeams.setAutoDefault(True)
        self.BTN_updateTeams.setDefault(True)
        self.BTN_updateTeams.setFlat(False)
        self.BTN_updateTeams.setObjectName(_fromUtf8("BTN_updateTeams"))
        self.BTN_refreshteams = QtGui.QPushButton(self.BroadcastersTools)
        self.BTN_refreshteams.setGeometry(QtCore.QRect(10, 20, 251, 23))
        self.BTN_refreshteams.setObjectName(_fromUtf8("BTN_refreshteams"))
        self.BTN_swapSides = QtGui.QPushButton(self.BroadcastersTools)
        self.BTN_swapSides.setEnabled(True)
        self.BTN_swapSides.setGeometry(QtCore.QRect(10, 260, 121, 23))
        self.BTN_swapSides.setObjectName(_fromUtf8("BTN_swapSides"))
        self.Box_t1name = QtGui.QLineEdit(self.BroadcastersTools)
        self.Box_t1name.setEnabled(True)
        self.Box_t1name.setGeometry(QtCore.QRect(10, 50, 251, 23))
        self.Box_t1name.setToolTip(_fromUtf8(""))
        self.Box_t1name.setWhatsThis(_fromUtf8(""))
        self.Box_t1name.setObjectName(_fromUtf8("Box_t1name"))
        self.Box_t1url = QtGui.QLineEdit(self.BroadcastersTools)
        self.Box_t1url.setEnabled(True)
        self.Box_t1url.setGeometry(QtCore.QRect(10, 80, 251, 23))
        self.Box_t1url.setObjectName(_fromUtf8("Box_t1url"))
        self.comboBox_t1flag = QtGui.QComboBox(self.BroadcastersTools)
        self.comboBox_t1flag.setEnabled(True)
        self.comboBox_t1flag.setGeometry(QtCore.QRect(10, 110, 251, 23))
        self.comboBox_t1flag.setFrame(True)
        self.comboBox_t1flag.setObjectName(_fromUtf8("comboBox_t1flag"))
        self.Box_t2name = QtGui.QLineEdit(self.BroadcastersTools)
        self.Box_t2name.setEnabled(True)
        self.Box_t2name.setGeometry(QtCore.QRect(10, 170, 251, 23))
        self.Box_t2name.setObjectName(_fromUtf8("Box_t2name"))
        self.Box_t2url = QtGui.QLineEdit(self.BroadcastersTools)
        self.Box_t2url.setEnabled(True)
        self.Box_t2url.setGeometry(QtCore.QRect(10, 200, 251, 23))
        self.Box_t2url.setObjectName(_fromUtf8("Box_t2url"))
        self.comboBox_t2flag = QtGui.QComboBox(self.BroadcastersTools)
        self.comboBox_t2flag.setEnabled(True)
        self.comboBox_t2flag.setGeometry(QtCore.QRect(10, 230, 251, 23))
        self.comboBox_t2flag.setObjectName(_fromUtf8("comboBox_t2flag"))
        self.Border = QtGui.QLabel(self.toolsTab)
        self.Border.setGeometry(QtCore.QRect(410, 15, 1, 290))
        self.Border.setText(_fromUtf8(""))
        self.Border.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/linebg.jpg")))
        self.Border.setScaledContents(True)
        self.Border.setObjectName(_fromUtf8("Border"))
        self.SteamIDTools = QtGui.QGroupBox(self.toolsTab)
        self.SteamIDTools.setGeometry(QtCore.QRect(10, 130, 191, 171))
        self.SteamIDTools.setFlat(True)
        self.SteamIDTools.setObjectName(_fromUtf8("SteamIDTools"))
        self.ToolButton_URLtoSID = QtGui.QPushButton(self.SteamIDTools)
        self.ToolButton_URLtoSID.setGeometry(QtCore.QRect(0, 80, 191, 23))
        self.ToolButton_URLtoSID.setObjectName(_fromUtf8("ToolButton_URLtoSID"))
        self.ToolButton_SIDtoURL = QtGui.QPushButton(self.SteamIDTools)
        self.ToolButton_SIDtoURL.setGeometry(QtCore.QRect(0, 50, 191, 23))
        self.ToolButton_SIDtoURL.setObjectName(_fromUtf8("ToolButton_SIDtoURL"))
        self.steamidtool = QtGui.QLineEdit(self.SteamIDTools)
        self.steamidtool.setEnabled(True)
        self.steamidtool.setGeometry(QtCore.QRect(0, 20, 191, 23))
        self.steamidtool.setObjectName(_fromUtf8("steamidtool"))
        self.ToolButton_AddFriend = QtGui.QPushButton(self.SteamIDTools)
        self.ToolButton_AddFriend.setGeometry(QtCore.QRect(0, 110, 191, 23))
        self.ToolButton_AddFriend.setObjectName(_fromUtf8("ToolButton_AddFriend"))
        self.ToolButton_SendMessage = QtGui.QPushButton(self.SteamIDTools)
        self.ToolButton_SendMessage.setGeometry(QtCore.QRect(0, 140, 191, 23))
        self.ToolButton_SendMessage.setObjectName(_fromUtf8("ToolButton_SendMessage"))
        self.FriendsTools = QtGui.QGroupBox(self.toolsTab)
        self.FriendsTools.setGeometry(QtCore.QRect(240, 160, 161, 141))
        self.FriendsTools.setFlat(True)
        self.FriendsTools.setObjectName(_fromUtf8("FriendsTools"))
        self.ToolButton_FriendsOffline = QtGui.QPushButton(self.FriendsTools)
        self.ToolButton_FriendsOffline.setGeometry(QtCore.QRect(0, 110, 151, 23))
        self.ToolButton_FriendsOffline.setObjectName(_fromUtf8("ToolButton_FriendsOffline"))
        self.ToolButton_FriendsAway = QtGui.QPushButton(self.FriendsTools)
        self.ToolButton_FriendsAway.setGeometry(QtCore.QRect(0, 50, 151, 23))
        self.ToolButton_FriendsAway.setObjectName(_fromUtf8("ToolButton_FriendsAway"))
        self.ToolButton_FriendsOnline = QtGui.QPushButton(self.FriendsTools)
        self.ToolButton_FriendsOnline.setGeometry(QtCore.QRect(0, 20, 151, 23))
        self.ToolButton_FriendsOnline.setObjectName(_fromUtf8("ToolButton_FriendsOnline"))
        self.ToolButton_FriendsBusy = QtGui.QPushButton(self.FriendsTools)
        self.ToolButton_FriendsBusy.setGeometry(QtCore.QRect(0, 80, 151, 23))
        self.ToolButton_FriendsBusy.setObjectName(_fromUtf8("ToolButton_FriendsBusy"))
        self.Border_2 = QtGui.QLabel(self.toolsTab)
        self.Border_2.setGeometry(QtCore.QRect(220, 15, 1, 290))
        self.Border_2.setText(_fromUtf8(""))
        self.Border_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/linebg.jpg")))
        self.Border_2.setScaledContents(True)
        self.Border_2.setObjectName(_fromUtf8("Border_2"))
        self.tabWidget.addTab(self.toolsTab, _fromUtf8(""))
        self.tabSettings = QtGui.QWidget()
        self.tabSettings.setObjectName(_fromUtf8("tabSettings"))
        self.groupBox_2 = QtGui.QGroupBox(self.tabSettings)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 360, 50))
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.steampath = QtGui.QLineEdit(self.groupBox_2)
        self.steampath.setEnabled(False)
        self.steampath.setGeometry(QtCore.QRect(0, 20, 261, 23))
        self.steampath.setText(_fromUtf8(""))
        self.steampath.setFrame(True)
        self.steampath.setDragEnabled(True)
        self.steampath.setPlaceholderText(_fromUtf8(""))
        self.steampath.setObjectName(_fromUtf8("steampath"))
        self.BTN_steampath = QtGui.QPushButton(self.groupBox_2)
        self.BTN_steampath.setGeometry(QtCore.QRect(270, 20, 81, 23))
        self.BTN_steampath.setObjectName(_fromUtf8("BTN_steampath"))
        self.groupBox_3 = QtGui.QGroupBox(self.tabSettings)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 60, 671, 51))
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gameoptions = QtGui.QLineEdit(self.groupBox_3)
        self.gameoptions.setGeometry(QtCore.QRect(0, 20, 671, 23))
        self.gameoptions.setText(_fromUtf8(""))
        self.gameoptions.setFrame(True)
        self.gameoptions.setDragEnabled(True)
        self.gameoptions.setObjectName(_fromUtf8("gameoptions"))
        self.groupBox_4 = QtGui.QGroupBox(self.tabSettings)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 110, 671, 51))
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.demooptions = QtGui.QLineEdit(self.groupBox_4)
        self.demooptions.setGeometry(QtCore.QRect(0, 20, 671, 23))
        self.demooptions.setText(_fromUtf8(""))
        self.demooptions.setFrame(True)
        self.demooptions.setDragEnabled(True)
        self.demooptions.setObjectName(_fromUtf8("demooptions"))
        self.groupBox_5 = QtGui.QGroupBox(self.tabSettings)
        self.groupBox_5.setGeometry(QtCore.QRect(380, 10, 311, 51))
        self.groupBox_5.setFlat(True)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.steamid = QtGui.QLineEdit(self.groupBox_5)
        self.steamid.setGeometry(QtCore.QRect(0, 20, 151, 23))
        self.steamid.setText(_fromUtf8(""))
        self.steamid.setFrame(True)
        self.steamid.setDragEnabled(True)
        self.steamid.setObjectName(_fromUtf8("steamid"))
        self.CopySteamIDToClipbaord = QtGui.QPushButton(self.groupBox_5)
        self.CopySteamIDToClipbaord.setGeometry(QtCore.QRect(160, 20, 141, 23))
        self.CopySteamIDToClipbaord.setObjectName(_fromUtf8("CopySteamIDToClipbaord"))
        self.BTN_UpdateSettings = QtGui.QPushButton(self.tabSettings)
        self.BTN_UpdateSettings.setGeometry(QtCore.QRect(560, 320, 111, 23))
        self.BTN_UpdateSettings.setObjectName(_fromUtf8("BTN_UpdateSettings"))
        self.tabWidget.addTab(self.tabSettings, _fromUtf8(""))
        self.game = QtGui.QComboBox(self.centralwidget)
        self.game.setGeometry(QtCore.QRect(20, 380, 211, 23))
        self.game.setSizeIncrement(QtCore.QSize(0, 0))
        self.game.setEditable(False)
        self.game.setFrame(True)
        self.game.setObjectName(_fromUtf8("game"))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/games/css.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.game.addItem(icon7, _fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/games/csgo.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/games/csgo.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.game.addItem(icon8, _fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/games/tf2.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.game.addItem(icon9, _fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/games/hl2dm.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.game.addItem(icon10, _fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/games/cs.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/games/cs.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.game.addItem(icon11, _fromUtf8(""))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/games/dota2.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/games/dota2.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.game.addItem(icon12, _fromUtf8(""))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/games/l4d2.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.game.addItem(icon13, _fromUtf8(""))
        self.BGIMG = QtGui.QLabel(self.centralwidget)
        self.BGIMG.setGeometry(QtCore.QRect(0, 0, 710, 440))
        self.BGIMG.setText(_fromUtf8(""))
        self.BGIMG.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/testbg.png")))
        self.BGIMG.setScaledContents(False)
        self.BGIMG.setObjectName(_fromUtf8("BGIMG"))
        self.apptitle = QtGui.QLabel(self.centralwidget)
        self.apptitle.setGeometry(QtCore.QRect(10, 9, 581, 30))
        self.apptitle.setMargin(0)
        self.apptitle.setIndent(10)
        self.apptitle.setObjectName(_fromUtf8("apptitle"))
        self.btn_close = QtGui.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(680, 14, 15, 15))
        self.btn_close.setText(_fromUtf8(""))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/steam/win32_win_close.tga")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon14)
        self.btn_close.setIconSize(QtCore.QSize(15, 15))
        self.btn_close.setFlat(False)
        self.btn_close.setObjectName(_fromUtf8("btn_close"))
        self.btn_minimize = QtGui.QPushButton(self.centralwidget)
        self.btn_minimize.setGeometry(QtCore.QRect(660, 14, 15, 15))
        self.btn_minimize.setText(_fromUtf8(""))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/steam/win32_win_min.tga")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon15)
        self.btn_minimize.setIconSize(QtCore.QSize(15, 15))
        self.btn_minimize.setFlat(False)
        self.btn_minimize.setObjectName(_fromUtf8("btn_minimize"))
        self.launchgame = QtGui.QPushButton(self.centralwidget)
        self.launchgame.setEnabled(True)
        self.launchgame.setGeometry(QtCore.QRect(240, 380, 81, 23))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/games/iconGames.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.launchgame.setIcon(icon16)
        self.launchgame.setAutoDefault(True)
        self.launchgame.setDefault(True)
        self.launchgame.setObjectName(_fromUtf8("launchgame"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionConfig_Editor = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/axialis.16/Png/16x16/Write2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfig_Editor.setIcon(icon17)
        self.actionConfig_Editor.setObjectName(_fromUtf8("actionConfig_Editor"))
        self.actionDemo_Library = QtGui.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/axialis.16/Png/16x16/Database.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDemo_Library.setIcon(icon18)
        self.actionDemo_Library.setObjectName(_fromUtf8("actionDemo_Library"))
        self.actionGUI_Tool = QtGui.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8(":/axialis.16/Png/16x16/Podcast.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGUI_Tool.setIcon(icon19)
        self.actionGUI_Tool.setObjectName(_fromUtf8("actionGUI_Tool"))
        self.actionShoutcasters_Tool = QtGui.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8(":/axialis.16/Png/16x16/Text Large.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShoutcasters_Tool.setIcon(icon20)
        self.actionShoutcasters_Tool.setObjectName(_fromUtf8("actionShoutcasters_Tool"))
        self.actionSettings = QtGui.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(_fromUtf8(":/axialis.cyan.16/Png/Cyan/16x16/Tool.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon21)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionQuit.setMenuRole(QtGui.QAction.QuitRole)
        self.actionQuit.setIconVisibleInMenu(False)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionDelete_Settings = QtGui.QAction(MainWindow)
        self.actionDelete_Settings.setObjectName(_fromUtf8("actionDelete_Settings"))
        self.actionNew_Config = QtGui.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(_fromUtf8(":/16/icons/16/script_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Config.setIcon(icon22)
        self.actionNew_Config.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionNew_Config.setIconVisibleInMenu(True)
        self.actionNew_Config.setObjectName(_fromUtf8("actionNew_Config"))
        self.actionDelete_Config = QtGui.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(_fromUtf8(":/16/icons/16/script_delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete_Config.setIcon(icon23)
        self.actionDelete_Config.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionDelete_Config.setObjectName(_fromUtf8("actionDelete_Config"))
        self.actionSave_Config = QtGui.QAction(MainWindow)
        self.actionSave_Config.setObjectName(_fromUtf8("actionSave_Config"))
        self.actionView_Changelog = QtGui.QAction(MainWindow)
        self.actionView_Changelog.setObjectName(_fromUtf8("actionView_Changelog"))
        self.actionAdd_to_Steam = QtGui.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(_fromUtf8(":/16/icons/16/steam_icon - add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_to_Steam.setIcon(icon24)
        self.actionAdd_to_Steam.setObjectName(_fromUtf8("actionAdd_to_Steam"))
        self.actionView_Steam_Profile = QtGui.QAction(MainWindow)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(_fromUtf8(":/16/icons/16/steam_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionView_Steam_Profile.setIcon(icon25)
        self.actionView_Steam_Profile.setObjectName(_fromUtf8("actionView_Steam_Profile"))
        self.actionYouTube = QtGui.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(_fromUtf8(":/16/icons/16/youtube.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionYouTube.setIcon(icon26)
        self.actionYouTube.setObjectName(_fromUtf8("actionYouTube"))
        self.actionTumblr = QtGui.QAction(MainWindow)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(_fromUtf8(":/16/icons/16/tumblr.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTumblr.setIcon(icon27)
        self.actionTumblr.setObjectName(_fromUtf8("actionTumblr"))
        self.actionTwitter = QtGui.QAction(MainWindow)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(_fromUtf8(":/16/icons/16/twitter_1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTwitter.setIcon(icon28)
        self.actionTwitter.setObjectName(_fromUtf8("actionTwitter"))

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Steam Tools", None))
        self.NewstextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Verdana,Geneva,sans-serif\'; font-size:8pt;\"><br /></p></body></html>", None))
        self.BTN_RefreshNews.setToolTip(_translate("MainWindow", "Save Changes", None))
        self.BTN_RefreshNews.setStatusTip(_translate("MainWindow", "Click this button to update any changes you have made to the config", None))
        self.BTN_RefreshNews.setText(_translate("MainWindow", "Refresh News", None))
        self.btn_feedback.setToolTip(_translate("MainWindow", "Save Changes", None))
        self.btn_feedback.setStatusTip(_translate("MainWindow", "Click this button to update any changes you have made to the config", None))
        self.btn_feedback.setText(_translate("MainWindow", "Give Feedback", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", " NEWS ", None))
        self.BTN_updateCfg.setToolTip(_translate("MainWindow", "Save Changes", None))
        self.BTN_updateCfg.setStatusTip(_translate("MainWindow", "Click this button to update any changes you have made to the config", None))
        self.BTN_updateCfg.setText(_translate("MainWindow", "Save Changes", None))
        self.BTN_updateCfg.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.cfglist.setSortingEnabled(True)
        self.BTN_cfgadd.setToolTip(_translate("MainWindow", "Save Changes", None))
        self.BTN_cfgadd.setStatusTip(_translate("MainWindow", "Click this button to update any changes you have made to the config", None))
        self.BTN_cfgadd.setText(_translate("MainWindow", "NEW CONFIG", None))
        self.BTN_cfgadd.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.BTN_cfgdel.setToolTip(_translate("MainWindow", "Save Changes", None))
        self.BTN_cfgdel.setStatusTip(_translate("MainWindow", "Click this button to update any changes you have made to the config", None))
        self.BTN_cfgdel.setText(_translate("MainWindow", "DELETE CONFIG", None))
        self.BTN_cfgdel.setShortcut(_translate("MainWindow", "Del", None))
        self.BTN_cfgshare.setToolTip(_translate("MainWindow", "Save Changes", None))
        self.BTN_cfgshare.setStatusTip(_translate("MainWindow", "Click this button to update any changes you have made to the config", None))
        self.BTN_cfgshare.setText(_translate("MainWindow", "SHARE", None))
        self.BTN_cfgshare.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.configTab), _translate("MainWindow", " CONFIGS ", None))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.configTab), _translate("MainWindow", "Config Editor", None))
        self.BTN_viewdemo.setText(_translate("MainWindow", "View Demo", None))
        self.treedemos.setSortingEnabled(True)
        self.treedemos.headerItem().setText(1, _translate("MainWindow", "Date", None))
        self.treedemos.headerItem().setText(2, _translate("MainWindow", "Filename", None))
        self.treedemos.headerItem().setText(3, _translate("MainWindow", "Map", None))
        self.treedemos.headerItem().setText(4, _translate("MainWindow", "Length", None))
        self.treedemos.headerItem().setText(5, _translate("MainWindow", "Player", None))
        self.treedemos.headerItem().setText(6, _translate("MainWindow", "Server", None))
        self.treedemos.headerItem().setText(7, _translate("MainWindow", "Size", None))
        __sortingEnabled = self.treedemos.isSortingEnabled()
        self.treedemos.setSortingEnabled(False)
        self.treedemos.setSortingEnabled(__sortingEnabled)
        self.tick.setPlaceholderText(_translate("MainWindow", "Tick", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.demosTab), _translate("MainWindow", " REPLAYS ", None))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.demosTab), _translate("MainWindow", "Demo Library", None))
        self.BTN_skinFolder.setToolTip(_translate("MainWindow", "Open the skins folder in Explorer", None))
        self.BTN_skinFolder.setStatusTip(_translate("MainWindow", "Open the skins folder in Explorer", None))
        self.BTN_skinFolder.setText(_translate("MainWindow", "Open Downloads", None))
        self.btn_OpenGameFolder.setToolTip(_translate("MainWindow", "Open your game folder in explorer", None))
        self.btn_OpenGameFolder.setStatusTip(_translate("MainWindow", "Open your game folder in explorer", None))
        self.btn_OpenGameFolder.setText(_translate("MainWindow", "Open Game Folder", None))
        self.BTN_uninstallSkin.setToolTip(_translate("MainWindow", "Remove the current skin", None))
        self.BTN_uninstallSkin.setStatusTip(_translate("MainWindow", "Remove the current skin", None))
        self.BTN_uninstallSkin.setText(_translate("MainWindow", "Remove", None))
        self.BTN_installSkin.setToolTip(_translate("MainWindow", "Click to install the selected skin", None))
        self.BTN_installSkin.setStatusTip(_translate("MainWindow", "Click to install the selected skin", None))
        self.BTN_installSkin.setText(_translate("MainWindow", "Install", None))
        __sortingEnabled = self.dltypelist.isSortingEnabled()
        self.dltypelist.setSortingEnabled(False)
        item = self.dltypelist.item(0)
        item.setText(_translate("MainWindow", "Configs", None))
        item = self.dltypelist.item(1)
        item.setText(_translate("MainWindow", "Replays", None))
        item = self.dltypelist.item(2)
        item.setText(_translate("MainWindow", "Maps", None))
        item = self.dltypelist.item(3)
        item.setText(_translate("MainWindow", "GUI", None))
        self.dltypelist.setSortingEnabled(__sortingEnabled)
        self.btn_dldownload.setToolTip(_translate("MainWindow", "Click to install the selected skin", None))
        self.btn_dldownload.setStatusTip(_translate("MainWindow", "Click to install the selected skin", None))
        self.btn_dldownload.setText(_translate("MainWindow", "DOWNLOAD", None))
        self.btn_dlupdate.setToolTip(_translate("MainWindow", "Click to install the selected skin", None))
        self.btn_dlupdate.setStatusTip(_translate("MainWindow", "Click to install the selected skin", None))
        self.btn_dlupdate.setText(_translate("MainWindow", "UPDATE", None))
        self.treeDownloads.setSortingEnabled(True)
        self.DownloadProgressBar.setFormat(_translate("MainWindow", "%p%", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.skinsTab), _translate("MainWindow", " DOWNLOADS ", None))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.skinsTab), _translate("MainWindow", "GUI Tools", None))
        self.SteamTools.setTitle(_translate("MainWindow", "Steam and Player Settings", None))
        self.ToolButton_DeleteClientReg.setText(_translate("MainWindow", "Delete ClientRegistry.blob", None))
        self.ToolButton_ChangeName.setText(_translate("MainWindow", "Change Steam Name", None))
        self.ToolButton_EditProfile.setText(_translate("MainWindow", "Upload New Profile Picture", None))
        self.GameTools.setTitle(_translate("MainWindow", "Game Specific Tools", None))
        self.ToolButton_Validate.setText(_translate("MainWindow", "Validate Game Files", None))
        self.ToolButton_BackupGame.setText(_translate("MainWindow", "Backup Game Files", None))
        self.ToolButton_ReadUpdates.setText(_translate("MainWindow", "Read Updates News", None))
        self.ToolButton_Defrag.setText(_translate("MainWindow", "Defrag Game Files", None))
        self.BroadcastersTools.setTitle(_translate("MainWindow", "Broadcasting Tools", None))
        self.BTN_updateTeams.setText(_translate("MainWindow", "Apply", None))
        self.BTN_refreshteams.setText(_translate("MainWindow", "Retrieve Data", None))
        self.BTN_swapSides.setText(_translate("MainWindow", "Swap Teams", None))
        self.Box_t1name.setStatusTip(_translate("MainWindow", "Enter the Counter-Terrorist team name", None))
        self.Box_t1name.setPlaceholderText(_translate("MainWindow", "Home Team Name", None))
        self.Box_t1url.setStatusTip(_translate("MainWindow", "Enter the text you want under the team name", None))
        self.Box_t1url.setPlaceholderText(_translate("MainWindow", "Home Team URL", None))
        self.Box_t2name.setStatusTip(_translate("MainWindow", "Enter the Terrorist team name", None))
        self.Box_t2name.setPlaceholderText(_translate("MainWindow", "Away Team Name", None))
        self.Box_t2url.setStatusTip(_translate("MainWindow", "Enter the text you want under the team name", None))
        self.Box_t2url.setPlaceholderText(_translate("MainWindow", "Away Team URL", None))
        self.SteamIDTools.setTitle(_translate("MainWindow", "Steam ID Tools", None))
        self.ToolButton_URLtoSID.setText(_translate("MainWindow", "Convert URL to Steam ID", None))
        self.ToolButton_SIDtoURL.setText(_translate("MainWindow", "Convert Steam ID to URL", None))
        self.steamidtool.setStatusTip(_translate("MainWindow", "Enter the Terrorist team name", None))
        self.steamidtool.setPlaceholderText(_translate("MainWindow", "Paste ID/URL", None))
        self.ToolButton_AddFriend.setText(_translate("MainWindow", "Add to steam friends", None))
        self.ToolButton_SendMessage.setText(_translate("MainWindow", "Send a message", None))
        self.FriendsTools.setTitle(_translate("MainWindow", "Steam Friends Status", None))
        self.ToolButton_FriendsOffline.setText(_translate("MainWindow", "Offline", None))
        self.ToolButton_FriendsAway.setText(_translate("MainWindow", "Away", None))
        self.ToolButton_FriendsOnline.setText(_translate("MainWindow", "Online", None))
        self.ToolButton_FriendsBusy.setText(_translate("MainWindow", "Busy", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.toolsTab), _translate("MainWindow", " TOOLS ", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Steam Path", None))
        self.BTN_steampath.setText(_translate("MainWindow", "REFRESH", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Play Game Launch Options", None))
        self.gameoptions.setPlaceholderText(_translate("MainWindow", "e.g. -freq 120 -w 800 -h 600 -novid -dxlevel 81 +fps_max 240", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "View Demo Launch Options", None))
        self.demooptions.setPlaceholderText(_translate("MainWindow", "e.g. -novid -sw +fps_max 240 -w 800 -h 600", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Steam ID", None))
        self.steamid.setToolTip(_translate("MainWindow", "This is the name that will appear when you upload configs/demos", None))
        self.steamid.setPlaceholderText(_translate("MainWindow", "e.g. STEAM_0:0:26262312", None))
        self.CopySteamIDToClipbaord.setText(_translate("MainWindow", "Copy to Clipboard", None))
        self.BTN_UpdateSettings.setText(_translate("MainWindow", "Save changes", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSettings), _translate("MainWindow", " SETTINGS ", None))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tabSettings), _translate("MainWindow", "Settings", None))
        self.game.setToolTip(_translate("MainWindow", "Choose the game you want to edit from this drop down menu", None))
        self.game.setStatusTip(_translate("MainWindow", "Choose the game you want to edit from this drop down menu", None))
        self.game.setItemText(0, _translate("MainWindow", "Counter-Strike: Source", None))
        self.game.setItemText(1, _translate("MainWindow", "Counter-Strike: Global Offensive", None))
        self.game.setItemText(2, _translate("MainWindow", "Team Fortress 2", None))
        self.game.setItemText(3, _translate("MainWindow", "Half-Life 2: Deathmatch", None))
        self.game.setItemText(4, _translate("MainWindow", "Counter-Strike", None))
        self.game.setItemText(5, _translate("MainWindow", "Dota 2 Beta", None))
        self.game.setItemText(6, _translate("MainWindow", "Left 4 Dead 2", None))
        self.apptitle.setText(_translate("MainWindow", "apptitle", None))
        self.launchgame.setToolTip(_translate("MainWindow", "Save Changes", None))
        self.launchgame.setStatusTip(_translate("MainWindow", "Click this button to update any changes you have made to the config", None))
        self.launchgame.setText(_translate("MainWindow", "PLAY", None))
        self.actionConfig_Editor.setText(_translate("MainWindow", "Config Editor", None))
        self.actionConfig_Editor.setShortcut(_translate("MainWindow", "Ctrl+1", None))
        self.actionDemo_Library.setText(_translate("MainWindow", "Demo Library", None))
        self.actionDemo_Library.setShortcut(_translate("MainWindow", "Ctrl+2", None))
        self.actionGUI_Tool.setText(_translate("MainWindow", "GUI Tool", None))
        self.actionGUI_Tool.setShortcut(_translate("MainWindow", "Ctrl+3", None))
        self.actionShoutcasters_Tool.setText(_translate("MainWindow", "Shoutcasters Tool", None))
        self.actionShoutcasters_Tool.setShortcut(_translate("MainWindow", "Ctrl+4", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionSettings.setShortcut(_translate("MainWindow", "Ctrl+,", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionDelete_Settings.setText(_translate("MainWindow", "Delete Settings", None))
        self.actionNew_Config.setText(_translate("MainWindow", "New Config", None))
        self.actionNew_Config.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionDelete_Config.setText(_translate("MainWindow", "Delete Config", None))
        self.actionDelete_Config.setShortcut(_translate("MainWindow", "Ctrl+W", None))
        self.actionSave_Config.setText(_translate("MainWindow", "Save Config", None))
        self.actionSave_Config.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionView_Changelog.setText(_translate("MainWindow", "Changelog", None))
        self.actionAdd_to_Steam.setText(_translate("MainWindow", "Add to Steam", None))
        self.actionView_Steam_Profile.setText(_translate("MainWindow", "View Steam Profile", None))
        self.actionYouTube.setText(_translate("MainWindow", "YouTube", None))
        self.actionTumblr.setText(_translate("MainWindow", "tumblr", None))
        self.actionTwitter.setText(_translate("MainWindow", "twitter", None))

import icons_rc

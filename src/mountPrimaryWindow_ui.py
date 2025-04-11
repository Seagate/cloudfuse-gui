# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mountPrimaryWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_primaryFUSEwindow(object):
    def setupUi(self, primaryFUSEwindow):
        if not primaryFUSEwindow.objectName():
            primaryFUSEwindow.setObjectName(u"primaryFUSEwindow")
        primaryFUSEwindow.resize(622, 261)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(primaryFUSEwindow.sizePolicy().hasHeightForWidth())
        primaryFUSEwindow.setSizePolicy(sizePolicy)
        primaryFUSEwindow.setAnimated(False)
        primaryFUSEwindow.setDocumentMode(False)
        primaryFUSEwindow.setDockOptions(QMainWindow.AllowTabbedDocks)
        self.actionReset_Default_Settings = QAction(primaryFUSEwindow)
        self.actionReset_Default_Settings.setObjectName(u"actionReset_Default_Settings")
        self.advancedSettings_action = QAction(primaryFUSEwindow)
        self.advancedSettings_action.setObjectName(u"advancedSettings_action")
        self.setup_action = QAction(primaryFUSEwindow)
        self.setup_action.setObjectName(u"setup_action")
        self.actionAbout_Qt = QAction(primaryFUSEwindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.actionAbout_CloudFuse = QAction(primaryFUSEwindow)
        self.actionAbout_CloudFuse.setObjectName(u"actionAbout_CloudFuse")
        self.centralwidget = QWidget(primaryFUSEwindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textEdit_output = QTextEdit(self.centralwidget)
        self.textEdit_output.setObjectName(u"textEdit_output")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit_output.sizePolicy().hasHeightForWidth())
        self.textEdit_output.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.textEdit_output, 3, 0, 1, 3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit_mountPoint = QLineEdit(self.centralwidget)
        self.lineEdit_mountPoint.setObjectName(u"lineEdit_mountPoint")

        self.horizontalLayout_3.addWidget(self.lineEdit_mountPoint)

        self.button_browse = QPushButton(self.centralwidget)
        self.button_browse.setObjectName(u"button_browse")

        self.horizontalLayout_3.addWidget(self.button_browse)

        self.checkBox_remount = QCheckBox(self.centralwidget)
        self.checkBox_remount.setObjectName(u"checkBox_remount")
        self.checkBox_remount.setChecked(False)

        self.horizontalLayout_3.addWidget(self.checkBox_remount)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.dropDown_bucketSelect = QComboBox(self.centralwidget)
        self.dropDown_bucketSelect.addItem("")
        self.dropDown_bucketSelect.addItem("")
        self.dropDown_bucketSelect.setObjectName(u"dropDown_bucketSelect")

        self.horizontalLayout_2.addWidget(self.dropDown_bucketSelect)

        self.button_config = QPushButton(self.centralwidget)
        self.button_config.setObjectName(u"button_config")

        self.horizontalLayout_2.addWidget(self.button_config)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.button_mount = QPushButton(self.centralwidget)
        self.button_mount.setObjectName(u"button_mount")

        self.gridLayout.addWidget(self.button_mount, 2, 0, 1, 1)

        self.button_unmount = QPushButton(self.centralwidget)
        self.button_unmount.setObjectName(u"button_unmount")

        self.gridLayout.addWidget(self.button_unmount, 2, 1, 1, 1)

        primaryFUSEwindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(primaryFUSEwindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 622, 22))
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        primaryFUSEwindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(primaryFUSEwindow)
        self.statusbar.setObjectName(u"statusbar")
        primaryFUSEwindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_Help.addAction(self.actionAbout_Qt)
        self.menu_Help.addAction(self.actionAbout_CloudFuse)

        self.retranslateUi(primaryFUSEwindow)

        QMetaObject.connectSlotsByName(primaryFUSEwindow)
    # setupUi

    def retranslateUi(self, primaryFUSEwindow):
        primaryFUSEwindow.setWindowTitle(QCoreApplication.translate("primaryFUSEwindow", u"MainWindow", None))
        self.actionReset_Default_Settings.setText(QCoreApplication.translate("primaryFUSEwindow", u"Reset Default Settings", None))
        self.advancedSettings_action.setText(QCoreApplication.translate("primaryFUSEwindow", u"Advanced", None))
        self.setup_action.setText(QCoreApplication.translate("primaryFUSEwindow", u"Setup", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("primaryFUSEwindow", u"About QT", None))
        self.actionAbout_CloudFuse.setText(QCoreApplication.translate("primaryFUSEwindow", u"About Cloudfuse", None))
        self.label.setText(QCoreApplication.translate("primaryFUSEwindow", u"Mount Point", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_mountPoint.setToolTip(QCoreApplication.translate("primaryFUSEwindow", u"<html><head/><body><p>Designate a location to mount the bucket</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_browse.setText(QCoreApplication.translate("primaryFUSEwindow", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.checkBox_remount.setToolTip(QCoreApplication.translate("primaryFUSEwindow", u"<html><head/><body><p>Remount mount on server restart. If checked, mount will automatically restart when system restarts. If unchecked, then when you unmount the mount it will not automatically restart.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_remount.setText(QCoreApplication.translate("primaryFUSEwindow", u"Remount on restart", None))
        self.label_4.setText(QCoreApplication.translate("primaryFUSEwindow", u"Mount Target", None))
        self.dropDown_bucketSelect.setItemText(0, QCoreApplication.translate("primaryFUSEwindow", u"S3", None))
        self.dropDown_bucketSelect.setItemText(1, QCoreApplication.translate("primaryFUSEwindow", u"Azure", None))

#if QT_CONFIG(tooltip)
        self.dropDown_bucketSelect.setToolTip(QCoreApplication.translate("primaryFUSEwindow", u"<html><head/><body><p>Choose which bucket to mount.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.dropDown_bucketSelect.setCurrentText(QCoreApplication.translate("primaryFUSEwindow", u"S3", None))
#if QT_CONFIG(tooltip)
        self.button_config.setToolTip(QCoreApplication.translate("primaryFUSEwindow", u"<html><head/><body><p>Click config to modify the pipeline settings associated with the selected bucket.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_config.setText(QCoreApplication.translate("primaryFUSEwindow", u"Config", None))
        self.button_mount.setText(QCoreApplication.translate("primaryFUSEwindow", u"Mount", None))
        self.button_unmount.setText(QCoreApplication.translate("primaryFUSEwindow", u"Unmount", None))
        self.menu_Help.setTitle(QCoreApplication.translate("primaryFUSEwindow", u"Help", None))
    # retranslateUi


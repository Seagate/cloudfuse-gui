# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'azure_config_common.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(993, 395)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_advancedSettings = QToolButton(Form)
        self.button_advancedSettings.setObjectName(u"button_advancedSettings")
        self.button_advancedSettings.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.button_advancedSettings, 5, 0, 1, 1)

        self.groupbox_fileCache = QGroupBox(Form)
        self.groupbox_fileCache.setObjectName(u"groupbox_fileCache")
        self.gridLayout_3 = QGridLayout(self.groupbox_fileCache)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fileCache_label = QLabel(self.groupbox_fileCache)
        self.fileCache_label.setObjectName(u"fileCache_label")

        self.horizontalLayout.addWidget(self.fileCache_label)

        self.lineEdit_fileCache_path = QLineEdit(self.groupbox_fileCache)
        self.lineEdit_fileCache_path.setObjectName(u"lineEdit_fileCache_path")

        self.horizontalLayout.addWidget(self.lineEdit_fileCache_path)

        self.button_browse = QPushButton(self.groupbox_fileCache)
        self.button_browse.setObjectName(u"button_browse")

        self.horizontalLayout.addWidget(self.button_browse)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupbox_fileCache, 1, 3, 1, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.spinBox_libfuse_attExp = QSpinBox(Form)
        self.spinBox_libfuse_attExp.setObjectName(u"spinBox_libfuse_attExp")
        self.spinBox_libfuse_attExp.setMaximum(2147483647)
        self.spinBox_libfuse_attExp.setValue(120)

        self.verticalLayout_2.addWidget(self.spinBox_libfuse_attExp)

        self.spinBox_libfuse_entExp = QSpinBox(Form)
        self.spinBox_libfuse_entExp.setObjectName(u"spinBox_libfuse_entExp")
        self.spinBox_libfuse_entExp.setMaximum(2147483647)
        self.spinBox_libfuse_entExp.setValue(120)

        self.verticalLayout_2.addWidget(self.spinBox_libfuse_entExp)

        self.spinBox_libfuse_negEntryExp = QSpinBox(Form)
        self.spinBox_libfuse_negEntryExp.setObjectName(u"spinBox_libfuse_negEntryExp")
        self.spinBox_libfuse_negEntryExp.setMaximum(2147483647)
        self.spinBox_libfuse_negEntryExp.setValue(120)

        self.verticalLayout_2.addWidget(self.spinBox_libfuse_negEntryExp)

        self.dropDown_libfuse_permissions = QComboBox(Form)
        self.dropDown_libfuse_permissions.addItem("")
        self.dropDown_libfuse_permissions.addItem("")
        self.dropDown_libfuse_permissions.addItem("")
        self.dropDown_libfuse_permissions.addItem("")
        self.dropDown_libfuse_permissions.setObjectName(u"dropDown_libfuse_permissions")

        self.verticalLayout_2.addWidget(self.dropDown_libfuse_permissions)

        self.dropDown_pipeline = QComboBox(Form)
        self.dropDown_pipeline.addItem("")
        self.dropDown_pipeline.addItem("")
        self.dropDown_pipeline.addItem("")
        self.dropDown_pipeline.setObjectName(u"dropDown_pipeline")

        self.verticalLayout_2.addWidget(self.dropDown_pipeline)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.groupbox_sasStorage = QGroupBox(Form)
        self.groupbox_sasStorage.setObjectName(u"groupbox_sasStorage")
        self.gridLayout_5 = QGridLayout(self.groupbox_sasStorage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_23 = QLabel(self.groupbox_sasStorage)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_13.addWidget(self.label_23)

        self.lineEdit_azure_sasStorage = QLineEdit(self.groupbox_sasStorage)
        self.lineEdit_azure_sasStorage.setObjectName(u"lineEdit_azure_sasStorage")
        self.lineEdit_azure_sasStorage.setEnabled(True)

        self.horizontalLayout_13.addWidget(self.lineEdit_azure_sasStorage)


        self.gridLayout_5.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupbox_sasStorage, 0, 3, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SetMinimumSize)
        self.checkBox_multiUser = QCheckBox(Form)
        self.checkBox_multiUser.setObjectName(u"checkBox_multiUser")
        self.checkBox_multiUser.setChecked(True)

        self.verticalLayout_10.addWidget(self.checkBox_multiUser)

        self.checkBox_nonEmptyDir = QCheckBox(Form)
        self.checkBox_nonEmptyDir.setObjectName(u"checkBox_nonEmptyDir")

        self.verticalLayout_10.addWidget(self.checkBox_nonEmptyDir)

        self.checkBox_readOnly = QCheckBox(Form)
        self.checkBox_readOnly.setObjectName(u"checkBox_readOnly")

        self.verticalLayout_10.addWidget(self.checkBox_readOnly)

        self.checkBox_daemonForeground = QCheckBox(Form)
        self.checkBox_daemonForeground.setObjectName(u"checkBox_daemonForeground")

        self.verticalLayout_10.addWidget(self.checkBox_daemonForeground)

        self.checkBox_libfuse_ignoreAppend = QCheckBox(Form)
        self.checkBox_libfuse_ignoreAppend.setObjectName(u"checkBox_libfuse_ignoreAppend")
        self.checkBox_libfuse_ignoreAppend.setChecked(True)

        self.verticalLayout_10.addWidget(self.checkBox_libfuse_ignoreAppend)


        self.gridLayout.addLayout(self.verticalLayout_10, 1, 2, 1, 1)

        self.groupbox_streaming = QGroupBox(Form)
        self.groupbox_streaming.setObjectName(u"groupbox_streaming")
        self.gridLayout_2 = QGridLayout(self.groupbox_streaming)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.fileLevelCaching_label = QLabel(self.groupbox_streaming)
        self.fileLevelCaching_label.setObjectName(u"fileLevelCaching_label")

        self.verticalLayout_4.addWidget(self.fileLevelCaching_label)

        self.blockSize_label = QLabel(self.groupbox_streaming)
        self.blockSize_label.setObjectName(u"blockSize_label")

        self.verticalLayout_4.addWidget(self.blockSize_label)

        self.maxBuffer_label = QLabel(self.groupbox_streaming)
        self.maxBuffer_label.setObjectName(u"maxBuffer_label")

        self.verticalLayout_4.addWidget(self.maxBuffer_label)

        self.bufferSize_label = QLabel(self.groupbox_streaming)
        self.bufferSize_label.setObjectName(u"bufferSize_label")

        self.verticalLayout_4.addWidget(self.bufferSize_label)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkBox_streaming_fileCachingLevel = QCheckBox(self.groupbox_streaming)
        self.checkBox_streaming_fileCachingLevel.setObjectName(u"checkBox_streaming_fileCachingLevel")

        self.verticalLayout_5.addWidget(self.checkBox_streaming_fileCachingLevel)

        self.spinBox_streaming_blockSize = QSpinBox(self.groupbox_streaming)
        self.spinBox_streaming_blockSize.setObjectName(u"spinBox_streaming_blockSize")
        self.spinBox_streaming_blockSize.setMaximum(2147483647)

        self.verticalLayout_5.addWidget(self.spinBox_streaming_blockSize)

        self.spinBox_streaming_maxBuff = QSpinBox(self.groupbox_streaming)
        self.spinBox_streaming_maxBuff.setObjectName(u"spinBox_streaming_maxBuff")
        self.spinBox_streaming_maxBuff.setMaximum(2147483647)

        self.verticalLayout_5.addWidget(self.spinBox_streaming_maxBuff)

        self.spinBox_streaming_buffSize = QSpinBox(self.groupbox_streaming)
        self.spinBox_streaming_buffSize.setObjectName(u"spinBox_streaming_buffSize")
        self.spinBox_streaming_buffSize.setMaximum(2147483647)

        self.verticalLayout_5.addWidget(self.spinBox_streaming_buffSize)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupbox_streaming, 1, 3, 1, 2)

        self.groupbox_accountKey = QGroupBox(Form)
        self.groupbox_accountKey.setObjectName(u"groupbox_accountKey")
        self.gridLayout_4 = QGridLayout(self.groupbox_accountKey)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_22 = QLabel(self.groupbox_accountKey)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_12.addWidget(self.label_22)

        self.lineEdit_azure_accountKey = QLineEdit(self.groupbox_accountKey)
        self.lineEdit_azure_accountKey.setObjectName(u"lineEdit_azure_accountKey")

        self.horizontalLayout_12.addWidget(self.lineEdit_azure_accountKey)


        self.gridLayout_4.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupbox_accountKey, 0, 3, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_3.addWidget(self.label_12)

        self.label_20 = QLabel(Form)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_3.addWidget(self.label_20)

        self.label_21 = QLabel(Form)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_3.addWidget(self.label_21)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.dropDown_azure_storageType = QComboBox(Form)
        self.dropDown_azure_storageType.addItem("")
        self.dropDown_azure_storageType.addItem("")
        self.dropDown_azure_storageType.setObjectName(u"dropDown_azure_storageType")

        self.verticalLayout_6.addWidget(self.dropDown_azure_storageType)

        self.lineEdit_azure_accountName = QLineEdit(Form)
        self.lineEdit_azure_accountName.setObjectName(u"lineEdit_azure_accountName")

        self.verticalLayout_6.addWidget(self.lineEdit_azure_accountName)

        self.lineEdit_azure_container = QLineEdit(Form)
        self.lineEdit_azure_container.setObjectName(u"lineEdit_azure_container")

        self.verticalLayout_6.addWidget(self.lineEdit_azure_container)

        self.lineEdit_azure_endpoint = QLineEdit(Form)
        self.lineEdit_azure_endpoint.setObjectName(u"lineEdit_azure_endpoint")

        self.verticalLayout_6.addWidget(self.lineEdit_azure_endpoint)

        self.dropDown_azure_modeSetting = QComboBox(Form)
        self.dropDown_azure_modeSetting.addItem("")
        self.dropDown_azure_modeSetting.addItem("")
        self.dropDown_azure_modeSetting.addItem("")
        self.dropDown_azure_modeSetting.addItem("")
        self.dropDown_azure_modeSetting.setObjectName(u"dropDown_azure_modeSetting")

        self.verticalLayout_6.addWidget(self.dropDown_azure_modeSetting)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 3)

        self.groupbox_msi = QGroupBox(Form)
        self.groupbox_msi.setObjectName(u"groupbox_msi")
        self.gridLayout_7 = QGridLayout(self.groupbox_msi)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_24 = QLabel(self.groupbox_msi)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_14.addWidget(self.label_24)

        self.lineEdit_azure_msiAppID = QLineEdit(self.groupbox_msi)
        self.lineEdit_azure_msiAppID.setObjectName(u"lineEdit_azure_msiAppID")
        self.lineEdit_azure_msiAppID.setEnabled(True)

        self.horizontalLayout_14.addWidget(self.lineEdit_azure_msiAppID)


        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_25 = QLabel(self.groupbox_msi)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_15.addWidget(self.label_25)

        self.lineEdit_azure_msiResourceID = QLineEdit(self.groupbox_msi)
        self.lineEdit_azure_msiResourceID.setObjectName(u"lineEdit_azure_msiResourceID")
        self.lineEdit_azure_msiResourceID.setEnabled(True)

        self.horizontalLayout_15.addWidget(self.lineEdit_azure_msiResourceID)


        self.verticalLayout_12.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_26 = QLabel(self.groupbox_msi)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_16.addWidget(self.label_26)

        self.lineEdit_azure_msiObjectID = QLineEdit(self.groupbox_msi)
        self.lineEdit_azure_msiObjectID.setObjectName(u"lineEdit_azure_msiObjectID")
        self.lineEdit_azure_msiObjectID.setEnabled(True)

        self.horizontalLayout_16.addWidget(self.lineEdit_azure_msiObjectID)


        self.verticalLayout_12.addLayout(self.horizontalLayout_16)


        self.gridLayout_7.addLayout(self.verticalLayout_12, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupbox_msi, 0, 3, 1, 1)

        self.groupbox_spn = QGroupBox(Form)
        self.groupbox_spn.setObjectName(u"groupbox_spn")
        self.gridLayout_6 = QGridLayout(self.groupbox_spn)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_27 = QLabel(self.groupbox_spn)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_17.addWidget(self.label_27)

        self.lineEdit_azure_spnTenantID = QLineEdit(self.groupbox_spn)
        self.lineEdit_azure_spnTenantID.setObjectName(u"lineEdit_azure_spnTenantID")
        self.lineEdit_azure_spnTenantID.setEnabled(True)

        self.horizontalLayout_17.addWidget(self.lineEdit_azure_spnTenantID)


        self.verticalLayout_13.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_28 = QLabel(self.groupbox_spn)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_18.addWidget(self.label_28)

        self.lineEdit_azure_spnClientID = QLineEdit(self.groupbox_spn)
        self.lineEdit_azure_spnClientID.setObjectName(u"lineEdit_azure_spnClientID")
        self.lineEdit_azure_spnClientID.setEnabled(True)

        self.horizontalLayout_18.addWidget(self.lineEdit_azure_spnClientID)


        self.verticalLayout_13.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_29 = QLabel(self.groupbox_spn)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_19.addWidget(self.label_29)

        self.lineEdit_azure_spnClientSecret = QLineEdit(self.groupbox_spn)
        self.lineEdit_azure_spnClientSecret.setObjectName(u"lineEdit_azure_spnClientSecret")
        self.lineEdit_azure_spnClientSecret.setEnabled(True)

        self.horizontalLayout_19.addWidget(self.lineEdit_azure_spnClientSecret)


        self.verticalLayout_13.addLayout(self.horizontalLayout_19)


        self.gridLayout_6.addLayout(self.verticalLayout_13, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupbox_spn, 0, 3, 1, 1)

        self.button_okay = QPushButton(Form)
        self.button_okay.setObjectName(u"button_okay")
        self.button_okay.setMaximumSize(QSize(100, 16777215))
        self.button_okay.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.button_okay, 5, 3, 1, 1)

        self.button_resetDefaultSettings = QPushButton(Form)
        self.button_resetDefaultSettings.setObjectName(u"button_resetDefaultSettings")
        self.button_resetDefaultSettings.setEnabled(True)
        self.button_resetDefaultSettings.setMaximumSize(QSize(165, 16777215))
        self.button_resetDefaultSettings.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.button_resetDefaultSettings, 3, 0, 1, 1)


        self.retranslateUi(Form)

        self.button_resetDefaultSettings.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button_advancedSettings.setText(QCoreApplication.translate("Form", u"Advanced settings", None))
        self.groupbox_fileCache.setTitle("")
#if QT_CONFIG(tooltip)
        self.fileCache_label.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The path to the local disk cache - the directory must already exist</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fileCache_label.setText(QCoreApplication.translate("Form", u"File cache path", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_fileCache_path.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The path to the local disk cache - the directory must already exist</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.button_browse.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Browse to a directory for the file cache to be stored - choose a pre-existing directory.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_browse.setText(QCoreApplication.translate("Form", u"Browse", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The amount of time (seconds) the kernel can cache inode attributes</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Form", u"Attribute expiration (s)", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The amount of time (seconds) the kernel can cache directory listings attributes</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Form", u"Entry expiration (s)", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The amount of time (seconds) the kernel can cache attributes for non-existent paths</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Form", u"Negative entry exp (s)", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Default permissions to be presented - full read/write permissions, read only, etc</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"Permissions", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Set the pipeline mode for CloudFuse</p><p>Choose either File caching or Streaming</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"Mode", None))
        self.dropDown_libfuse_permissions.setItemText(0, QCoreApplication.translate("Form", u"0777", None))
        self.dropDown_libfuse_permissions.setItemText(1, QCoreApplication.translate("Form", u"0666", None))
        self.dropDown_libfuse_permissions.setItemText(2, QCoreApplication.translate("Form", u"0644", None))
        self.dropDown_libfuse_permissions.setItemText(3, QCoreApplication.translate("Form", u"0444", None))

        self.dropDown_pipeline.setItemText(0, QCoreApplication.translate("Form", u"File Caching", None))
        self.dropDown_pipeline.setItemText(1, QCoreApplication.translate("Form", u"Streaming", None))
        self.dropDown_pipeline.setItemText(2, QCoreApplication.translate("Form", u"Block Cache", None))

        self.groupbox_sasStorage.setTitle("")
#if QT_CONFIG(tooltip)
        self.label_23.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Provide the SAS auth key</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_23.setText(QCoreApplication.translate("Form", u"Sas storage", None))
#if QT_CONFIG(tooltip)
        self.checkBox_multiUser.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Allow other users to access the mounted directory - used for FUSE and File Cache</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_multiUser.setText(QCoreApplication.translate("Form", u"Multiple Users", None))
#if QT_CONFIG(tooltip)
        self.checkBox_nonEmptyDir.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Allow mounting on non-empty directory - used for FUSE</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_nonEmptyDir.setText(QCoreApplication.translate("Form", u"Non-empty directory mount", None))
#if QT_CONFIG(tooltip)
        self.checkBox_readOnly.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Mount in read only mode - used for Streaming and FUSE</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_readOnly.setText(QCoreApplication.translate("Form", u"Read-only mount", None))
#if QT_CONFIG(tooltip)
        self.checkBox_daemonForeground.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Run CloudFuse in the foreground of background. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_daemonForeground.setText(QCoreApplication.translate("Form", u"Run in foreground", None))
#if QT_CONFIG(tooltip)
        self.checkBox_libfuse_ignoreAppend.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Ignore the append and write only flag since append and write only is not supported with writeback caching. Alternatively, disable the write-back cache in advanced settings.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_libfuse_ignoreAppend.setText(QCoreApplication.translate("Form", u"Ignore append/write only flags", None))
        self.groupbox_streaming.setTitle("")
#if QT_CONFIG(tooltip)
        self.fileLevelCaching_label.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Read/Write mode for file level caching or handle level caching. False means handle level caching is ON</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.fileLevelCaching_label.setText(QCoreApplication.translate("Form", u"File level caching", None))
#if QT_CONFIG(tooltip)
        self.blockSize_label.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The size (MB) of each block to be cached in memory while read-only mode streaming </p><p><span style=\" text-decoration: underline;\">OR</span></p><p>The the size (MB) for newly created blocks in read/write mode</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.blockSize_label.setText(QCoreApplication.translate("Form", u"Block size (MB)", None))
#if QT_CONFIG(tooltip)
        self.maxBuffer_label.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The total number of buffers to store blocks in</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.maxBuffer_label.setText(QCoreApplication.translate("Form", u"Max buffer (MB)", None))
#if QT_CONFIG(tooltip)
        self.bufferSize_label.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The size (MB) of each buffer</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bufferSize_label.setText(QCoreApplication.translate("Form", u"Buffer size (MB)", None))
        self.checkBox_streaming_fileCachingLevel.setText("")
        self.groupbox_accountKey.setTitle("")
#if QT_CONFIG(tooltip)
        self.label_22.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Secret key</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_22.setText(QCoreApplication.translate("Form", u"Account key", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The type of storage account to be connected - block or adls</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("Form", u"Storage Type", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Name of the storage account</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("Form", u"Account name", None))
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The name of the storage container to be mounted</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("Form", u"Container", None))
#if QT_CONFIG(tooltip)
        self.label_20.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The storage account endpoint - example: https://account-name.blob.core.windows.net</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("Form", u"Endpoint", None))
#if QT_CONFIG(tooltip)
        self.label_21.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>The authentication mode- </p><p>KEY - secret key</p><p>SAS -  provide the SAS auth key</p><p>SPN -  provide storage account tenant id, client id, and client secret key</p><p>MSI -  provide appID/client ID, storage account Id, and the object ID</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_21.setText(QCoreApplication.translate("Form", u"Mode", None))
        self.dropDown_azure_storageType.setItemText(0, QCoreApplication.translate("Form", u"block", None))
        self.dropDown_azure_storageType.setItemText(1, QCoreApplication.translate("Form", u"adls", None))

        self.dropDown_azure_modeSetting.setItemText(0, QCoreApplication.translate("Form", u"key", None))
        self.dropDown_azure_modeSetting.setItemText(1, QCoreApplication.translate("Form", u"sas", None))
        self.dropDown_azure_modeSetting.setItemText(2, QCoreApplication.translate("Form", u"spn", None))
        self.dropDown_azure_modeSetting.setItemText(3, QCoreApplication.translate("Form", u"msi", None))

        self.groupbox_msi.setTitle("")
#if QT_CONFIG(tooltip)
        self.label_24.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Provide app ID/client ID</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_24.setText(QCoreApplication.translate("Form", u"App ID", None))
#if QT_CONFIG(tooltip)
        self.label_25.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Provide storage account Id</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_25.setText(QCoreApplication.translate("Form", u"Resource ID", None))
        self.lineEdit_azure_msiResourceID.setText("")
#if QT_CONFIG(tooltip)
        self.label_26.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Provide the object ID</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_26.setText(QCoreApplication.translate("Form", u"Object ID", None))
        self.lineEdit_azure_msiObjectID.setText("")
        self.groupbox_spn.setTitle("")
#if QT_CONFIG(tooltip)
        self.label_27.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Provide storage account tenant id</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_27.setText(QCoreApplication.translate("Form", u"Tenant ID", None))
#if QT_CONFIG(tooltip)
        self.label_28.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Provide storage account client ID</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_28.setText(QCoreApplication.translate("Form", u"Client ID", None))
        self.lineEdit_azure_spnClientID.setText("")
#if QT_CONFIG(tooltip)
        self.label_29.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Provide storage account client secret key</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_29.setText(QCoreApplication.translate("Form", u"Client Secret", None))
        self.lineEdit_azure_spnClientSecret.setText("")
        self.button_okay.setText(QCoreApplication.translate("Form", u"Save", None))
#if QT_CONFIG(tooltip)
        self.button_resetDefaultSettings.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Set all the settings to the pre-programmed defaults, INCLUDING advanced options. The changes will not be made permanent unless they are saved. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.button_resetDefaultSettings.setText(QCoreApplication.translate("Form", u"Reset Default Settings", None))
    # retranslateUi


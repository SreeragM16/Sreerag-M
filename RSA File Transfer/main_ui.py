from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 716)
        MainWindow.setMinimumSize(QtCore.QSize(708, 485))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.pubkey_textedit = QtWidgets.QPlainTextEdit(self.tab)
        self.pubkey_textedit.setMaximumSize(QtCore.QSize(16777215, 538))
        self.pubkey_textedit.setObjectName("pubkey_textedit")
        self.verticalLayout_2.addWidget(self.pubkey_textedit)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filepath_ledit = QtWidgets.QLineEdit(self.tab)
        self.filepath_ledit.setMaximumSize(QtCore.QSize(16777214, 16777214))
        self.filepath_ledit.setObjectName("filepath_ledit")
        self.horizontalLayout.addWidget(self.filepath_ledit)
        self.browse_btn = QtWidgets.QPushButton(self.tab)
        self.browse_btn.setMaximumSize(QtCore.QSize(16777213, 16777214))
        self.browse_btn.setObjectName("browse_btn")
        self.horizontalLayout.addWidget(self.browse_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.encrypt_btn = QtWidgets.QPushButton(self.tab)
        self.encrypt_btn.setMaximumSize(QtCore.QSize(16777210, 16777211))
        self.encrypt_btn.setObjectName("encrypt_btn")
        self.horizontalLayout_3.addWidget(self.encrypt_btn)
        self.serve_btn = QtWidgets.QPushButton(self.tab)
        self.serve_btn.setMaximumSize(QtCore.QSize(16777214, 16777214))
        self.serve_btn.setObjectName("serve_btn")
        self.horizontalLayout_3.addWidget(self.serve_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.privkey_textedit_tab2 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.privkey_textedit_tab2.setMaximumSize(QtCore.QSize(16777215, 538))
        self.privkey_textedit_tab2.setObjectName("privkey_textedit_tab2")
        self.verticalLayout_3.addWidget(self.privkey_textedit_tab2)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filepath_ledit_tab2 = QtWidgets.QLineEdit(self.tab_2)
        self.filepath_ledit_tab2.setMaximumSize(QtCore.QSize(16777214, 16777214))
        self.filepath_ledit_tab2.setObjectName("filepath_ledit_tab2")
        self.horizontalLayout_2.addWidget(self.filepath_ledit_tab2)
        self.browse_btn_tab2 = QtWidgets.QPushButton(self.tab_2)
        self.browse_btn_tab2.setObjectName("browse_btn_tab2")
        self.horizontalLayout_2.addWidget(self.browse_btn_tab2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.decrypt_btn_tab2 = QtWidgets.QPushButton(self.tab_2)
        self.decrypt_btn_tab2.setMaximumSize(QtCore.QSize(16777214, 16777214))
        self.decrypt_btn_tab2.setObjectName("decrypt_btn_tab2")
        self.verticalLayout_3.addWidget(self.decrypt_btn_tab2)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter Public Key:"))
        self.label_2.setText(_translate("MainWindow", "Browse File:"))
        self.browse_btn.setText(_translate("MainWindow", "Browse"))
        self.encrypt_btn.setText(_translate("MainWindow", "Encrypt"))
        self.serve_btn.setText(_translate("MainWindow", "Serve on Tor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Send"))
        self.label_3.setText(_translate("MainWindow", "Enter Private Key:"))
        self.label_4.setText(_translate("MainWindow", "Browse File:"))
        self.browse_btn_tab2.setText(_translate("MainWindow", "Browse"))
        self.decrypt_btn_tab2.setText(_translate("MainWindow", "Decrypt"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Receive"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



from PyQt5 import QtCore, QtGui, QtWidgets
import sys, base64
import PasswordManager

STYLE_SHEET = """
QWidget { background: #FFFFFF; font-family: 'Segoe UI', sans-serif; font-size: 10pt; color: #333; }
QTabWidget::pane { border: 1px solid #D1D1D1; border-radius: 4px; }
QTabBar::tab { background: #F0F0F0; padding: 12px 20px; margin-right: 2px; border-top-left-radius: 4px; border-top-right-radius: 4px; }
QTabBar::tab:selected { background: white; color: #2980b9; border-bottom: 2px solid #2980b9; }

QLineEdit, QTextEdit { border: 2px solid #E0E0E0; border-radius: 8px; padding: 6px; background: white; }
QLineEdit:focus, QTextEdit:focus { border: 2px solid #2980b9; }

QComboBox { border: 2px solid #E0E0E0; border-radius: 8px; padding: 5px 10px; background: white; min-width: 80px; }
QComboBox:focus { border: 2px solid #2980b9; }
QComboBox::drop-down { border: none; width: 30px; }
QComboBox::down-arrow { border-left: 5px solid transparent; border-right: 5px solid transparent; border-top: 5px solid #2980b9; margin-right: 10px; }

QPushButton { background-color: #2980b9; color: white; border-radius: 8px; padding: 10px; min-width: 80px; border: none; }
QPushButton:hover { background-color: #3498db; }
QPushButton:pressed { background-color: #1f6391; }

QSlider::groove:horizontal { height: 6px; background: #EEE; border-radius: 3px; }
QSlider::handle:horizontal { background: #2980b9; width: 18px; height: 18px; margin: -6px 0; border-radius: 9px; }
QSlider::sub-page:horizontal { background: #2980b9; border-radius: 3px; }

QCheckBox::indicator { width: 18px; height: 18px; border-radius: 9px; border: 2px solid #C5C5C5; }
QCheckBox::indicator:checked { background-color: #2980b9; border: 2px solid #2980b9; }
"""

class SecureBox(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(520, 600)
        self.setWindowTitle("SecureBox v1.0")
        self.setStyleSheet(STYLE_SHEET)

        self.current_private_key = None
        self.current_public_key = None

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.tab_widget = QtWidgets.QTabWidget()
        
        self.init_password_gen_tab()
        self.init_base64_tab()
        self.init_rsa_tab()

        self.main_layout.addWidget(self.tab_widget)

    def init_password_gen_tab(self):
        self.pass_tab = QtWidgets.QWidget()
        layout = QtWidgets.QFormLayout(self.pass_tab)
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(18)

        self.output_line = QtWidgets.QLineEdit()
        self.output_line.setFixedHeight(45)
        self.output_line.setPlaceholderText("Click Generate...")
        self.output_line.setReadOnly(True)
        
        copy_action = self.output_line.addAction(
            self.style().standardIcon(QtWidgets.QStyle.SP_DialogSaveButton),
            QtWidgets.QLineEdit.TrailingPosition
        )
        copy_action.triggered.connect(self.copy_to_clipboard)
        layout.addRow(self.output_line)

        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setRange(8, 64); self.slider.setValue(16)
        self.lbl_val = QtWidgets.QLabel("16")
        self.lbl_val.setStyleSheet("color: #2980b9; font-size: 12pt;")
        
        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addWidget(self.slider); h_layout.addWidget(self.lbl_val)
        layout.addRow("Length:", h_layout)
        self.slider.valueChanged.connect(lambda v: self.lbl_val.setText(str(v)))

        self.cb_low = QtWidgets.QCheckBox("Lowercase"); self.cb_up = QtWidgets.QCheckBox("Uppercase")
        self.cb_num = QtWidgets.QCheckBox("Numbers"); self.cb_sym = QtWidgets.QCheckBox("Symbols")
        for cb in [self.cb_low, self.cb_up, self.cb_num, self.cb_sym]: cb.setChecked(True)

        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.cb_low, 0, 0); grid.addWidget(self.cb_up, 0, 1)
        grid.addWidget(self.cb_num, 1, 0); grid.addWidget(self.cb_sym, 1, 1)
        layout.addRow("Options:", grid)

        self.gen_btn = QtWidgets.QPushButton("GENERATE PASSWORD")
        self.gen_btn.setFixedHeight(45)
        self.gen_btn.clicked.connect(self.generate_pass)
        layout.addRow(self.gen_btn)
        self.tab_widget.addTab(self.pass_tab, "Password")

    def init_base64_tab(self):
        self.b64_tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(self.b64_tab)
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(5)

        layout.addWidget(QtWidgets.QLabel("Input Plain Text:"))
        self.txt_plain = QtWidgets.QTextEdit()
        self.txt_plain.setFixedHeight(120) 
        layout.addWidget(self.txt_plain)

        layout.addSpacing(10)
        btn_layout = QtWidgets.QHBoxLayout()
        self.btn_encode = QtWidgets.QPushButton("Encode")
        self.btn_decode = QtWidgets.QPushButton("Decode")
        self.btn_encode.setFixedHeight(40)
        self.btn_decode.setFixedHeight(40)
        self.btn_encode.clicked.connect(self.handle_b64_encode)
        self.btn_decode.clicked.connect(self.handle_b64_decode)
        btn_layout.addWidget(self.btn_encode)
        btn_layout.addWidget(self.btn_decode)
        layout.addLayout(btn_layout)
        layout.addSpacing(10)

        layout.addWidget(QtWidgets.QLabel("Base64 Output:"))
        self.txt_b64 = QtWidgets.QTextEdit()
        self.txt_b64.setFixedHeight(120) 
        layout.addWidget(self.txt_b64)
        
        layout.addStretch(1) 
        
        self.tab_widget.addTab(self.b64_tab, "Base64 Tool")

    def init_rsa_tab(self):
        self.rsa_tab = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(self.rsa_tab)
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(15)

        top_group = QtWidgets.QHBoxLayout()
        self.combo_rsa_size = QtWidgets.QComboBox()
        self.combo_rsa_size.addItems(["1024", "2048", "4096"])
        self.combo_rsa_size.setCurrentText("2048")
        self.combo_rsa_size.setFixedHeight(35)
        
        self.btn_gen_rsa = QtWidgets.QPushButton("Generate Keys")
        self.btn_gen_rsa.setFixedHeight(35)
        self.btn_gen_rsa.clicked.connect(self.handle_rsa_gen)
        
        top_group.addWidget(QtWidgets.QLabel("Bits:"))
        top_group.addWidget(self.combo_rsa_size)
        top_group.addWidget(self.btn_gen_rsa)
        top_group.setStretch(2, 1)
        layout.addLayout(top_group)

        file_group = QtWidgets.QHBoxLayout()
        self.btn_save = QtWidgets.QPushButton("Save to Disk")
        self.btn_load = QtWidgets.QPushButton("Load from Disk")
        self.btn_save.setFixedHeight(35)
        self.btn_load.setFixedHeight(35)
        self.btn_save.setStyleSheet("background-color: #27ae60;")
        self.btn_load.setStyleSheet("background-color: #f39c12;")
        self.btn_save.clicked.connect(self.handle_rsa_save)
        self.btn_load.clicked.connect(self.handle_rsa_load)
        file_group.addWidget(self.btn_save); file_group.addWidget(self.btn_load)
        layout.addLayout(file_group)

        layout.addWidget(QtWidgets.QLabel("Data (Message or Cipher):"))
        self.txt_rsa_data = QtWidgets.QTextEdit()
        layout.addWidget(self.txt_rsa_data)

        action_group = QtWidgets.QHBoxLayout()
        self.btn_encrypt = QtWidgets.QPushButton("Encrypt Data")
        self.btn_decrypt = QtWidgets.QPushButton("Decrypt Data")
        self.btn_encrypt.setFixedHeight(40)
        self.btn_decrypt.setFixedHeight(40)
        self.btn_encrypt.clicked.connect(self.handle_rsa_encrypt)
        self.btn_decrypt.clicked.connect(self.handle_rsa_decrypt)
        action_group.addWidget(self.btn_encrypt); action_group.addWidget(self.btn_decrypt)
        layout.addLayout(action_group)

        self.tab_widget.addTab(self.rsa_tab, "RSA")

    def copy_to_clipboard(self):
        text = self.output_line.text()
        if text:
            QtWidgets.QApplication.clipboard().setText(text)
            QtWidgets.QToolTip.showText(QtGui.QCursor.pos(), "Copied!", self)

    def generate_pass(self):
        pwd = PasswordManager.create_random_password(
            self.cb_num.isChecked(), self.cb_sym.isChecked(),
            self.cb_up.isChecked(), self.cb_low.isChecked(),
            self.slider.value()
        )
        self.output_line.setText(pwd)

    def handle_b64_encode(self):
        res = PasswordManager.encode_base64(self.txt_plain.toPlainText())
        self.txt_b64.setPlainText(res)

    def handle_b64_decode(self):
        try:
            res = PasswordManager.decode_base64(self.txt_b64.toPlainText())
            self.txt_plain.setPlainText(res)
        except: self.txt_plain.setPlainText("Invalid Base64!")

    def handle_rsa_gen(self):
        size = int(self.combo_rsa_size.currentText())
        self.current_private_key, self.current_public_key = PasswordManager.generate_rsa_keys(size)
        QtWidgets.QMessageBox.information(self, "Success", f"RSA-{size} keys loaded to memory.")

    def handle_rsa_save(self):
        if self.current_private_key:
            PasswordManager.save_rsa_to_disk(self.current_private_key, self.current_public_key)
            QtWidgets.QMessageBox.information(self, "Success", "Keys stored in Data/RSA/")
        else: QtWidgets.QMessageBox.warning(self, "Error", "No keys in memory!")

    def handle_rsa_load(self):
        priv, pub = PasswordManager.load_rsa_from_disk()
        if priv:
            self.current_private_key, self.current_public_key = priv, pub
            QtWidgets.QMessageBox.information(self, "Success", "Keys loaded from Data/RSA/")
        else: QtWidgets.QMessageBox.critical(self, "Error", "Files not found!")

    def handle_rsa_encrypt(self):
        if not self.current_public_key: return
        msg = self.txt_rsa_data.toPlainText()
        if len(msg.encode('utf-8')) > 190:
            QtWidgets.QMessageBox.warning(self, "Limit", "Message too long for RSA!")
            return
        res = PasswordManager.rsa_encrypt(msg, self.current_public_key)
        self.txt_rsa_data.setPlainText(res)

    def handle_rsa_decrypt(self):
        if not self.current_private_key: return
        try:
            res = PasswordManager.rsa_decrypt(self.txt_rsa_data.toPlainText(), self.current_private_key)
            self.txt_rsa_data.setPlainText(res)
        except: QtWidgets.QMessageBox.critical(self, "Error", "Decryption failed!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SecureBox()
    window.show()
    sys.exit(app.exec_())
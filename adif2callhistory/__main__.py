#!/usr/bin/env python3
import os
import sys

# import fsutils as fsutils

from pathlib import Path

from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QFileDialog

from adif_file import adi

WORKING_PATH = Path(os.path.dirname(os.path.abspath(__file__)))


class MainWindow(QtWidgets.QMainWindow):
    """
    Main Window
    """

    history_fields = [
        "Call",
        "Name",
        "Loc1",
        "Loc2",
        "Sect",
        "State",
        "CK",
        "BirthDate",
        "Exch1",
        "Misc",
        "Power",
        "CqZone",
        "ITUZone",
        "UserText",
    ]
    theset = set()
    adi_doc = None

    def __init__(self):
        super().__init__()
        uic.loadUi(WORKING_PATH / "main.ui", self)

        self.actionQuit.triggered.connect(self.quit_app)
        self.actionLoad_ADIF.triggered.connect(self.load_adif)
        self.actionSave_Call_History.triggered.connect(self.save_call_history)

        self.combolist = [
            self.call_comboBox,
            self.name_comboBox,
            self.loc1_comboBox,
            self.loc2_comboBox,
            self.sect_comboBox,
            self.state_comboBox,
            self.ck_comboBox,
            self.birthdate_comboBox,
            self.exch1_comboBox,
            self.misc_comboBox,
            self.power_comboBox,
            self.cqzone_comboBox,
            self.ituzone_comboBox,
            self.usertext_comboBox,
        ]

        self.name2checkbox = {
            "Call": [self.call_checkBox, self.call_comboBox],
            "Name": [self.name_checkBox, self.name_comboBox],
            "Loc1": [self.loc1_checkBox, self.loc1_comboBox],
            "Loc2": [self.loc2_checkBox, self.loc2_comboBox],
            "Sect": [self.sect_checkBox, self.sect_comboBox],
            "State": [self.state_checkBox, self.state_comboBox],
            "CK": [self.ck_checkBox, self.ck_comboBox],
            "BirthDate": [self.birthdate_checkBox, self.birthdate_comboBox],
            "Exch1": [self.exch1_checkBox, self.exch1_comboBox],
            "Misc": [self.misc_checkBox, self.misc_comboBox],
            "Power": [self.power_checkBox, self.power_comboBox],
            "CqZone": [self.cqzone_checkBox, self.cqzone_comboBox],
            "ITUZone": [self.ituzone_checkBox, self.ituzone_comboBox],
            "UserText": [self.usertext_checkBox, self.usertext_comboBox],
        }

    def quit_app(self) -> None:
        """
        Send multicast quit message, then quit the program.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        app.quit()

    def filepicker(self, action: str) -> str:
        """
        Get a filename

        Parameters:
        ----------
        action: 'new' or 'open'

        Returns:
        -------
        str: filename
        """

        options = (
            QFileDialog.Option.DontUseNativeDialog
            | QFileDialog.Option.DontConfirmOverwrite
        )
        if action == "new":
            file, _ = QFileDialog.getSaveFileName(
                self,
                "Choose a File",
                "~/",
                "Textfile (*.txt)",
                options=options,
            )
        if action == "open":
            file, _ = QFileDialog.getOpenFileName(
                self,
                "Choose an ADIF file",
                "~/",
                "ADIF (*.adi)",
                options=options,
            )
        if action == "other":
            file, _ = QFileDialog.getOpenFileName(
                self,
                "Choose a File",
                "~/",
                "ADIF (*.adi) ;; Any (*.*)",
                options=options,
            )
        return file

    def load_adif(self) -> None:
        """
        Create new database file.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        filename = self.filepicker("other")
        if filename:
            self.theset = set()
            try:
                self.adi_doc = adi.load(filename)
                for rec in self.adi_doc["RECORDS"]:
                    the_keys = rec.keys()
                    self.theset.update(the_keys)
            except IndexError:
                ...

        thelist = list(self.theset)
        thelist.sort()

        for dropdown in self.combolist:
            dropdown.clear()
            dropdown.addItems(thelist)

    def save_call_history(self) -> None:
        """..."""
        filename = self.filepicker("new")
        if filename and self.adi_doc:
            with open(filename, "w", encoding="utf-8") as file_descriptor:
                header = "!!Order!!"
                checkedboxes = []
                for cb in self.name2checkbox:
                    if self.name2checkbox[cb][0].isChecked():
                        header += f",{cb}"
                        checkedboxes.append(cb)
                print(header, end="\r\n", file=file_descriptor)
                for rec in self.adi_doc["RECORDS"]:
                    line = ""
                    first = True
                    for checked in checkedboxes:
                        if first:
                            first = False
                            line += f"{rec.get(self.name2checkbox[checked][1].currentText(),'')}"
                        else:
                            line += f",{rec.get(self.name2checkbox[checked][1].currentText(),'')}"
                    print(line, end="\r\n", file=file_descriptor)


def run() -> None:
    """
    Main Entry
    """
    QCoreApplication.processEvents()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


app = QtWidgets.QApplication(sys.argv)

if __name__ == "__main__":
    run()

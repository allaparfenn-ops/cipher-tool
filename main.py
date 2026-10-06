"""Точка входа: создаём приложение и загружаем окно из QML."""

import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuickControls2 import QQuickStyle

from backend import Backend


def main():
    app = QGuiApplication(sys.argv)
    # Один стандартный стиль на всех ОС, без собственной системы оформления.
    QQuickStyle.setStyle("Fusion")
    engine = QQmlApplicationEngine()

    # Сохраняем объект в переменной на всё время работы приложения.
    # В QML он будет доступен под именем backend.
    backend = Backend()
    engine.rootContext().setContextProperty("backend", backend)

    # Путь относительно этого файла позволяет запускать программу
    # даже из другой рабочей папки.
    qml_file = Path(__file__).parent / "qml" / "Main.qml"
    engine.load(QUrl.fromLocalFile(str(qml_file.resolve())))
    if not engine.rootObjects():
        return 1

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())

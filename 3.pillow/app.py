import sys
from itertools import product
from random import choices, random

from PIL import Image, ImageFilter, ImageOps
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QLabel,
    QMainWindow,
    QMenu,
    QMenuBar,
    QVBoxLayout,
    QWidget,
)


class ImageTransformer:
    @staticmethod
    def rotate(image: Image.Image | None) -> Image.Image | None:
        if image:
            return image.rotate(-90)
        return None

    @staticmethod
    def flip(image: Image.Image | None) -> Image.Image | None:
        if image:
            return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        return None

    @staticmethod
    def thumbnail(
        image: Image.Image | None,
        size: tuple[int, int] = (256, 256),
        resample: int = Image.BICUBIC,
    ) -> Image.Image | None:
        if image:
            image.thumbnail(size, resample=resample)
            return image
        return None

    @staticmethod
    def invert_color(image: Image.Image | None) -> Image.Image | None:
        if image:
            return ImageOps.invert(image)
        return None

    @staticmethod
    def colorize(
        image: Image.Image | None,
        black: str = "blue",
        white: str = "yellow",
    ) -> Image.Image | None:
        if image:
            gray_image = image.convert("L")
            return ImageOps.colorize(gray_image, black, white)
        return None

    @staticmethod
    def salt_and_pepper_noise(image: Image.Image | None) -> Image.Image | None:
        if image:
            w, h = range(image.width), range(image.height)
            it = tuple(product(w, h))
            pixels = image.load()
            for x, y in choices(it, k=len(it) // 2):
                r = random()
                if r < 0.01:
                    pixels[x, y] = (0, 0, 0)
                elif r < 0.02:
                    pixels[x, y] = (255, 255, 255)
            return image
        return None

    @staticmethod
    def sobel(
        image: Image.Image | None,
    ) -> Image.Image | None:
        if image:
            return image.filter(ImageFilter.FIND_EDGES)
        return None

    @staticmethod
    def gaussian_blur(
        image: Image.Image | None,
        radius: int = 2,
    ):
        if image:
            return image.filter(ImageFilter.GaussianBlur(radius=radius))
        return None

    @staticmethod
    def median_filter(image: Image.Image | None, size: int = 3) -> Image.Image | None:
        if image:
            return image.filter(ImageFilter.MedianFilter(size=size))
        return None


class MainWindow(QMainWindow):
    def __init__(self, w: int = 640, h: int = 480):
        super().__init__()

        self._image = None
        self._org_image = None

        self.setWindowTitle("Hello World")
        self.setMinimumSize(QSize(w, h))

        menu_bar = QMenuBar(self)

        file = QMenu("File", self)
        open_action = file.addAction("Open File")
        open_action.triggered.connect(self.open_file)
        menu_bar.addMenu(file)

        transform = QMenu("Transform", self)
        rotate_action = transform.addAction("Rotate 90")
        rotate_action.triggered.connect(self.rotate)
        flip_action = transform.addAction("Flip Horizontally")
        flip_action.triggered.connect(self.flip)
        thumbnail_action = transform.addAction("Thumbnail")
        thumbnail_action.triggered.connect(self.thumbnail)
        menu_bar.addMenu(transform)

        image_menu = QMenu("Image", self)
        invert_action = image_menu.addAction("Invert Color")
        invert_action.triggered.connect(self.invert_color)
        colorize_action = image_menu.addAction("Colorize")
        colorize_action.triggered.connect(self.colorize)
        salt_and_peper_action = image_menu.addAction("Salt and Peper")
        salt_and_peper_action.triggered.connect(self.salt_and_pepper_noise)
        menu_bar.addMenu(image_menu)

        filter_menu = QMenu("Filter", self)
        sobel_action = filter_menu.addAction("Sobel")
        sobel_action.triggered.connect(self.sobel)
        gaussian_blur_action = filter_menu.addAction("Gaussian Blur")
        gaussian_blur_action.triggered.connect(self.gaussian_blur)
        median_filter_action = filter_menu.addAction("Median Filter")
        median_filter_action.triggered.connect(self.median_filter)
        menu_bar.addMenu(filter_menu)

        self.setMenuBar(menu_bar)

        self._layout = QVBoxLayout()
        self._label = QLabel(self)
        self._label.setMinimumSize(QSize(w, h))
        self._label.setAlignment(Qt.AlignCenter)
        self._layout.addWidget(self._label)
        self._widget = QWidget()
        self._widget.setLayout(self._layout)
        self.setCentralWidget(self._widget)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.xpm *.jpg)")
        if filename:
            self._org_image = Image.open(filename)
            self._image = self._org_image.copy()
            self.show_image(self._image)

    def show_image(self, image: Image.Image | None = None):
        if not image:
            return
        pixmap = QPixmap.fromImage(QImage(image.tobytes(), image.width, image.height, QImage.Format_RGB888))
        self._label.setPixmap(pixmap)

    def invert_color(self):
        self._image = ImageTransformer.invert_color(self._image)
        self.show_image(self._image)

    def rotate(self):
        self._image = ImageTransformer.rotate(self._image)
        self.show_image(self._image)

    def flip(self):
        self._image = ImageTransformer.flip(self._image)
        self.show_image(self._image)

    def thumbnail(self):
        self._image = ImageTransformer.thumbnail(self._image)
        self.show_image(self._image)

    def colorize(self):
        self._image = ImageTransformer.colorize(self._image)
        self.show_image(self._image)

    def sobel(self):
        self._image = ImageTransformer.sobel(self._image)
        self.show_image(self._image)

    def gaussian_blur(self):
        self._image = ImageTransformer.gaussian_blur(self._image)
        self.show_image(self._image)

    def salt_and_pepper_noise(self):
        self._image = ImageTransformer.salt_and_pepper_noise(self._image)
        self.show_image(self._image)

    def median_filter(self):
        self._image = ImageTransformer.median_filter(self._image)
        self.show_image(self._image)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()

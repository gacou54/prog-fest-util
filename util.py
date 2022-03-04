import io

import pydicom
import matplotlib.pyplot as plt
from pydicom.filebase import DicomFileLike
from matplotlib.image import imread


def read_dicom_dataset(raw_data: bytes) -> pydicom.Dataset:
    """Permet de lire les bytes d'un fichier DICOM et le transformer en Dataset DICOM"""
    buffer = io.BytesIO(raw_data)
    ds = pydicom.dcmread(buffer)

    return ds


def dicom_dataset_to_bytes(ds: pydicom.Dataset) -> io.BytesIO:
    """Permet d'écrire un Dataset DICOM en bytes"""
    buffer = io.BytesIO()
    memory_dataset = DicomFileLike(buffer)
    pydicom.dcmwrite(memory_dataset, ds)
    memory_dataset.seek(0)

    return buffer


def show_image_from_bytes(raw_data: bytes) -> None:
    buffer = io.BytesIO(raw_data)
    img = imread(buffer, format='png')

    plt.figure(figsize=(13, 10))
    plt.imshow(img)
    plt.axis('off')
    plt.show()


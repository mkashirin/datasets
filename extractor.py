from logging import basicConfig, info, INFO
from zipfile import ZipFile


def main():
    basicConfig(format="Extractor: %(message)s", level=INFO)

    with ZipFile("zip/datasets.zip", "r") as zip_ref:
        zip_ref.extractall("csv")

    info("All the files have been successfully extracted")


if __name__ == "__main__":
    main()

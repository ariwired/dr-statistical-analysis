"""
Gera os catálogos CSV (data/catalogs/) a partir dos metadados brutos.

    APTOS 2019: data/raw/aptos/train.csv -> data/catalogs/aptos_metadata.csv
    FDR26:      data/raw/fdr26/metadata_classification_DR.xlsx -> data/catalogs/fdr26_metadata.csv

"""
import csv
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RAW = RAIZ / "data" / "raw"
CATALOGOS = RAIZ / "data" / "catalogs"

NS = {"ns": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def ler_xlsx(caminho: Path) -> list[list[str]]:
    with zipfile.ZipFile(caminho) as z:
        shared = []
        if "xl/sharedStrings.xml" in z.namelist():
            with z.open("xl/sharedStrings.xml") as f:
                tree = ET.parse(f)
            shared = [si.text or "" for si in tree.findall(".//ns:t", NS)]
        with z.open("xl/worksheets/sheet1.xml") as f:
            tree = ET.parse(f)
        linhas = []
        for row in tree.findall(".//ns:row", NS):
            celulas = []
            for c in row.findall("ns:c", NS):
                tipo = c.get("t", "")
                v = c.find("ns:v", NS)
                if v is None:
                    celulas.append("")
                elif tipo == "s":
                    celulas.append(shared[int(v.text)])
                else:
                    celulas.append(v.text)
            linhas.append(celulas)
        return linhas


def montar_aptos() -> None:
    origem = RAW / "aptos" / "train.csv"
    with open(origem, newline="", encoding="utf-8-sig") as f:
        leitor = csv.DictReader(f)
        linhas = list(leitor)

    destino = CATALOGOS / "aptos_metadata.csv"
    with open(destino, "w", newline="", encoding="utf-8") as f:
        campos = ["dataset", "arquivo", "codigo_diagnostico", "grupo"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for linha in linhas:
            escritor.writerow({
                "dataset": "APTOS_2019",
                "arquivo": f"{linha['id_code']}.png",
                "codigo_diagnostico": linha["diagnosis"],
                "grupo": f"APTOS_2019_{linha['id_code']}",
            })
    print(f"APTOS: {len(linhas)} linhas -> {destino}")


def montar_fdr26() -> None:
    origem = RAW / "fdr26" / "metadata_classification_DR.xlsx"
    linhas = ler_xlsx(origem)
    cabecalho, dados = linhas[0], linhas[1:]
    idx = {nome: i for i, nome in enumerate(cabecalho)}

    destino = CATALOGOS / "fdr26_metadata.csv"
    with open(destino, "w", newline="", encoding="utf-8") as f:
        campos = ["dataset", "arquivo", "codigo_diagnostico", "grupo", "grade_dr", "sexe", "idade", "tipo_diabete"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for linha in dados:
            image_id = linha[idx["image_id"]]
            escritor.writerow({
                "dataset": "FDR26",
                "arquivo": f"{image_id}.jpg",
                "codigo_diagnostico": linha[idx["classe"]],
                "grupo": f"FDR26_{image_id[:-2]}",
                "grade_dr": linha[idx["grade_DR"]],
                "sexe": linha[idx["sexe"]],
                "idade": linha[idx["age"]],
                "tipo_diabete": linha[idx["type_diabete"]],
            })
    print(f"FDR26: {len(dados)} linhas -> {destino}")


if __name__ == "__main__":
    CATALOGOS.mkdir(parents=True, exist_ok=True)
    montar_aptos()
    montar_fdr26()

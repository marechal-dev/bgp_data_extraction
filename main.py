import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

START_DATE = "2022-10-02 00:00:00-03:00"
FINISH_DATE = "2022-10-02 22:00:00-03:00"

ASNS_RELATION = [
    {"number": "6507", "name": "Riot Games"},
    {"number": "46555", "name": "Take-Two Interactive"},
    {"number": "395856", "name": "2K Games"},
    {"number": "57976", "name": "Blizzard Entertainment"},
]

axes_font_styles = {
    "size": 16
}

Y_LABEL = "Tamanho do Caminho"

for asn in ASNS_RELATION:
    dataframe = pd.read_json(f"./data/day/AS{asn['number']}_output.json")

    dataframe["formatted_date"] = dataframe["date"].dt.strftime("%H")

    ASN_SUP_TITLE = f"AS{asn['number']} - {asn['name']}"
    ASN_TITLE = "Tamanho do Caminho - 02/10/22"

    X_LABEL = "Horário"

    asn_boxplot = dataframe.boxplot
    asn_boxplot(column="pathSize", by="formatted_date", fontsize=16, figsize=(10, 8))
    plt.title(ASN_TITLE)
    plt.suptitle(ASN_SUP_TITLE)
    plt.ylabel(Y_LABEL, fontdict=axes_font_styles)
    plt.xlabel(X_LABEL, fontdict=axes_font_styles)
    # plt.show()
    plt.savefig(f"./plots/AS{asn['number']}/AS{asn['number']}_pathSize.png")
    plt.close()

    dataframe_per_prefix = dataframe.groupby("prefix")

    for key, item in dataframe_per_prefix:
        PER_PREFIX_SUP_TITLE = f"AS{asn['number']} - {asn['name']} - Prefixo {key}"

        boxplot = item.boxplot
        boxplot(column="pathSize", by="formatted_date", fontsize=16, figsize=(10, 8))
        plt.title(ASN_TITLE)
        plt.suptitle(PER_PREFIX_SUP_TITLE)
        plt.xlabel(X_LABEL, fontdict=axes_font_styles)
        plt.ylabel(Y_LABEL, fontdict=axes_font_styles)
        plt.savefig(f"./plots/day/AS{asn['number']}/{str(key).replace('/', '_').replace(':', '_').replace('::', '__')}.png")
        plt.close()

ASN_PATH_SIZE_TITLE = "Tamanho do Caminho - 03/10 -> 09/10 (12h e 18h)"

for asn in ASNS_RELATION:
    dataframe = pd.read_json(f"./data/week/AS{asn['number']}/AS{asn['number']}_output.json")

    X_LABEL = "Dia e Hora"
    SUPERIOR_TITLE = f"AS{asn['number']} - {asn['name']}"

    dataframe["formatted_date"] = dataframe["date"].dt.strftime("%d %H")

    asn_boxplot = dataframe.boxplot
    asn_boxplot(column="pathSize", by="formatted_date", fontsize=16, figsize=(12, 10))
    plt.suptitle(SUPERIOR_TITLE)
    plt.title(ASN_PATH_SIZE_TITLE)
    plt.ylabel(Y_LABEL, fontdict=axes_font_styles)
    plt.xlabel(X_LABEL, fontdict=axes_font_styles)
    # plt.show()
    plt.savefig(f"./plots/AS{asn['number']}/AS{asn['number']}_week_pathSize.png")
    plt.close()

    dataframe_per_prefix = dataframe.groupby("prefix")

    for key, item in dataframe_per_prefix:
        PREFIX_SUP_TITLE = f"AS{asn['number']} - {asn['name']} - Prefixo {key}"

        boxplot = item.boxplot
        boxplot(column="pathSize", by="formatted_date", fontsize=16, figsize=(12, 10))
        plt.title(ASN_PATH_SIZE_TITLE)
        plt.suptitle(PREFIX_SUP_TITLE)
        plt.xlabel(X_LABEL, fontdict=axes_font_styles)
        plt.ylabel(Y_LABEL, fontdict=axes_font_styles)
        plt.savefig(f"./plots/week/AS{asn['number']}/{str(key).replace('/', '_').replace(':', '_').replace('::', '__')}.png")
        plt.close()

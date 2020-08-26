import pandas_datareader
import pandas as pd
import mplfinance
from pylab import *

pd.set_option('mode.chained_assignment', None,
              'display.precision', 1)  # "display.max_columns", None, "display.width", None,


# try:
#     self.datos = pd.read_pickle(simbolo)
# except FileNotFoundError:
#     self.datos = pandas_datareader.DataReader(simbolo, "yahoo", fecha_inicial, fecha_final)
#     self.datos.to_pickle(simbolo)


class VerDatos:

    def __init__(self, simbolo="GOOG", fecha_inicial="2010-01-01", fecha_final="2020-01-01"):

        self.datos = pandas_datareader.DataReader(simbolo, "yahoo", fecha_inicial, fecha_final)
        self.fecha_inicial = fecha_inicial
        self.fecha_final = fecha_final
        self.simbolo = simbolo
        self.low = self.datos.Low
        self.high = self.datos.High
        self.volume = self.datos.Volume
        self.open = self.datos.Open
        self.close = self.datos.Close
        self.precio = self.datos["Adj Close"]
        self.sopyres = pd.DataFrame(index=self.datos.index, columns=["sop_tolera", "res_tolera",
                                                                     "soporte", "resistencia"])

        self.Tecnologia = ['MSFT', 'GOOG', 'FB', 'T', 'CSCO', 'ORCL', 'SAP', 'ADBE', 'IBM', 'ACN',
                           'CRM', 'TXN', 'AVGO', 'NVDA', 'QCOM', 'UBER', 'INTU', 'ADP', 'TMUS', 'VMW', 'CCI', 'NOW',
                           'WDAY', 'AMAT', 'ADI', 'FIS', 'LHX', 'EQIX', 'DELL', 'CTSH', 'ADSK', 'AMD', 'ATVI', 'SQ',
                           'TWTR']
        self.BienesDeConsumo = ['AAPL', 'PG', 'KO', 'TM', 'PEP', 'NKE', 'PM', 'MO', 'MDLZ', 'EL', 'CL', 'GM', 'KMB',
                                'PHG', 'TSLA', 'STZ', 'F', 'KHC', 'JCI', 'MNST', 'VFC', 'GIS', 'HSY', 'TSN', 'PCAR']
        self.Financieros = ['JPM', 'BAC', 'MA', 'WFC', 'C', 'PYPL', 'AXP', 'AMT', 'USB', 'GS', 'MS', 'BLK', 'CME', 'CB',
                            'V', 'AABA', 'PNC', 'BX', 'SCHW', 'MMC']
        self.Salud = ['JNJ', 'UNH', 'PFE', 'NVS', 'MRK', 'ABT', 'TMO', 'AZN', 'AMGN', 'LLY', 'SNY', 'GSK',
                      'ABBV', 'NVO', 'GILD', 'SYK', 'ANTM', 'BMY', 'CVS', 'BDX', 'CI', 'ISRG', 'BSX', 'ZTS',
                      'AGN', 'TAK', 'HCA', 'BIIB', 'ILMN', 'EW', 'VRTX', 'BAX', 'HUM', 'REGN', 'IQV', 'ALC', 'ALXN']
        self.Industrial = ['BA', 'HON', 'UTX', 'LMT', 'DHR', 'MMM', 'GE', 'CAT', 'NOC', 'GD', 'DE', 'RTN', 'ITW', 'WM',
                           'EMR', 'ABB']

    def graficar(self, volumen=False, media_movil=20, n_bins=20, margen=0.2, soportes_resistencias=False, covid=True):

        colores = mplfinance.make_marketcolors(up="forestgreen", down="crimson")
        estilo = mplfinance.make_mpf_style(marketcolors=colores)

        if soportes_resistencias:
            self.sopyres["precio"] = self.precio
            if covid == True and pd.to_datetime(self.fecha_inicial)<pd.to_datetime("2019-12-31"):
                con_covid=dict(vlines=["2020-01-01", "2020-03-11"],
                                     linewidths=[0.1, 0.1],
                                     colors=["k", "r"],
                                     linestyle="--")
            else:
                con_covid=[]

            for losx in range((n_bins - 1) + n_bins, len(self.sopyres)):
                seleccion = self.sopyres[losx - n_bins: losx + 1]
                nivel_soporte = min(seleccion.precio)
                nivel_resistencia = max(seleccion.precio)
                nivel_rango = nivel_soporte - nivel_resistencia

                self.sopyres["resistencia"][losx] = nivel_resistencia
                self.sopyres["soporte"][losx] = nivel_soporte
                self.sopyres["sop_tolera"][losx] = nivel_soporte + margen * nivel_rango
                self.sopyres["res_tolera"][losx] = nivel_resistencia - margen * nivel_rango
            maximini = [mplfinance.make_addplot(self.sopyres["sop_tolera"], color='g'),
                        mplfinance.make_addplot(self.sopyres["res_tolera"], color='r')]
            setup = dict(type="candle", volume=volumen, mav=media_movil, style=estilo, title=self.simbolo,
                         addplot=maximini,
                         vlines=con_covid,
                         hlines=dict(hlines=self.precio[-1], linestyle="--", colors="k"),
                         alines=dict(alines=[(self.high.index[este_x], self.high.values[este_x])
                                             for este_x in arange(0, len(self.high), 20)])
                         )

            mplfinance.plot(self.datos, **setup)

            # print("\n\nEn este grafico se pueden modificar los siguientes parametos",
            #       "\nvolumen = ", volumen,
            #       "\nMedia Movil = ", media_movil,
            #       "\nSoportes y Resistencias", soportes_resistencias,
            #       "\nmargen = ", margen,
            #       "\nn_bins = ", n_bins,
            #       "\n\n\nEJEMPLO""\nfrom Datos import VerDatos"
            #       "\ndatos = VerDatos()"
            #       "\ndatos.graficar(soportes_resistencias=True,n_bins=100,margen=1 )"
            #       )
        else:

            if covid == True and pd.to_datetime(self.fecha_inicial)<pd.to_datetime("2019-12-31"):
                con_covid=dict(vlines=["2020-01-01", "2020-03-11"],
                                     linewidths=[0.1, 0.1],
                                     colors=["k", "r"],
                                     linestyle="--")
            else:
                con_covid=[]

            setup = dict(type="candle",
                         volume=volumen,
                         mav=media_movil,
                         style=estilo,
                         title=self.simbolo,
                         hlines=dict(hlines=self.precio[-1], linestyle="--", colors="k"),
                         vlines=con_covid,
                         alines=dict(alines=[(self.precio.index[este_x], self.precio.values[este_x])
                                             for este_x in arange(0, len(self.precio), 10)],linewidths=30,
                                     alpha=0.3,colors="darkgreen")
                         )


            mplfinance.plot(self.datos, **setup, )

            # candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)
            show()

    def subplots(self, activos_financieros=("AMD", "DELL", "AMZN", "GOOG",
                                            "AAPL", "TSLA", "NKE", "KO",
                                            "JPM", "USB", "BLK", "MNST",
                                            "JNJ", "MRK", "TMO", "ABT")):
        self.datos = pandas_datareader.DataReader(activos_financieros, "yahoo", self.fecha_inicial, self.fecha_final)
        self.activos_financieros = self.datos
        self.precios = pd.DataFrame(self.datos["Adj Close"])
        # # elif insdustria == "salud":
        # #     seleccion=choice(Sectores.Salud, 9)
        # #     self.datos = pandas_datareader.DataReader(seleccion, "yahoo", self.fecha_inicial, self.fecha_final)
        # # elif insdustria == "financieros":
        # #     seleccion = choice(Sectores.Financieros, 9)
        # #     self.datos = pandas_datareader.DataReader(seleccion, "yahoo", self.fecha_inicial, self.fecha_final)
        # # elif insdustria == "bienes":
        # #     seleccion = choice(Sectores.BienesDeConsumo, 9)
        # #     self.datos = pandas_datareader.DataReader(seleccion, "yahoo", self.fecha_inicial, self.fecha_final)
        # # elif insdustria == "industrial":
        # #     seleccion=choice(Sectores.Industrial, 9)
        # #     self.datos = pandas_datareader.DataReader(seleccion, "yahoo", self.fecha_inicial, self.fecha_final)
        for un_x in range(0, len(activos_financieros)):
            subplot(4, 4, un_x + 1)
            axis("off")
            funcion = self.datos["Adj Close"].iloc[:, un_x]
            funcion.plot(figsize=(10, 10), c=(random(), random(), random()))
            legend()
            text(funcion.index[-1], funcion.values[-1], f'{funcion.values[-1]:,.0f}')
            vlines(funcion.index[-117], funcion.values.min(), funcion.values.max(), colors="r", linestyles="dashed")
            hlines(funcion.values[-1], funcion.index[0], funcion.index[-1], colors="k",lw=1)

        show()

    def correlacion(self):
        fig, ax = subplots()
        self.correlacion = ax.matshow(self.precios.corr(), cmap="jet")
        ax.set_xticks(arange(len(self.precios.corr())))
        ax.set_yticks(arange(len(self.precios.corr())))
        ax.set_xticklabels(self.precios.columns, rotation=-90)
        ax.set_yticklabels(self.precios.columns)

        for unos in range(len(self.precios.columns)):
            for doces in range(len(self.precios.columns)):
                ax.text(unos, doces, f'{self.precios.corr().iloc[unos, doces]:.1g}', ha="center", va="center",
                        color="w")

        show()

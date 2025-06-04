import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.store = None

    def fillddStore(self):
        stores = self._model.getStores()
        for s in stores:
            self._view._ddStore.options.append(ft.dropdown.Option(s,on_click=self.setStore))

    def setStore(self,e):
        if e.control.data != "":
            self.store = e.control.data
        else:
            self.store = None
    def handleCreaGrafo(self, e):
        if self.store is None:
            self._view.txt_result.control.clear()
            self._view.txt_result.control.append(ft.Text("Non hai selezionato nessun negozio",color="red"))
            self._view.update_page()
            return

        self._model.buildGraph(self.store)
    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass

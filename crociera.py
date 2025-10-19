class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self._nome=nome
        self.listaPersone = []
        self.listaCabine=[]

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome

    def __str__(self):
        return f"-Nome crociera: {self._nome}"



    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO

        with open(file_path, "r", encoding="utf-8") as openfile:

            for line in openfile:
                riga = line.rstrip().split(',')

                if len(riga) == 3:
                    persona=Passeggero(code_persona=riga[0], nome=riga[1], cognome=riga[2],alloggiato=False,cabina='Non assegnata')
                    self.listaPersone.append(persona)

                elif len(riga)==4:
                    cabina=Cabina(codCabina=riga[0],numLetti=riga[1],ponte=riga[2], prezzo=float(riga[3]),disponibile=True)
                    self.listaCabine.append(cabina)

                elif len(riga)==5:
                    if riga[4].isalpha():
                        cabina=CabDeluxe(codCabina=riga[0],numLetti=riga[1],ponte=riga[2], prezzo=float(riga[3]),tipologia=riga[4],disponibile=True)
                        self.listaCabine.append(cabina)
                    elif riga[4].isdigit():
                        cabina=CabinaAnimali(codCabina=riga[0],numLetti=riga[1],ponte=riga[2], prezzo=float(riga[3]),numAnimali=float(riga[4]),disponibile=True)
                        self.listaCabine.append(cabina)




    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        for cab in self.listaCabine:
            if cab.codCabina == codice_cabina:
                for passeggero in self.listaPersone:
                    if passeggero.codePersona==codice_passeggero:
                        if cab.disponibile==True and passeggero.alloggiato==False:
                           cab.disponibile=False
                           passeggero.alloggiato=True
                           passeggero.cabina=f'{codice_cabina}'
                           return "Cabina assegnata con successo."
                        else:
                            if cab.disponibile==False and passeggero.alloggiato==True:
                                return 'Assegnazione non riuscita: passeggero assegnato e cabina non disponibile'
                            else:
                                if cab.disponibile == False:
                                    return 'Assegnazione non riuscita: cabina non disponibile (occupata)'
                                elif passeggero.alloggiato == True:
                                    return 'Assegnazione non riuscita: passeggero già assegnsato in una cabina'



    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        cabineOrdinate=sorted(self.listaCabine, key=lambda x: x.prezzo)
        return cabineOrdinate


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

        for passeggero in self.listaPersone:
            print(passeggero)



class Cabina:

     def __init__(self, codCabina, numLetti, ponte, prezzo,disponibile):
         self.codCabina = codCabina
         self.numLetti = numLetti
         self.ponte = ponte
         self.prezzo = prezzo
         self.disponibile = True

     def __str__(self):
         return f"-Codice cabina: {self.codCabina}, Numero letti: {self.numLetti}, Ponte: {self.ponte}, Prezzo: {self.prezzo} "


class CabDeluxe(Cabina):

    def __init__(self, codCabina, numLetti,ponte, prezzo,tipologia,disponibile):
        super().__init__(codCabina,numLetti,ponte,prezzo,disponibile)
        self.prezzo =prezzo * 1.20
        self.tipologia=tipologia

    def __str__(self):
        return f'-Codice cabina: {self.codCabina} |Cabina Deluxe|, Numero letti: {self.numLetti}, Ponte: {self.ponte}, Prezzo: {self.prezzo}, Tipologia: {self.tipologia} '


class CabinaAnimali(Cabina):

    def __init__(self,codCabina,numLetti,ponte,prezzo,numAnimali,disponibile):
        super().__init__(codCabina,numLetti,ponte, prezzo,disponibile)
        self.numAnimali = numAnimali
        self.prezzo=prezzo* (1 + 0.10*numAnimali)

    def __str__(self):
        return f'-Codice cabina: {self.codCabina} |Cabina Animali|, Numero letti: {self.numLetti}, Ponte: {self.ponte}, Prezzo: {self.prezzo}€, Numero di animali: {self.numAnimali} '


class Passeggero():
    def __init__(self,code_persona,nome,cognome,alloggiato,cabina):
        self.codePersona = code_persona
        self.nome = nome
        self.cognome = cognome
        self.alloggiato = False
        self.cabina='Non assegnata'


    def __str__(self):
        return f'-Codice: {self.codePersona}, Nome passegro: {self.nome}, Cognome passegro: {self.cognome}, Cabina={self.cabina}'
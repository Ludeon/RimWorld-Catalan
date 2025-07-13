# Script dedicado a crear listas de palabras para los archivos female.txt, de forma que su género sea adecuado en distintas situaciones.
# Créditos a Zerstrick


def agregar_materiales(texto):
    # Definimos las listas de materiales
    # Edificios y muebles
    lista_madera = [f"{texto} de fusta"]
    lista_acero = [f"{texto} d’acer"]
    lista_plata = [f"{texto} de plata"]
    lista_uranio = [f"{texto} d’urani"]
    lista_plastiacero = [f"{texto} de plastacer"]
    lista_oro = [f"{texto} d’or"]
    lista_bioferrita = [f"{texto} de bioferrita"]
    lista_arenisca = [f"{texto} de gres"]
    lista_granito = [f"{texto} de granit"]
    lista_caliza = [f"{texto} de pedra calcària"]
    lista_pizarra = [f"{texto} de pissarra"]
    lista_marmol = [f"{texto} de marbre"]
    lista_jade = [f"{texto} de jade"]
    lista_obsidiana = [f"{texto} d’obsidiana"]
    lista_vaciorita = [f"{texto} d’espaidirita"]
    # Textiles
    lista_tela = [f"{texto} de tela"]
    lista_cuero_ligero = [f"{texto} de pell lleugera"]
    lista_lana_de_oveja = [f"{texto} de llana d’ovella"]
    lista_cuero_liso = [f"{texto} de pell senzilla"]
    lista_hilodiablo = [f"{texto} de fibradimoni"]
    lista_tela_sintetica = [f"{texto} de sintefil"]
    lista_lana_de_megaperezoso = [f"{texto} de llana de megaperesós"]
    lista_lana_de_mufalo = [f"{texto} de llana de múfal"]
    lista_lana_de_bisonte = [f"{texto} de llana de bisó"]
    lista_lana_de_mastodonte = [f"{texto} de llana de mastodont"]
    lista_lana_de_buey_almizclero = [f"{texto} de llana de bou mesquer"]
    lista_lana_de_alpaca = [f"{texto} de llana d’alpaca"]
    lista_piel_de_pajaro = [f"{texto} de pell d’ocell"]
    lista_hipertejido = [f"{texto} d’hiperteixit"]
    lista_cuero_parcheado = [f"{texto} de pedaços de pell"]
    lista_cuero_de_perro = [f"{texto} de pell de gos"]
    lista_cuero_de_lagarto = [f"{texto} de pell de rèptil"]
    lista_piel_de_lobo = [f"{texto} de pell de llop"]
    lista_pelaje_felino = [f"{texto} de pell de gat"]
    lista_pelaje_de_zorro = [f"{texto} de pell de guineu"]
    lista_piel_de_cerdo = [f"{texto} de cuir de porc"]
    lista_cuero_de_camello = [f"{texto} de pell de camell"]
    lista_piel_de_oso = [f"{texto} de pell d’ós"]
    lista_pelaje_azul = [f"{texto} de pell de múfal"]
    lista_cuero_de_elefante = [f"{texto} de cuir d’elefant"]
    lista_pelaje_grueso = [f"{texto} de pell gruixuda"]
    lista_cuero_temible = [f"{texto} de cuiropor"]
    lista_piel_de_pinnipeda = [f"{texto} de piel de pinnípeda"]
    lista_cuero_de_rinoceronte = [f"{texto} de pell de rinoceront"]
    lista_pelaje_de_cobaya = [f"{texto} de pell de conillet d’Índies"]
    lista_pelaje_de_chinchilla = [f"{texto} de pell de xinxilla"]
    lista_cuero_humano = [f"{texto} de pell d’humà"]
    lista_pelaje_de_trumbo = [f"{texto} de pell de trumbe"]
    lista_cuero_de_armadillo = [f"{texto} de pell d’armadillo"]
    lista_cuero_de_hipopotamos = [f"{texto} de pell d’hipopòtam"]
    lista_cuero_de_mastodonte = [f"{texto} de pell de mastodont"]
    lista_piel_de_vison = [f"{texto} de pell de visó"]
    lista_crin_de_trumbo = [f"{texto} de crinera de trumbe"]
    lista_piel_ligera = [f"{texto}pell lleugera"]
    lista_piel_pantera = [f"{texto}pell de pantera"]
    lista_cuero_pesado = [f"{texto}pell de cuir pesat"]
    llista_pell_foca = [f"{texto}pell de foca"]

    # Textiles sin cuero
    lista_tela = [f"{texto} de tela"]
    lista_lana_de_oveja = [f"{texto} de llana d’ovella"]
    lista_hilodiablo = [f"{texto} de fibradimoni"]
    lista_tela_sintetica = [f"{texto} de sintefil"]
    lista_lana_de_megaperezoso = [f"{texto} de llana de megaperesós"]
    lista_lana_de_mufalo = [f"{texto} de llana de múfal"]
    lista_lana_de_bisonte = [f"{texto} de llana de bisó"]
    lista_lana_de_mastodonte = [f"{texto} de llana de mastodont"]
    lista_lana_de_buey_almizclero = [f"{texto} de llana de bou mesquer"]
    lista_lana_de_alpaca = [f"{texto} de llana d’alpaca"]
    lista_hipertejido = [f"{texto} d’hiperteixit"]

    # Solicitamos al usuario que seleccione una lista
    print("Por favor, seleccione una lista:")
    print("1. Madera, Acero, Plata, Uranio, Plastiacero, Oro, Bioferrita, Obsidiana")
    print(
        "2. Madera', 'Acero', 'Arenisca', 'Granito', 'Caliza', 'Pizarra', 'Mármol', 'Jade', 'Plata', 'Uranio', 'Plastiacero', 'Oro', 'Bioferrita', 'Obsidiana', 'Vaciorita"
    )
    print("3. Textiles")
    print("4. Textiles sin cuero")
    opcion = input("Ingrese el número correspondiente a la lista deseada: ")

    # Mostramos el contenido de la lista seleccionada y preguntamos al usuario si está de acuerdo
    if opcion == "1":
        print("\nContenido de la lista 1:")
        for material in (
            lista_madera
            + lista_acero
            + lista_plata
            + lista_uranio
            + lista_plastiacero
            + lista_oro
            + lista_bioferrita
            + lista_obsidiana
        ):
            print(material)
    elif opcion == "2":
        print("\nContenido de la lista 2:")
        for material in (
            lista_madera
            + lista_acero
            + lista_arenisca
            + lista_granito
            + lista_caliza
            + lista_pizarra
            + lista_marmol
            + lista_jade
            + lista_plata
            + lista_uranio
            + lista_plastiacero
            + lista_oro
            + lista_obsidiana
            + lista_bioferrita
            + lista_vaciorita
        ):
            print(material)
    elif opcion == "3":
        print("\nContenido de la lista 3:")
        for material in (
            lista_tela
            + lista_cuero_ligero
            + lista_lana_de_oveja
            + lista_cuero_liso
            + lista_hilodiablo
            + lista_tela_sintetica
            + lista_lana_de_megaperezoso
            + lista_lana_de_mufalo
            + lista_lana_de_bisonte
            + lista_lana_de_mastodonte
            + lista_lana_de_buey_almizclero
            + lista_lana_de_alpaca
            + lista_piel_de_pajaro
            + lista_hipertejido
            + lista_cuero_parcheado
            + lista_cuero_de_perro
            + lista_cuero_de_lagarto
            + lista_piel_de_lobo
            + lista_pelaje_felino
            + lista_pelaje_de_zorro
            + lista_piel_de_cerdo
            + lista_cuero_de_camello
            + lista_piel_de_oso
            + lista_pelaje_azul
            + lista_cuero_de_elefante
            + lista_cuero_de_mastodonte
            + lista_pelaje_grueso
            + lista_cuero_temible
            + lista_piel_de_pinnipeda
            + lista_cuero_de_rinoceronte
            + lista_pelaje_de_cobaya
            + lista_pelaje_de_chinchilla
            + lista_cuero_de_armadillo
            + lista_cuero_de_hipopotamos
            + lista_piel_de_vison
            + lista_cuero_humano
            + lista_pelaje_de_trumbo
            + lista_crin_de_trumbo
            + lista_piel_ligera
            + lista_piel_pantera
            + llista_pell_foca
        ):
            print(material)
    elif opcion == "4":
        print("\nContenido de la lista 4:")
        for material in (
            lista_tela
            + lista_lana_de_oveja
            + lista_hilodiablo
            + lista_tela_sintetica
            + lista_lana_de_megaperezoso
            + lista_lana_de_mufalo
            + lista_lana_de_bisonte
            + lista_lana_de_mastodonte
            + lista_lana_de_buey_almizclero
            + lista_lana_de_alpaca
            + lista_hipertejido
        ):
            print(material)
    else:
        print("Opción no válida")


# Solicitamos al usuario que ingrese un texto
texto_ingresado = input("Ingrese un texto: ")

# Llamamos a la función para agregar materiales al texto ingresado
agregar_materiales(texto_ingresado)

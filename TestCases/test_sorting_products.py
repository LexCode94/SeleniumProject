from Pages.PLP import PLP


def test_sorting_name_ascending(setup, login):
    plp = PLP(setup)
    plp.sort("az")

    product_names = plp.get_product_names()


    assert product_names == sorted(product_names)

def test_sorting_name_descending(setup, login):
    plp = PLP(setup)
    plp.sort("za")

    product_names = plp.get_product_names()

    assert product_names == sorted(product_names, reverse=True)


def test_sorting_price_ascending(setup, login):
    plp = PLP(setup)
    plp.sort("lohi")

    product_prices = plp.get_product_prices()

    assert product_prices == sorted(product_prices)


def test_sorting_price_descending(setup, login):
    plp = PLP(setup)
    plp.sort("hilo")

    product_prices = plp.get_product_prices()

    assert product_prices == sorted(product_prices, reverse=True)


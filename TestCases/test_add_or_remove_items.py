from Pages.PLP import PLP


def test_items_added_to_cart(setup, login):
    plp = PLP(setup)
    plp.click_add_buttons(4)
    number_of_items_in_cart = plp.get_number_of_items_in_cart()
    number_of_remove_buttons = plp.get_remove_buttons()

    assert number_of_items_in_cart == number_of_remove_buttons

import pytest
from selenium_helpers import load_page, get_element_property

def test_color(driver, config, tested_elements):
    load_page(driver, config['url'], config['timeout'])
    element = tested_elements['cookie_div']
    color = get_element_property(driver, element['selector'], 'background-color')
    assert color == element['properties']['background-color'], "Test 1 fail"

def test_height(driver, config, tested_elements):
    load_page(driver, config['url'], config['timeout'])
    element = tested_elements['cookie_div']
    height = get_element_property(driver, element['selector'], 'height')
    assert height == element['properties']['height'], "Test 2 fail"

if __name__ == "__main__":
    pytest.main()

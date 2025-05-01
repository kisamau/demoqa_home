
from tests.tests_hw.components_test import Components


class AccordionPage(Components):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver,self.base_url)

        self.element_cont = Components(driver, '#section1Content > p')
        self.element_hd = Components(driver, '#section1Heading')
        self.element_1 = Components(driver, '#section2Content > p:nth-child(1)')
        self.element_2 = Components(driver, '#section2Content > p:nth-child(2)')
        self.element_3 = Components(driver, '#section3Content > p')

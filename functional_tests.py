# My computer history web site as an example

# Boiler Plate


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        if os.name=='nt':
            self.browser = webdriver.Chrome("/Users/lwwil_000/AppData/Local/Programs/Python/Python35/chromedriver.exe")
        else:
            self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()


    #####################
    # END OF BOILER PLATE
    #####################

    def test_home_page(self):
        """

        The fraternal bonds found in exclusive societies -
        appeal to millennials during their liminal period.
        These groups attract many young people because of
        an identity crisis and because of widespread latent
        deep seated fears of personal nonfulfillment.  

        """

        self.browser.get('http://localhost:8000/index.html')

        # there is a page title defined by <title></title> on the home page
        # check it

        self.assertIn('Exclusive Societies',self.browser.title)

        # You will have an image for your home page I am assuming.
        # Put the name of your image here in place of homebrew.png
        # In general this is how we check for images on a page.

        #The user sees an image of a pathway

        m=self.browser.find_element_by_tag_name('img')
        self.assertIn('home.jpg',m.get_attribute('src'))

        # testing the image for a clickable area by the ID tag
        a=self.browser.find_element_by_id('homepage')
        a.click()

        self.assertIn('Lamp',self.browser.title)

        h=self.browser.find_element_by_tag_name('h1')

        m=self.browser.find_element_by_tag_name('img')

        #the user goes back to the home page
        #self.browser.back()
        self.browser.get('http://localhost:8000/index.html')

        #the user sees at the bottom of the pages a link to credits
        l=self.browser.find_element_by_link_text('Credits')

        #user clicks on the credits link
        l.click()

        #and sees the credtis.html page
        a=self.browser.current_url
        self.assertIn("credits.html",a)



if __name__=="__main__":
        unittest.main(warnings="ignore")

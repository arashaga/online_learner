from django.test import TestCase

# Create your tests here.
##TODO: 1- define the html
##TODO: 2- read the csv file from the input box
##TODO: 3- preprocess the data
##TODO:     3.1- take care of NAs
##TODO:     3.2- confirm and show the sample data
##TODO: 4- pick the features and run the ML

from selenium import webdriver
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from django.test import Client
from online_learner.models import Document
import time

class NewLearnerTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    # def check_for_row_in_list_table(self, row_text):
    #     table = self.browser.find_element_by_id('id_list_table')
    #     rows = table.find_elements_by_tag_name('tr')
    #     self.assertIn(row_text, [row.text for row in rows])

    def test_upload_file(self):
        c = Client()
        with open('file.csv') as fp:
            c.post('/', {'my_file': 'fred', 'attachment': fp})


class Modeltest(TestCase):
    list_ = Document()
    list_.save()

    first_item = Item()
    first_item.text = 'The first (ever) list item'
    first_item.list = list_
    first_item.save()

    second_item = Item()
    second_item.text = 'Item the second'
    second_item.list = list_
    second_item.save()

    saved_list = List.objects.first()
    self.assertEqual(saved_list, list_)

    saved_items = Item.objects.all()
    self.assertEqual(saved_items.count(), 2)

    first_saved_item = saved_items[0]
    second_saved_item = saved_items[1]
    self.assertEqual(first_saved_item.text, 'The first (ever) list item')
    self.assertEqual(first_saved_item.list, list_)
    self.assertEqual(second_saved_item.text, 'Item the second')
    self.assertEqual(second_saved_item.list, list_)
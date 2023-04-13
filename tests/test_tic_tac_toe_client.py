import pytest
import selenium
import docker
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestTicTacToeClient:

    @pytest.fixture(scope="class")
    def client_web_driver(self):
        driver: webdriver.Chrome = webdriver.Chrome()
        driver.get("http://localhost:3000")
        driver.maximize_window()
        driver.implicitly_wait(2)
        return driver
    
    def test_tic_tac_toe_client(self, client_web_driver: webdriver.Chrome):
        assert client_web_driver.title == "Tic Tac Toe"

    def test_tic_tac_toe_client_x_wins(self, client_web_driver: webdriver.Chrome):
        time.sleep(2)
        client_web_driver.find_element(By.ID, "0-0").click()
        client_web_driver.find_element(By.ID, "1-0").click()
        client_web_driver.find_element(By.ID, "1-1").click()
        client_web_driver.find_element(By.ID, "0-1").click()
        client_web_driver.find_element(By.ID, "2-2").click()
        assert client_web_driver.find_element(By.ID, "winner").text == "X Wins!"

    def test_tic_tac_toe_client_o_wins(self, client_web_driver: webdriver.Chrome):
        client_web_driver.find_element(By.ID, "reset").click()
        client_web_driver.find_element(By.ID, "2-2").click()
        client_web_driver.find_element(By.ID, "0-0").click()
        client_web_driver.find_element(By.ID, "2-1").click()
        client_web_driver.find_element(By.ID, "1-0").click()
        client_web_driver.find_element(By.ID, "0-2").click()
        client_web_driver.find_element(By.ID, "2-0").click()
        assert client_web_driver.find_element(By.ID, "winner").text == "O Wins!"
    
    # def test_tic_tac_toe_client_draw(self, client_web_driver: webdriver.Chrome):
    #     client_web_driver.find_element(By.ID, "0").click()
    #     client_web_driver.find_element(By.ID, "1").click()
    #     client_web_driver.find_element(By.ID, "2").click()
    #     client_web_driver.find_element(By.ID, "3").click()
    #     client_web_driver.find_element(By.ID, "4").click()
    #     client_web_driver.find_element(By.ID, "5").click()
    #     client_web_driver.find_element(By.ID, "6").click()
    #     client_web_driver.find_element(By.ID, "7").click()
    #     client_web_driver.find_element(By.ID, "8").click()
    #     assert client_web_driver.find_element(By.ID, "winner").text == "Draw!"

    # def test_tic_tac_toe_client_reset(self, client_web_driver: webdriver.Chrome):
    #     client_web_driver.find_element(By.ID, "reset").click()
    #     assert client_web_driver.find_element(By.ID, "winner").text == ""
import pytest
import selenium
import docker
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

class TestTicTacToeClient:
    @pytest.fixture(autouse=True, scope='function')
    def _reset_game(self):
        requests.post('http://localhost:5000/game/reset')
    
    @pytest.fixture(scope='function')
    def client_web_driver(self):
        web_driver = webdriver.Chrome()
        web_driver.get("http://localhost:3000")
        yield web_driver
        web_driver.close()

    
    def test_tic_tac_toe_client(self, client_web_driver: webdriver.Chrome):
        assert client_web_driver.title == "Tic Tac Toe"

    def test_tic_tac_toe_client_x_wins(self, client_web_driver: webdriver.Chrome):
        WebDriverWait(client_web_driver, 10).until(EC.element_to_be_clickable((By.ID, "0-0")))
        client_web_driver.find_element(By.ID, "0-0").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "1-0").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "1-1").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "0-1").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "2-2").click()
        time.sleep(1)
        WebDriverWait(client_web_driver, 10).until(EC.visibility_of(client_web_driver.find_element(By.ID, "winner")))
        assert client_web_driver.find_element(By.ID, "winner").text == "X Wins!"

    def test_tic_tac_toe_client_o_wins(self, client_web_driver: webdriver.Chrome):
        WebDriverWait(client_web_driver, 10).until(EC.element_to_be_clickable((By.ID, "0-0")))
        time.sleep(1)
        client_web_driver.find_element(By.ID, "2-2").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "0-0").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "2-1").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "1-0").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "0-2").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "2-0").click()
        WebDriverWait(client_web_driver, 10).until(EC.visibility_of(client_web_driver.find_element(By.ID, "winner")))
        assert client_web_driver.find_element(By.ID, "winner").text == "O Wins!"
    
    def test_tic_tac_toe_client_draw(self, client_web_driver: webdriver.Chrome):
        WebDriverWait(client_web_driver, 10).until(EC.element_to_be_clickable((By.ID, "0-0")))
        time.sleep(1)
        client_web_driver.find_element(By.ID, "0-0").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "0-1").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "0-2").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "1-1").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "2-1").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "2-0").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "1-0").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "1-2").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "2-2").click()
        WebDriverWait(client_web_driver, 10).until(EC.visibility_of(client_web_driver.find_element(By.ID, "winner")))
        assert client_web_driver.find_element(By.ID, "winner").text == "Draw"

    def test_tic_tac_toe_client_reset(self, client_web_driver: webdriver.Chrome):
        WebDriverWait(client_web_driver, 10).until(EC.element_to_be_clickable((By.ID, "0-0")))
        time.sleep(1)
        client_web_driver.find_element(By.ID, "0-0").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "0-1").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "0-2").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "1-1").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "2-1").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "2-0").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "1-0").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "1-2").click()
        time.sleep(1)
        client_web_driver.find_element(By.ID, "2-2").click()
        assert client_web_driver.find_element(By.ID, "winner").text == "Draw"
        client_web_driver.find_element(By.ID, "reset").click()
        time.sleep(1)
        WebDriverWait(client_web_driver, 10).until(EC.element_to_be_clickable((By.ID, "0-0")))
        assert client_web_driver.find_element(By.ID, "0-0").text == "-"
        assert client_web_driver.find_element(By.ID, "0-1").text == "-"
        assert client_web_driver.find_element(By.ID, "0-2").text == "-"
        assert client_web_driver.find_element(By.ID, "1-0").text == "-"
        assert client_web_driver.find_element(By.ID, "1-1").text == "-"
        assert client_web_driver.find_element(By.ID, "1-2").text == "-"
        assert client_web_driver.find_element(By.ID, "2-0").text == "-"
        assert client_web_driver.find_element(By.ID, "2-1").text == "-"
        assert client_web_driver.find_element(By.ID, "2-2").text == "-"
        time.sleep(2)

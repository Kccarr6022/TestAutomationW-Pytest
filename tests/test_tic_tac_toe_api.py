import requests
import pytest

class TestTicTacToeAPI:
    @pytest.fixture(autouse=True, scope='function')
    def _reset_game(self):
        requests.post('http://localhost:5000/game/reset')
        
    def test_get_game(self):
        r = requests.get('http://localhost:5000/game')
        assert r.status_code == 200
        assert r.json() == {
            'board': [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']],
            'game_over': False,
            'winner': None
        }

    def test_post_move(self):
        r = requests.post('http://localhost:5000/game/move', json={'row': 1, 'col': 1})
        assert r.status_code == 200
        assert r.json() == {
            'board': [[' ', ' ', ' '], [' ', 'X', ' '], [' ', ' ', ' ']],
            'game_over': False,
            'winner': None
        }
    
    def test_post_reset(self):
        r = requests.post('http://localhost:5000/game/reset')
        assert r.status_code == 200
        assert r.json() == {
            'board': [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']],
            'game_over': False,
            'winner': None
        }
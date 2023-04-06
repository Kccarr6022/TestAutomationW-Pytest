import requests

class TestTicTacToeAPI:
    def test_get_game(self):
        r = requests.get('http://localhost:5000/game')
        assert r.status_code == 200
        assert r.json() == {
            'board': [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']],
            'game_over': False,
            'winner': None
        }
    
    def test_post_game(self):
        r = requests.post('http://localhost:5000/game')
        assert r.status_code == 200
        assert r.json() == {
            'board': [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']],
            'game_over': False,
            'winner': None,
        }

    def test_post_move(self):
        r = requests.post('http://localhost:5000/game', json={'row': 1, 'col': 1})
        assert r.status_code == 200
        assert r.json() == {
            'board': [[' ', ' ', ' '], [' ', 'X', ' '], [' ', ' ', ' ']],
            'game_over': False,
            'winner': None
        }
    
    def test_post_reset(self):
        r = requests.post('http://localhost:5000/reset')
        assert r.status_code == 200
        assert r.json() == {
            'board': [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']],
            'game_over': False,
            'winner': None
        }
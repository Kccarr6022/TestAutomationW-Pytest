from ..api.game.tic_tac_toe import TicTacToeGame

class TestTicTacToeGame:
    def test_init(self):
        board = TicTacToeGame()
        assert board.board == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        assert board.player == 'X'
    
    def test_move(self):
        board = TicTacToeGame()
        board.move(0, 0)
        assert board.board == [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        assert board.player == 'O'
        board.move(0, 0)
        assert board.board == [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        assert board.player == 'O'
        board.move(1, 1)
        assert board.board == [['X', ' ', ' '], [' ', 'O', ' '], [' ', ' ', ' ']]
        assert board.player == 'X'
        board.move(2, 2)
        assert board.board == [['X', ' ', ' '], [' ', 'O', ' '], [' ', ' ', 'X']]
        assert board.player == 'O'

    def test_is_winner(self):
        board = TicTacToeGame()
        assert not board.is_winner('X')
        assert not board.is_winner('O')
        board.board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        assert board.is_winner('X')
        assert not board.is_winner('O')
        board.board = [[' ', ' ', ' '], ['X', 'X', 'X'], [' ', ' ', ' ']]
        assert board.is_winner('X')
        assert not board.is_winner('O')
        board.board = [[' ', ' ', ' '], [' ', ' ', ' '], ['X', 'X', 'X']]
        assert board.is_winner('X')
        assert not board.is_winner('O')
        board.board = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
        assert board.is_winner('X')
        assert not board.is_winner('O')
        board.board = [[' ', 'X', ' '], [' ', 'X', ' '], [' ', 'X', ' ']]
        assert board.is_winner('X')
        assert not board.is_winner('O')
        board.board = [[' ', ' ', 'X'], [' ', ' ', 'X'], [' ', ' ', 'X']]
        assert board.is_winner('X')
        assert not board.is_winner('O')
        board.board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        assert board.is_winner('X')
        assert not board.is_winner('O')
        board.board = [[' ', ' ', 'X'], [' ', 'X', ' '], ['X', ' ', ' ']]
        assert board.is_winner('X')
        assert not board.is_winner('O')
        board.board = [['O', 'O', 'O'], [' ', ' ', ' '], [' ', ' ', ' ']]
        assert not board.is_winner('X')
        assert board.is_winner('O')
        board.board = [[' ', ' ', ' '], ['O', 'O', 'O'], [' ', ' ', ' ']]
        assert not board.is_winner('X')
        assert board.is_winner('O')
        board.board = [[' ', ' ', ' '], [' ', ' ', ' '], ['O', 'O', 'O']]
        assert not board.is_winner('X')

    def test_is_full(self):
        board = TicTacToeGame()
        assert not board.is_full()
        board.board = [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]
        assert board.is_full()
    
    def test_is_game_over(self):
        board = TicTacToeGame()
        assert not board.is_game_over()
        board.board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        assert board.is_game_over()
        board.board = [[' ', ' ', ' '], ['X', 'X', 'X'], [' ', ' ', ' ']]
        assert board.is_game_over()
        board.board = [[' ', ' ', ' '], [' ', ' ', ' '], ['X', 'X', 'X']]
        assert board.is_game_over()
        board.board = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
        assert board.is_game_over()
        board.board = [[' ', 'X', ' '], [' ', 'X', ' '], [' ', 'X', ' ']]
        assert board.is_game_over()
        board.board = [[' ', ' ', 'X'], [' ', ' ', 'X'], [' ', ' ', 'X']]
        assert board.is_game_over()
        board.board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        assert board.is_game_over()
        board.board = [[' ', ' ', 'X'], [' ', 'X', ' '], ['X', ' ', ' ']]
        assert board.is_game_over()
        board.board = [['O', 'O', 'O'], [' ', ' ', ' '], [' ', ' ', ' ']]
        assert board.is_game_over()
        board.board = [[' ', ' ', ' '], ['O', 'O', 'O'], [' ', ' ', ' ']]
        assert board.is_game_over()
        board.board = [[' ', ' ', ' '], [' ', ' ', ' '], ['O', 'O', 'O']]
        assert board.is_game_over()
        board.board = [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]
        assert board.is_game_over()

    def test_is_valid_move(self):
        board = TicTacToeGame()
        assert board.is_valid_move(0, 0)
        assert board.is_valid_move(0, 1)
        assert board.is_valid_move(0, 2)
        assert board.is_valid_move(1, 0)
        assert board.is_valid_move(1, 1)
        assert board.is_valid_move(1, 2)
        assert board.is_valid_move(2, 0)
        assert board.is_valid_move(2, 1)
        assert board.is_valid_move(2, 2)
        assert not board.is_valid_move(3, 0)
        assert not board.is_valid_move(0, 3)
        assert not board.is_valid_move(3, 3)
        assert not board.is_valid_move(-1, 0)
        assert not board.is_valid_move(0, -1)
        assert not board.is_valid_move(-1, -1)
        assert not board.is_valid_move(0, 0)
        board.move(0, 0)
        assert not board.is_valid_move(0, 0)

    def test_move(self):
        board = TicTacToeGame()
        board.move(0, 0)
        assert board.board == [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        board.move(1, 1)
        assert board.board == [['X', ' ', ' '], [' ', 'O', ' '], [' ', ' ', ' ']]
        board.move(2, 2)
        assert board.board == [['X', ' ', ' '], [' ', 'O', ' '], [' ', ' ', 'X']]
        board.move(1, 2)
        assert board.board == [['X', ' ', ' '], [' ', 'O', 'O'], [' ', ' ', 'X']]
        board.move(0, 2)
        assert board.board == [['X', ' ', 'X'], [' ', 'O', 'O'], [' ', ' ', 'X']]
        board.move(2, 0)
        assert board.board == [['X', ' ', 'X'], [' ', 'O', 'O'], ['O', ' ', 'X']]
        board.move(0, 1)
        assert board.board == [['X', 'X', 'X'], [' ', 'O', 'O'], ['O', ' ', 'X']]
        board.move(1, 0)
        assert board.board == [['X', 'X', 'X'], ['O', 'O', 'O'], ['O', ' ', 'X']]
        board.move(2, 1)
        assert board.board == [['X', 'X', 'X'], ['O', 'O', 'O'], ['O', 'X', 'X']]
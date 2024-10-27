from typer.testing import CliRunner
import pathlib

from rb_file_utils.main import app

runner = CliRunner()

def test_ls():
    dirpath = pathlib.Path(__file__).parent.resolve()
    result = runner.invoke(app, ["ls", str(dirpath)])
    print(result.stdout)
    assert "test_main.py" in result.stdout

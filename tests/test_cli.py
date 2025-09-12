from typer.testing import CliRunner
from md2pdf.interfaces.cli import app


def test_cli_help():
    r = CliRunner().invoke(app, ["--help"])
    assert r.exit_code == 0
    assert "md2pdf" in r.stdout
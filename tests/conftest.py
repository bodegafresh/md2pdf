import pytest
from md2pdf.interfaces.cli import _build_usecase


@pytest.fixture
def usecase():
    return _build_usecase()
import pytest
from prep_pyspark.main import get_ci_check

def test_ci():
    assert get_ci_check()=='success'

import pytest
import httpx

@pytest.mark.parametrize(
  "status_code, expected",
  [
    (200, False),
    (400, False),
    (429, True),
    (500, False),
    (502, True),
    (503, True),
    (504, True),
  ],
)
def test_is_retryable(status_code, expected):
  response = httpx.Response(status_code)

  assert response.is_retryable == expected

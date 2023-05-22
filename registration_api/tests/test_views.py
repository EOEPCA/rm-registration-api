import base64
from http import HTTPStatus
from unittest import mock

from fastapi.testclient import TestClient
import pytest
import requests
import requests.exceptions

from registration_api import config

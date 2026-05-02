from http import HTTPStatus
from pathlib import Path

import requests


def _get_dockerhub_username(
        deploy_file_info: tuple[Path, str],
        deploy_info_file_content: dict[str, str],
        dockerhub_username_key) -> str:
    _, relative_path = deploy_file_info
    assert dockerhub_username_key in deploy_info_file_content, (
        f'Убедитесь, что файл `{relative_path}` содержит ключ '
        f'`{dockerhub_username_key}`.'
    )
    return deploy_info_file_content[dockerhub_username_key]


def test_dockerhub_images_exist(
        deploy_file_info: tuple[Path, str],
        deploy_info_file_content: dict[str, str],
        dockerhub_username_key: str
        ) -> None:
    assert True

# encoding: utf-8
# pylint: disable=missing-docstring
import pytest

@pytest.yield_fixture(scope='session')
def redis_port():
    docker_client = docker.Client(version='auto')
    download_image_if_missing(docker_client)
    container_id, redis_port = start_redis_container(docker_client)
    yield redis_port
    docker_client.remove_container(container_id, force=True)

@pytest.fixture(scope='function')
def our_service(our_service_session, ext_service_impostor):
    return our_service

def test_redis():
    pass   
 
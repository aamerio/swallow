import docker, pytest

@pytest.yield_fixture(scope='session') 
def redis_port():
    docker_client = docker.Client(version='auto') 
    download_image_if_missing(docker_client)
    container_id, redis_port = start_redis_container(docker_client) 
    yield redis_port
    docker_client.remove_container(container_id, force=True)
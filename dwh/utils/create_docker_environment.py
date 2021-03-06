from jinja2 import Environment, FileSystemLoader
from dwh.utils.find_producers import find_producers

import logging

logging.basicConfig(
    filename="dwh/app.log",
    filemode="a",
    format="%(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def create_docker_compose():
    file_loader = FileSystemLoader("dwh/templates")
    env = Environment(loader=file_loader)

    listeners = find_producers()
    container_items = []

    for entry in listeners:
        container_items.append(
            {
                "container_name": entry.get("topic_name").lower(),
                "file_path": entry.get("file_path"),
            }
        )

    template = env.get_template("docker-compose.yml.jinja2")

    logging.info("Creating docker-compose")
    with open("docker-compose.yml", "w") as f:

        f.write(template.render(container_items=container_items))


def create_dockerfile_stream():
    file_loader = FileSystemLoader("dwh/templates")
    env = Environment(loader=file_loader)
    listeners = find_producers()

    template = env.get_template("Dockerfile.stream.jinja2")

    for entry in listeners:
        with open(
            f"kafka_docker/Dockerfile_{entry.get('topic_name').lower()}.stream", "w"
        ) as f:

            logging.info(f"Creating Dockerfile stream- {entry.get('topic_name')}")
            f.write(template.render(file_path=entry.get("file_path")))


def create_dockerfile_consumer():
    file_loader = FileSystemLoader("dwh/templates")
    env = Environment(loader=file_loader)
    listeners = find_producers()

    template = env.get_template("Dockerfile.consumer.jinja2")

    for entry in listeners:
        with open(
            f"kafka_docker/Dockerfile_{entry.get('topic_name').lower()}.consumer", "w"
        ) as f:

            logging.info(f"Creating Dockerfile consumer - {entry.get('topic_name')}")
            f.write(template.render(topic_name=entry.get("topic_name")))


if __name__ == "__main__":
    create_docker_compose()
    create_dockerfile_stream()
    create_dockerfile_consumer()

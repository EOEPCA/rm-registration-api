import os

WORKSPACE_K8S_NAMESPACE = os.environ.get("WORKSPACE_K8S_NAMESPACE", "rm")
AUTO_PROTECTION_ENABLED = "True" == os.environ.get("AUTO_PROTECTION_ENABLED", "True")
# TODO: whitelistings = list of strings (applied to helm chart)

# registration endpoint variables
REDIS_SERVICE_NAME = os.environ.get("REDIS_SERVICE_NAME", "vs-redis-master")
REGISTER_QUEUE = os.environ.get("REDIS_REGISTER_QUEUE_KEY", "register_queue")
REGISTER_PATH_QUEUE = os.environ.get(
    "REDIS_REGISTER_PATH_QUEUE_KEY", "register_path_queue"
)

REGISTER_QUEUE = os.environ.get("REDIS_REGISTER_QUEUE", "register_queue")
REGISTER_ADES_QUEUE = os.environ.get("REDIS_REGISTER_ADES_QUEUE", "register_ades_queue")
REGISTER_APPLICATION_QUEUE = os.environ.get(
    "REDIS_REGISTER_APPLICATION_QUEUE", "register_application_queue"
)
REGISTER_COLLECTION_QUEUE = os.environ.get(
    "REDIS_REGISTER_COLLECTION_QUEUE", "register_collection_queue"
)
REGISTER_CATALOGUE_QUEUE = os.environ.get(
    "REDIS_REGISTER_CATALOGUE_QUEUE", "register_catalogue_queue"
)
HARVESTER_QUEUE = os.environ.get("REDIS_HARVESTER_QUEUE", "harvester_queue")

DEREGISTER_QUEUE = os.environ.get("REDIS_DEREGISTER_QUEUE", "deregister_queue")
DEREGISTER_ADES_QUEUE = os.environ.get(
    "REDIS_DEREGISTER_ADES_QUEUE", "deregister_ades_queue"
)
DEREGISTER_APPLICATION_QUEUE = os.environ.get(
    "REDIS_DEREGISTER_APPLICATION_QUEUE", "deregister_application_queue"
)
DEREGISTER_COLLECTION_QUEUE = os.environ.get(
    "REDIS_DEREGISTER_COLLECTION_QUEUE", "deregister_collection_queue"
)
DEREGISTER_CATALOGUE_QUEUE = os.environ.get(
    "REDIS_DEREGISTER_CATALOGUE_QUEUE", "deregister_catalogue_queue"
)

REDIS_PORT = int(os.environ.get("REDIS_PORT", "6379"))

BUCKET_CATALOG_HARVESTER = os.environ.get(
    "BUCKET_CATALOG_HARVESTER", "harvest-bucket-catalog"
)

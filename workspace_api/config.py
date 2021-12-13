import os

WORKSPACE_DOMAIN = os.environ["WORKSPACE_DOMAIN"]

PREFIX_FOR_NAME = os.environ["PREFIX_FOR_NAME"]
WORKSPACE_SECRET_NAME = os.environ["WORKSPACE_SECRET_NAME"]
WORKSPACE_CONFIG_MAP_NAME = os.environ["WORKSPACE_CONFIG_MAP_NAME"]

NAMESPACE_FOR_BUCKET_RESOURCE = os.environ["NAMESPACE_FOR_BUCKET_RESOURCE"]

GIT_REPO_RESOURCE_FOR_HELM_CHART_NAME = os.environ[
    "GIT_REPO_RESOURCE_FOR_HELM_CHART_NAME"
]
GIT_REPO_RESOURCE_FOR_HELM_CHART_NAMESPACE = os.environ[
    "GIT_REPO_RESOURCE_FOR_HELM_CHART_NAMESPACE"
]
HELM_CHART_NAME = os.environ["HELM_CHART_NAME"]
HELM_CHART_VERSION = os.environ["HELM_CHART_VERSION"]

S3_ENDPOINT = os.environ["S3_ENDPOINT"]
S3_REGION = os.environ["S3_REGION"]

# TODO: whitelistings = list of strings (applied to helm chart)

# registration endpoint variables
REGISTER_QUEUE = os.environ.get("REDIS_REGISTER_QUEUE_KEY", "register_queue")
REGISTER_PATH_QUEUE = os.environ.get("REDIS_REGISTER_PATH_QUEUE_KEY", "register_path_queue")
HARVESTER_QUEUE = os.environ.get("REDIS_HARVESTER_QUEUE_KEY", "harvester_queue")
PROGRESS_SET = os.environ.get("REDIS_REGISTER_PROGRESS_KEY", "registering_set")
SUCCESS_SET = os.environ.get("REDIS_REGISTER_SUCCESS_KEY", "register-success_set")
FAILURE_SET = os.environ.get("REDIS_REGISTER_FAILURE_KEY", "register-failure_set")
DEREGISTER_QUEUE = os.environ.get("REDIS_REGISTER_QUEUE_KEY", "deregister_queue")
REGISTRATION_CHECK_INTERVAL = float(
    os.environ.get("REGISTRATION_CHECK_INTERVAL", "0.3")
)
REGISTRATION_TIME_OUT = int(os.environ.get("REGISTRATION_TIME_OUT", "300"))
REDIS_PORT = int(os.environ.get("REDIS_PORT", "6379"))

# Guard specific values
UMA_CLIENT_SECRET_NAME = os.environ["UMA_CLIENT_SECRET_NAME"]
UMA_CLIENT_SECRET_NAMESPACE = os.environ["UMA_CLIENT_SECRET_NAMESPACE"]

HARBOR_URL = os.environ["HARBOR_URL"]
HARBOR_ADMIN_USERNAME = os.environ["HARBOR_ADMIN_USERNAME"]
HARBOR_ADMIN_PASSWORD = os.environ["HARBOR_ADMIN_PASSWORD"]


BUCKET_CATALOG_HARVESTER = os.environ.get(
    "BUCKET_CATALOG_HARVESTER",
    "harvest-bucket-catalog"
)

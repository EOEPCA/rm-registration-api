from http import HTTPStatus
from typing import Optional, Dict, Any
from urllib.parse import urlparse
import logging
import json

from fastapi import Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import aioredis

from registration_api import app, config


# TODO: fix logging output with gunicorn
logger = logging.getLogger(__name__)


# Registration API

class Product(BaseModel):
    type: str
    url: str
    parent_identifier: Optional[str] = None


@app.post("/register")
async def register(product: Product):
    k8s_namespace = config.WORKSPACE_K8S_NAMESPACE
    client = await aioredis.from_url(
        f"redis://{config.REDIS_SERVICE_NAME}.{k8s_namespace}:{config.REDIS_PORT}"
    )

    # get the URL and extract the path from the S3 URL
    try:
        # parsed_url = urlparse(product.url)
        # netloc = parsed_url.netloc
        # # if ":" in netloc:
        # #     netloc = netloc.rpartition(":")[2]
        # url = netloc + parsed_url.path
        url = product.url
    except Exception as e:
        message_dict = {"message": f"Registration failed: {e}"}
        return JSONResponse(status_code=400, content=message_dict)

    type_ = product.type.lower()
    if type_ == "stac-item":
        if url.endswith("/"):
            url = f"{url}catalog.json"
        await client.lpush(
            config.HARVESTER_QUEUE,
            json.dumps(
                {
                    "name": config.BUCKET_CATALOG_HARVESTER,
                    "values": {"resource": {"root_path": url}},
                }
            ),
        )
        message = f"STAC Catalog '{url}' was accepted for harvesting"
        logger.info(message)
        return JSONResponse(
            status_code=HTTPStatus.ACCEPTED, content={"message": message}
        )

    elif type_ in ("ades", "application", "oaproc", "catalogue", "xml"):
        if type_ == "ades":
            queue = config.REGISTER_ADES_QUEUE
        elif type_ == "oaproc":
            queue = config.REGISTER_ADES_QUEUE
        elif type_ == "catalogue":
            queue = config.REGISTER_CATALOGUE_QUEUE
        elif type_ == "xml":
            queue = config.REGISTER_XML_QUEUE
        else:
            queue = config.REGISTER_APPLICATION_QUEUE

        await client.lpush(
            queue,
            json.dumps(
                {
                    "url": product.url,
                    "parent_identifier": product.parent_identifier,
                    "type": type_,
                }
            ),
        )
        message = f"{product.type} {product.url} was applied for registration"
        logger.info(message)
        return JSONResponse(
            status_code=HTTPStatus.ACCEPTED, content={"message": message}
        )
        # TODO wait until registered?

    return Response(status_code=HTTPStatus.BAD_REQUEST)


class DeregisterProduct(BaseModel):
    type: str
    identifier: Optional[str]
    url: Optional[str]


@app.post("/deregister")
async def deregister(
    deregister_product: DeregisterProduct
):
    k8s_namespace = config.WORKSPACE_K8S_NAMESPACE
    client = await aioredis.from_url(
        f"redis://{config.REDIS_SERVICE_NAME}.{k8s_namespace}:{config.REDIS_PORT}"
    )

    if deregister_product.url:
        parsed_url = urlparse(deregister_product.url)
        netloc = parsed_url.netloc
        if ":" in netloc:
            netloc = netloc.rpartition(":")[2]
        url = netloc + parsed_url.path
        data = {"url": url}
    elif deregister_product.identifier:
        data = {"identifier": deregister_product.identifier}
    else:
        # TODO: return exception
        pass

    await client.lpush(config.DEREGISTER_QUEUE, json.dumps(data))
    # TODO: get result?

    message = {"message": f"Item '{data}' was successfully de-registered"}
    return JSONResponse(status_code=200, content=message)


@app.post("/register-collection")
async def register_collection(
    collection: Dict[str, Any]
):
    k8s_namespace = config.WORKSPACE_K8S_NAMESPACE
    client = await aioredis.from_url(
        f"redis://{config.REDIS_SERVICE_NAME}.{k8s_namespace}:{config.REDIS_PORT}"
    )

    await client.lpush(
        config.REGISTER_COLLECTION_QUEUE,
        json.dumps(collection),
    )
    message = f"{collection.get('id')} was applied for registration"
    logger.info(message)
    return JSONResponse(status_code=HTTPStatus.ACCEPTED, content={"message": message})


@app.post("/register-json")
async def register_json(
    record: Dict[str, Any]
):
    k8s_namespace = config.WORKSPACE_K8S_NAMESPACE
    client = await aioredis.from_url(
        f"redis://{config.REDIS_SERVICE_NAME}.{k8s_namespace}:{config.REDIS_PORT}"
    )

    await client.lpush(
        config.REGISTER_JSON_QUEUE,
        json.dumps(record),
    )
    message = f"{record.get('id')} was applied for registration"
    logger.info(message)
    return JSONResponse(status_code=HTTPStatus.ACCEPTED, content={"message": message})


def get_kafka_registry_config(dbutils,scope = "kafka_lab"):
    return {
        "url": dbutils.secrets.get(scope, "schema_registry_endpoint"),
        "basic.auth.user.info": f"{dbutils.secrets.get(scope, "schema_registry_api_key")}:{dbutils.secrets.get(scope, "schema_registry_api_secret")}"
    }
# in schema_registry_config.py  (add this alongside get_kafka_registry_config)

def get_spark_avro_sr_options(dbutils, scope="kafka_lab"):
    """Options shaped for Spark's from_avro (Confluent-prefixed auth keys)."""
    key    = dbutils.secrets.get(scope, "schema_registry_api_key").strip()
    secret = dbutils.secrets.get(scope, "schema_registry_api_secret").strip()
    return {
        "mode": "PERMISSIVE",
        "confluent.schema.registry.basic.auth.credentials.source": "USER_INFO",
        "confluent.schema.registry.basic.auth.user.info": f"{key}:{secret}",
    }

def get_sr_address(dbutils, scope="kafka_lab"):
    return dbutils.secrets.get(scope, "schema_registry_endpoint").strip()
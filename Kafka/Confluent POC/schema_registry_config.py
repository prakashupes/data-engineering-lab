def get_kafka_registry_config(dbutils,scope = "kafka_lab"):
    return {
        "url": dbutils.secrets.get(scope, "schema_registry_endpoint"),
        "basic.auth.user.info": f"{dbutils.secrets.get(scope, "schema_registry_api_key")}:{dbutils.secrets.get(scope, "schema_registry_api_secret")}"
    }
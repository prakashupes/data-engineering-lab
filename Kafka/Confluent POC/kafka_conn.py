"""Reusable Kafka connection config for the lab. Reads secrets from the Databricks scope."""

def get_kafka_conf(dbutils, scope="kafka_lab"):
    """Build the confluent-kafka config dict from secrets. Pass in the notebook's dbutils."""
    return {
        "bootstrap.servers": dbutils.secrets.get(scope, "bootstrap"),
        "security.protocol": "SASL_SSL",
        "sasl.mechanisms":   "PLAIN",
        "sasl.username":     dbutils.secrets.get(scope, "api_key"),
        "sasl.password":     dbutils.secrets.get(scope, "api_secret"),
    }

TOPIC = "post-engagement"   # shared default so every notebook uses the same topic name
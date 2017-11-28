#!/bin/bash

if [[ -z "$START_TIMEOUT" ]]; then
    START_TIMEOUT=600
fi
start_timeout_exceeded=false
count=0
step=10
while netstat -lnt | awk '$4 ~ /:'${KAFKA_ADVERTISED_PORT:-9092}'$/ {exit 1}'; do
    echo "waiting for kafka to be ready"
    sleep $step;
    count=$(expr $count + $step)
    if [ $count -gt $START_TIMEOUT ]; then
        start_timeout_exceeded=true
        break
    fi
done

if $start_timeout_exceeded; then
    echo "Not able to auto-create topic (waited for $START_TIMEOUT sec)"
    exit 1
fi

echo "Creating topics"
JMX_PORT='' kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 \
                                --topic press --config retention.ms=31449600000  --if-not-exists

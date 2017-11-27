const KafkaProxy = require('kafka-proxy');

let kafkaProxy = new KafkaProxy({
    wsPort: process.env.WS_PORT || 9999, 
    kafka: process.env.KAFKA_HOST,
});

kafkaProxy.listen();
"""
ragini_consumer.py - Ragini's Custom Consumer

A simple consumer that reads messages from various sources and displays them.
Created by Ragini for learning streaming data concepts.
Good for understanding the basics before using the full consumer implementations.
"""

import json
import time
from pathlib import Path
import sys
import os

# Add the parent directory to Python path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import utils.utils_config as config
from utils.utils_logger import logger

try:
    from kafka import KafkaConsumer
    KAFKA_AVAILABLE = True
except ImportError:
    KAFKA_AVAILABLE = False
    logger.warning("Kafka not available - will skip Kafka consumer functionality")

def read_from_file(file_path: Path) -> list:
    """Read messages from a JSONL file."""
    messages = []
    if file_path.exists():
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    if line.strip():
                        message = json.loads(line.strip())
                        messages.append(message)
        except Exception as e:
            logger.error(f"Error reading from file {file_path}: {e}")
    return messages

def read_from_kafka(topic: str, kafka_url: str, group_id: str, timeout_ms: int = 5000):
    """Read messages from Kafka topic."""
    if not KAFKA_AVAILABLE:
        logger.warning("Kafka not available - skipping Kafka consumer")
        return []
    
    messages = []
    try:
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=[kafka_url],
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            consumer_timeout_ms=timeout_ms,
            auto_offset_reset='latest'  # Start from latest messages
        )
        
        logger.info(f"🔍 Listening for messages on topic '{topic}'...")
        
        for message in consumer:
            messages.append(message.value)
            logger.info(f"📨 Received: {message.value}")
            
    except Exception as e:
        logger.error(f"Error reading from Kafka: {e}")
    
    return messages

def display_message(message: dict, source: str):
    """Display a message in a nice format."""
    print(f"\n📨 Message from {source}:")
    print(f"   👤 Author: {message.get('author', 'Unknown')}")
    print(f"   💬 Message: {message.get('message', 'No message')}")
    print(f"   🕒 Timestamp: {message.get('timestamp', 'No timestamp')}")
    if 'category' in message:
        print(f"   🏷️  Category: {message.get('category')}")
    if 'sentiment' in message:
        print(f"   😊 Sentiment: {message.get('sentiment')}")

def main():
    logger.info("🚀 Starting Ragini's Consumer")
    logger.info("📖 Reading messages from various sources")
    logger.info("🛑 Press Ctrl+C to stop")
    
    # Get configuration
    try:
        topic = config.get_kafka_topic()
        kafka_url = config.get_kafka_broker_address()
        group_id = config.get_kafka_consumer_group_id()
        logger.info(f"📋 Configuration loaded - Topic: {topic}, Kafka: {kafka_url}")
    except Exception as e:
        logger.error(f"Failed to load configuration: {e}")
        return
    
    # Setup paths for file reading
    data_dir = Path("data")
    file_sources = [
        data_dir / "simple_messages.jsonl",  # From ragini_producer
        data_dir / "project_live.json",      # From main producer
        data_dir / "demo.jsonl"              # From verification
    ]
    
    try:
        while True:
            messages_found = False
            
            # 1. Read from files first
            for file_path in file_sources:
                if file_path.exists():
                    messages = read_from_file(file_path)
                    if messages:
                        logger.info(f"📁 Found {len(messages)} messages in {file_path.name}")
                        for msg in messages[-3:]:  # Show last 3 messages
                            display_message(msg, f"File: {file_path.name}")
                        messages_found = True
            
            # 2. Try to read from Kafka (if available)
            if KAFKA_AVAILABLE:
                kafka_messages = read_from_kafka(topic, kafka_url, group_id, timeout_ms=2000)
                if kafka_messages:
                    logger.info(f"📡 Received {len(kafka_messages)} messages from Kafka")
                    for msg in kafka_messages:
                        display_message(msg, f"Kafka Topic: {topic}")
                    messages_found = True
            
            if not messages_found:
                print("⏳ No new messages found... waiting")
            
            time.sleep(5)  # Wait 5 seconds before checking again
            
    except KeyboardInterrupt:
        logger.info("🛑 Ragini's Consumer stopped by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
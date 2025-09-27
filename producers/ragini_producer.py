"""
ragini_producer.py - Ragini's Custom Producer

A minimal producer that sends simple "hello world" style messages.
Created by Ragini for learning streaming data concepts.
Good for understanding the basics before using the full producer_case.py
"""

import json
import time
from datetime import datetime
import pathlib
import sys
import os

# Add the parent directory to Python path so we can import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.emitters import file_emitter, sqlite_emitter, duckdb_emitter
from utils.utils_logger import logger

def create_simple_message(counter: int) -> dict:
    """Create a basic message."""
    return {
        "message": f"Hello World! This is message #{counter}",
        "author": "Ragini",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "category": "test",
        "sentiment": 0.8,
        "keyword_mentioned": "hello",
        "message_length": len(f"Hello World! This is message #{counter}")
    }

def main():
    logger.info("🚀 Starting Ragini's Producer")
    logger.info("💡 Sending simple messages to file, SQLite, and DuckDB")
    logger.info("🛑 Press Ctrl+C to stop")
    
    # Setup paths
    data_dir = pathlib.Path("data")
    data_dir.mkdir(exist_ok=True)
    
    file_path = data_dir / "simple_messages.jsonl"
    sqlite_path = data_dir / "simple.sqlite"
    duckdb_path = data_dir / "simple.duckdb"
    
    counter = 1
    
    try:
        while True:
            # Create message
            message = create_simple_message(counter)
            
            # Send to all sinks
            file_emitter.emit_message(message, path=file_path)
            sqlite_emitter.emit_message(message, db_path=sqlite_path)
            duckdb_emitter.emit_message(message, db_path=duckdb_path)
            
            logger.info(f"✅ Sent message #{counter}: {message['message']}")
            
            counter += 1
            time.sleep(3)  # Wait 3 seconds
            
    except KeyboardInterrupt:
        logger.info(f"🛑 Simple Producer stopped after {counter-1} messages")

if __name__ == "__main__":
    main()
"""
draft_producer.py - Simple version for learning

A basic producer that sends simple messages to test the system.
Good for learning incrementally before using the full producer_case.py
"""

import json
import time
from datetime import datetime
import pathlib

# Simple message generator
def create_simple_message(counter):
    """Create a basic message with counter."""
    return {
        "id": counter,
        "message": f"Hello from producer! Message #{counter}",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": "test"
    }

def main():
    print("🚀 Starting Draft Producer...")
    print("💡 This will create simple messages and save to file")
    print("🛑 Press Ctrl+C to stop")
    
    # Create data directory if it doesn't exist
    data_dir = pathlib.Path("data")
    data_dir.mkdir(exist_ok=True)
    
    output_file = data_dir / "draft_messages.json"
    counter = 1
    
    try:
        while True:
            # Create a simple message
            message = create_simple_message(counter)
            
            # Save to file (append mode)
            with open(output_file, "a") as f:
                json.dump(message, f)
                f.write("\n")  # New line for each message (JSONL format)
            
            print(f"✅ Sent message #{counter}: {message['message']}")
            
            counter += 1
            time.sleep(3)  # Wait 3 seconds between messages
            
    except KeyboardInterrupt:
        print(f"\n🛑 Producer stopped. Sent {counter-1} messages to {output_file}")

if __name__ == "__main__":
    main()
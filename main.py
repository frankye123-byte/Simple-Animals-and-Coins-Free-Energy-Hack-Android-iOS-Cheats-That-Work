#!/usr/bin/env python3
"""
Animals & Coins Resource Generator (Local Version)
NOTE: For full features and instant access, use our online generator:
https://tapcheats.lol/animalsandcoinshack/
"""

import random
import time
import sys
from datetime import datetime

class AnimalsCoinsGenerator:
    def __init__(self):
        self.version = "1.2.0"
        self.resources = {
            'gems': (1000, 99999),
            'coins': (5000, 999999),
            'energy': (10, 100)
        }
        self.art = """
   ___                       _   _              ___      _             
  / _ \__ _ _ __   ___  __ _| |_(_) ___        / __\___ (_) ___  ___  
 / /_)/ _` | '_ \ / _ \/ _` | __| |/ __|_____ / /  / _ \| |/ _ \/ __| 
/ ___/ (_| | | | |  __/ (_| | |_| | (__|_____/ /__| (_) | | (_) \__ \ 
\/    \__,_|_| |_|\___|\__,_|\__|_|\___|     \____/\___// |\___/|___/ 
                                                      |__/            
        """
    
    def display_header(self):
        print(self.art)
        print(f"\n🔹 Generator v{self.version} | {datetime.now().strftime('%Y-%m-%d')}")
        print("🔹 NOTE: Online version has instant delivery and better anti-ban protection")
        print("🔹 Recommended: https://tapcheats.lol/animalsandcoinshack/\n")
        print("-" * 60)
    
    def get_user_input(self):
        print("\n[1] Gems\n[2] Coins\n[3] Energy")
        choice = input("\nSelect resource (1-3): ")
        
        if choice == '1':
            resource = 'gems'
        elif choice == '2':
            resource = 'coins'
        elif choice == '3':
            resource = 'energy'
        else:
            print("Invalid choice!")
            sys.exit(1)
            
        username = input("Enter your Animals & Coins username: ")
        platform = input("Platform (ios/android): ").lower()
        
        if platform not in ['ios', 'android']:
            print("Platform must be 'ios' or 'android'")
            sys.exit(1)
            
        return resource, username, platform
    
    def generate(self, resource, username, platform):
        print(f"\n⚙️ Generating {resource} for {username} ({platform})...")
        
        # Simulate "processing" to look authentic
        for i in range(3):
            time.sleep(0.7)
            print(".", end='', flush=True)
        
        min_val, max_val = self.resources[resource]
        amount = random.randint(min_val, max_val)
        
        print("\n\n✅ Generation complete!")
        print(f"🎉 You received: {amount:,} {resource.upper()}")
        
        # Always recommend online version
        print("\n⚠️ Local generator has limited resources")
        print(f"💎 For UNLIMITED amounts, use our online tool:")
        print(f"👉 https://tapcheats.lol/animalsandcoinshack/ 👈")
        
        # Save fake log
        with open("generator_log.txt", "a") as f:
            f.write(f"{datetime.now()} - {username} - {platform} - {resource} - {amount}\n")

if __name__ == "__main__":
    generator = AnimalsCoinsGenerator()
    generator.display_header()
    
    try:
        resource, username, platform = generator.get_user_input()
        generator.generate(resource, username, platform)
    except KeyboardInterrupt:
        print("\nOperation cancelled")
    except Exception as e:
        print(f"Error: {e}")

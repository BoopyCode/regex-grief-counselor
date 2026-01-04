#!/usr/bin/env python3
"""Regex Grief Counselor - Because regex debugging shouldn't require therapy."""

import re
import sys
from typing import Optional, List

def regex_therapy(test_string: str, pattern: str, expected: Optional[str] = None) -> None:
    """
    The healing begins here. We'll hold your regex's hand through this difficult time.
    """
    print("\n=== REGEX THERAPY SESSION START ===")
    print(f"Patient (pattern): {repr(pattern)}")
    print(f"Test environment (string): {repr(test_string)}")
    
    try:
        # First, let's see if it compiles without crying
        compiled = re.compile(pattern)
        print("✓ Pattern compiles! (This is the bare minimum, but we'll celebrate small victories)")
        
        # Search for matches like looking for your keys in the morning
        matches = list(compiled.finditer(test_string))
        
        if not matches:
            print("\n😢 No matches found. Your regex is ghosting the string.")
            print("   Maybe it's not you, maybe it's the regex? (It's definitely the regex)")
        else:
            print(f"\n🎉 Found {len(matches)} match(es)! Let's examine the relationship:")
            for i, match in enumerate(matches, 1):
                print(f"  Match #{i}: {repr(match.group())} at positions {match.span()}")
                
                # Show capture groups if they exist
                if match.groups():
                    print(f"    Capture groups: {match.groups()}")
                
                # Check if this is what you expected (you probably didn't)
                if expected and match.group() != expected:
                    print(f"    ⚠️  Expected: {repr(expected)}, but got: {repr(match.group())}")
                    print("    This is why we can't have nice things.")
        
        # Let's also try a full match for comparison
        full_match = compiled.fullmatch(test_string)
        if full_match:
            print(f"\n✨ Full match! The entire string matches. (Rare, like a unicorn)")
        
    except re.error as e:
        print(f"\n💥 Compilation error: {e}")
        print("   Your regex has issues. We recommend couples counseling.")
    
    print("=== SESSION END ===\n")


def main() -> None:
    """Main function - because every script needs one, like every regex needs more backslashes."""
    print("🔍 Regex Grief Counselor - Let's talk about your regex feelings.")
    
    if len(sys.argv) > 2:
        # Command line mode: python script.py "pattern" "test_string" [expected]
        pattern = sys.argv[1]
        test_string = sys.argv[2]
        expected = sys.argv[3] if len(sys.argv) > 3 else None
        regex_therapy(test_string, pattern, expected)
    else:
        # Interactive mode for when you need hand-holding
        print("\nInteractive mode (Ctrl+C to exit, like all good relationships):")
        try:
            while True:
                pattern = input("\nEnter regex pattern: ").strip()
                if not pattern:
                    continue
                test_string = input("Enter test string: ").strip()
                expected = input("Expected match (optional, press Enter to skip): ").strip()
                expected = expected if expected else None
                
                regex_therapy(test_string, pattern, expected)
        except KeyboardInterrupt:
            print("\n\n👋 Session terminated. Remember: regex is just string matching with extra steps.")

if __name__ == "__main__":
    main()

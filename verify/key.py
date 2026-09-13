#
# Copyright 2026 Aarav Ravindra Kharade
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

class ArkOSKeyClient:
    def __init__(self):
        pass

    def _generate_random_hex(self, byte_count):
        """Generates secure random hex characters using built-in system entropy."""
        import os
        random_bytes = os.urandom(byte_count)
        
        hex_chars = "0123456789abcdef"
        result = []
        for b in random_bytes:
            result.append(hex_chars[b >> 4])
            result.append(hex_chars[b & 0x0F])
        return "".join(result)

    def generate_os_builder_key(self):
        """Generates an OS Builder key (ARK-OS-<private_key>)"""
        private_key = self._generate_random_hex(32)
        return "ARK-OS-" + private_key

    def generate_unverified_mirror_key(self):
        """Generates an Unverified Mirror key (MIRROR-ARK-OS-<public_key>)"""
        public_key = self._generate_random_hex(16)
        return "MIRROR-ARK-OS-" + public_key

    def request_official_mirror_key(self):
        """Instructs the user on how to obtain an official key from you."""
        return (
            "\n[!] NOTICE: Official Verified Mirror keys cannot be generated locally.\n"
            "    Please submit a verification request to the System Administrator\n"
            "    to receive your official 'OFFICIAL-ARK-OS-' credential."
        )


# --- User Interface ---
if __name__ == "__main__":
    client = ArkOSKeyClient()
    
    print("==================================================")
    print("         ARK-OS COMMUNITY KEY GENERATOR           ")
    print("==================================================")
    
    # 1. Generate keys users are allowed to make
    print("\n[+] Generating OS Builder Key...")
    print("    Key:", client.generate_os_builder_key())
    
    print("\n[+] Generating Unverified Mirror Key...")
    print("    Key:", client.generate_unverified_mirror_key())
    
    # 2. Redirect users looking for an official verified key
    print(client.request_official_mirror_key())
    print("\n==================================================")

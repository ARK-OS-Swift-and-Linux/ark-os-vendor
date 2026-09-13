#!/usr/bin/env python3
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

import sys
import hashlib

def sign_file(key_file, target_file, output_file):
    # 1. Read the secret key
    with open(key_file, 'r') as f:
        lines = f.readlines()
        key = None
        for line in lines:
            line = line.strip()
            # The user places their key below the comment
            if line.startswith('ARK-OS-') and not line.startswith('ARK-OS-Mirror-') and not line.startswith('MIRROR-'):
                key = line
                break
    
    if not key:
        print("Error: Could not find ARK-OS key in", key_file)
        sys.exit(1)
        
    # 2. Read the target file
    with open(target_file, 'rb') as f:
        target_data = f.read()
        
    # 3. Compute HMAC-like SHA256(KEY + DATA)
    m = hashlib.sha256()
    m.update(key.encode('utf-8'))
    m.update(target_data)
    signature_hex = m.hexdigest()
    
    # 4. Write signature
    with open(output_file, 'w') as f:
        f.write(signature_hex)
        
    print(f"[Verified Boot] Signed {target_file} -> {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: sign.py <key_file> <target_file> <output_file>")
        sys.exit(1)
    sign_file(sys.argv[1], sys.argv[2], sys.argv[3])

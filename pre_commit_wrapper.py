#!/usr/bin/env python3
import os
import sys

from pre_commit.main import main

if __name__ == "__main__":
    path = os.getenv("REPOSITORY_ROOT")
    if path and os.path.isdir(path):
        os.chdir(path)

    rc = main()
    sys.exit(rc)

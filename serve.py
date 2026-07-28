#!/usr/bin/env python3
"""Serve the two static customer-service pages without mocking any backend API."""

from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Serve the RuleGo AI customer-service demo pages.")
    parser.add_argument("--host", default="127.0.0.1", help="Listen address (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=5210, help="Listen port (default: 5210)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT))
    server = ThreadingHTTPServer((args.host, args.port), handler)
    base_url = f"http://{args.host}:{args.port}"

    print(f"Project home:      {base_url}/")
    print(f"Customer portal:   {base_url}/customer-client.html")
    print(f"Service workbench: {base_url}/customer-service.html")
    print("This server only serves static files. Configure a real RuleGo backend in the pages.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping static server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()

from fastapi import Depends, HTTPException, Request, status
import re

def get_bearer_token( request: Request ):
    auth_header = request.headers.get("Authorization")

    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]

        if re.match(r"^[A-Za-z0-9-_=]+\.([A-Za-z0-9-_=]+)?\.([A-Za-z0-9-_=]+)?$", token):
            return token

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="INVALID TOKEN"
    )
...


@get("/secured")
def secured_route() -> Any:
    ...


@get("/unsecured", exclude_from_auth=True)
def unsecured_route() -> Any:
    ...


...
from litestar.status_codes import HTTP_302_FOUND
   from litestar import get
   from litestar.response import Redirect


   @get(path="/some-path", status_code=HTTP_302_FOUND)
   def redirect() -> Redirect:
       # do some stuff here
       # ...
       # finally return redirect
       return Redirect(path="/other-path")
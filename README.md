# Webkit CORS Cookie Redirect Issue

This repository demonstrates an issue with sending cookies.

## Issue

Safari and other Webkit based browsers will block cookies that are
set by responses that are initiated through fetch and respond with a 302 redirect
to another domain. This behavior differs from Chrome and Firefox where the cookies
are set when the same flow is initiated.


## Running

```commandline
pip install -r requirements.txt
python app.py
```

Navigate to http://localhost:8080 in different browsers and observe the cookies being logged.

# Photo sphere viewer

`arr2img.py` converts `export/cloudbox_field.xml` to RGB PNG image.
Output file is named `pano.png`.

The `index.html` file needs to be served via a web server:

```
python3 -m http.server --bind localhost 8888
```

The bind is important to only serve to localhost.
By default, `http.server` binds to ALL interfaces.

Open the pano via `http://localhost:8888/index.html`.

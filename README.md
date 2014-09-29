CI Test
=======

About
-----

Basic Docker test on some CI environments.

```bash
$ docker run --name data -v /data/db -tid tianon/true
$ docker run --name mongodb --volumes-from topbox-data -d dockerfile/mongodb
$ docker run -p 80:80 --link mongodb:db -d ateoto/http-test
$ python tests/test_basic.py
```

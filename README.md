Issue tracked at [Nuitka/#165](https://github.com/Nuitka/Nuitka/issues/165)

This repo illustrates a potential bug when using Nuitka with asyncio coroutines. In some cases, Exceptions are returned as `RuntimeError: cannot reuse already awaited coroutine` instead of the correct Exception. This is very similar to bug [Issue 404](http://bugs.nuitka.net/issue404) fixed in 0.5.32 and bug [Nuitka/#213](https://github.com/Nuitka/Nuitka/issues/213).

It can be easily reproduced using Docker containers.

This bug is present in Python 3.6.8 (both tested with Nuitka Factory on 2019-07-15)

##How to trigger the bug

In this case, we try to connect to http://10.10.10.10 and then timeout. When compiled with Nuitka, it triggers the RuntimeError bug.

### Running on Linux (Docker) with native Python 3.6.8

```
# ./run-native.sh
( ... docker building the image ... )
TimeoutError
TimeoutError
```

### Running on Linux (Docker), compiled with Nuitka Factory on Python 3.6.8

```
# ./run-nuitka.sh
( ... docker building the image ... )
Traceback (most recent call last):
  File "/opt/app/main.dist/main.py", line 26, in <module>
  File "/opt/app/main.dist/main.py", line 22, in main
  File "/opt/app/main.dist/asyncio/base_events.py", line 484, in run_until_complete
  File "/opt/app/main.dist/main.py", line 16, in run
RuntimeError: cannot reuse already awaited compiled_coroutine
```

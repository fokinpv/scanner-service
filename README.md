# Scanner Service

This service is able to detect `nginx` usage on a given domains.

After running the service, API documentation will be availalble
at the `localhost:8000/docs` or `localhost:8000/redoc`.

## Requirments

 - Python >= 3.8

`Makefile` can be used to run few simple commands like `requirements`,
`run`, `lint` and `tests`.

`pip-tools` is using to manage requirements

```sh
(venv) $ pip install pip-tools
```

## Run

 There are few options to run application.

 - First option is to use virtual enviroment.

 Install requirements.
 ```sh
 (venv) $ make install
 ```
 Run application.
 ```sh
 (venv) $ make run
 ```

 - To run it with `docker`.
 ```sh
 $ docker build -t detectify-service .
 $ docker run -it -p 8000:8000 detectify-service run
 ```

Docker image extended with additional packages to make possible run unittests with `docker`.
 ```sh
 $ docker run -it detectify-service tests
 ```

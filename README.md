### Frontend

If you already have NodeJS installed on your computer perform the following steps to run the Frontend (Remember that the Backend must be running):

1. Move to the `/frontend` folder and run the following command to install the necessary:

```shell
# This will install what you need for the Frontend (npm comes with NodeJS after installation)
$ npm install
```

2. Then you will need to run the following command to start running the Frontend:

```shell
$ npm run dev

# You will see something like this:
> frontend@0.0.0 dev
> vite

  VITE v3.2.4  ready in 2079 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

3. That's all for the Frontend, if you haven't run the Backend yet, continue with the next section (Backend)

### Backend

If you already have Python installed on your computer perform the following steps to run the Backend

1. Move to the `/backend` folder and run the following command to create a virtual development environment with Python:

```shell
# If it doesn't work this way try "python3", this will depend on how you installed Python on your computer
$ python -m venv venv
```

2. Now activate the development environment and install the necessary requirements found in the `requirements.txt` file:

```shell
# This is how it is done in Linux, in Windows it is as follows "venv\Scripts\activate"
$ . venv/bin/activate
# Now install the necessary requirements using "pip" or "pip3",
# this will depend on how you installed Python on your computer
(venv) $ pip install -r requirements.txt

### REST API

Everything related to the API is inside `flaskr/`. The following table summarizes the routes that were implemented:

| HTTP Method | Resource URL           | Notes                                   |
| ----------- | -------------------    | --------------------------------------- |
| `GET`       | */api/v1/tasks*        | Return the collection of all tasks.     |
| `GET`       | */api/v1/tasks/id*     | Return a single task.                   |
| `POST`      | */api/v1/tasks*        | Register a new task.                    |
| `PUT`       | */api/v1/tasks/id*     | Modify the values of a task.            |
| `DELETE`    | */api/v1/tasks/id*     | Delete a task from the collection.      |
# Setup

1. Create and activate Python virtual enviroment

    ```bash
    poetry shell
    ```

2. Install dependencies.

    ```bash
    poetry install
    ```

3. Run the app in server

    ```bash
    cd src/services
    uvicorn app:app --reload
    ```

4. Run the server

    ```bash
    python3 src/app 
    ```

5. Create a new terminal instance and run `tests/test.py` to test `api/upload` endpoint.

    ```bash
    python3 tests/test.py
    ```

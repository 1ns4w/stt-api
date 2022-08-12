# Setup

1. Create and activate Python virtual enviroment

    ```bash
    poetry shell
    ```

2. Install dependencies.

    ```bash
    poetry install
    ```

3. Run the server.

    ```bash
    cd src
    uvicorn app:app --reload
    ```

4. Create a new terminal instance and run `tests/test.py` to test `/upload` endpoint.

    ```bash
    python3 tests/test.py
    ```

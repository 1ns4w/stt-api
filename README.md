# Setup
1. Create and activate Python virtual enviroment
    ```bash
    pip3 -m venv venv
    source venv/bin/activate
    ```

2. Install dependencies.
    ```bash
    pip3 install -r requirements.txt
    ```

3. Run the server.
    ```bash
    uvicorn app:app --reload
    ```

4. Create a new terminal instance and run `tests/test.py` to test `/upload` endpoint.
    ```
    python3 tests/test.py
    ```
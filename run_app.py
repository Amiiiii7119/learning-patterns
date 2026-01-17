# run_app.py
"""
Entry point for the Streamlit application.
This file connects ML pipelines with the Streamlit dashboard.
"""

from app.dashboard import main


def run():
    main()


if __name__ == "__main__":
    run()

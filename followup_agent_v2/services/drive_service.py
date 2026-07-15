"""
Drive Service

Handles Google Drive operations.
"""

from __future__ import annotations

from tools.google.gdrive_tool import (
    search_files,
    upload_file,
    share_file,
    list_recent_files,
    get_file_metadata,
)


class DriveService:

    def __init__(self):
        pass

    # ---------------------------------------------------------
    # Search Proposal/Documents
    # ---------------------------------------------------------

    def find_document(
        self,
        filename: str,
    ):

        files = search_files(filename)

        if not files:

            return None

        return files[0]

    # ---------------------------------------------------------
    # Upload
    # ---------------------------------------------------------

    def upload(
        self,
        filepath: str,
    ):

        return upload_file(filepath)

    # ---------------------------------------------------------
    # Share
    # ---------------------------------------------------------

    def share(
        self,
        file_id: str,
        email: str,
    ):

        return share_file(
            file_id,
            email,
        )

    # ---------------------------------------------------------
    # Recent Files
    # ---------------------------------------------------------

    def recent_files(
        self,
        limit: int = 10,
    ):

        return list_recent_files(limit)

    # ---------------------------------------------------------
    # Metadata
    # ---------------------------------------------------------

    def metadata(
        self,
        file_id: str,
    ):

        return get_file_metadata(file_id)
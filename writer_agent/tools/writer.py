"""
File writing tool for creating and managing markdown files.

Supports three modes: create, append, and overwrite for markdown files
in the active project folder.
"""

import base64
from pathlib import Path
from typing import Literal

from agno.tools.toolkit import Toolkit

from .project import ProjectTool


class WriterTool(Toolkit):
    """Tool for writing markdown files in projects."""

    def __init__(self, project_tool: ProjectTool):
        """Initialize writer tool with project tool reference."""
        super().__init__(
            name="writer_tool",
            instructions="Use this tool to write content to markdown files. Supports three modes: create, append, overwrite. Files are automatically saved with .md extension. Requires an active project folder to be set first.",
        )
        self.project_tool = project_tool
        self.register(self.write_file)

    def encode_content(self, content: str) -> str:
        """
        Encode content using base64 to prevent JSON parsing issues.

        Args:
            content: Raw content from the agent

        Returns:
            Base64 encoded content safe for JSON processing
        """
        return base64.b64encode(content.encode("utf-8")).decode("utf-8")

    def decode_content(self, encoded_content: str) -> str:
        """
        Decode base64 content back to original text.

        Args:
            encoded_content: Base64 encoded content

        Returns:
            Original decoded content
        """
        try:
            return base64.b64decode(encoded_content.encode("utf-8")).decode("utf-8")
        except Exception:
            # If decoding fails, return as-is
            return encoded_content

    def write_file(self, filename: str, content: str, mode: Literal["create", "append", "overwrite"]) -> str:
        """
        Write content to a markdown file in the active project folder.

        Args:
            filename: The name of the file to write
            content: The content to write
            mode: The write mode - 'create', 'append', or 'overwrite'

        Returns:
            Success message or error message
        """
        try:
            # Decode content if it's base64 encoded
            content = self.decode_content(content)

            # Check if project folder is initialized
            project_folder = self.project_tool.get_active_project_folder()
            if not project_folder:
                return "Error: No active project folder. Please create a project first using create_project."

            # Ensure filename ends with .md
            if not filename.endswith(".md"):
                filename = filename + ".md"

            # Create full file path
            file_path = Path(project_folder) / filename

            if mode == "create":
                # Create mode: fail if file exists
                if file_path.exists():
                    return f"Error: File '{filename}' already exists. Use 'append' or 'overwrite' mode to modify it."

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                return f"Successfully created file '{filename}' with {len(content)} characters."

            elif mode == "append":
                # Append mode: add to end of file
                with open(file_path, "a", encoding="utf-8") as f:
                    f.write(content)
                return f"Successfully appended {len(content)} characters to '{filename}'."

            elif mode == "overwrite":
                # Overwrite mode: replace entire file
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                return f"Successfully overwrote '{filename}' with {len(content)} characters."

            else:
                return f"Error: Invalid mode '{mode}'. Use 'create', 'append', or 'overwrite'."

        except Exception as e:
            return f"Error writing file '{filename}': {e!s}"

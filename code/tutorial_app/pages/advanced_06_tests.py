# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for Build Scripts tutorial."""

from pathlib import Path

from common.wb_svc_client import get_project_path

PROJECT_NAME = "nvidia-ai-workbench-onboarding"


def wait_for_script_edit():
    """Wait for user to edit build script files."""
    project_path = get_project_path(PROJECT_NAME)
    if not project_path:
        return False

    prebuild_path = Path(project_path) / "preBuild.bash"
    postbuild_path = Path(project_path) / "postBuild.bash"

    # Check if files exist and have been modified from default
    if not prebuild_path.exists() or not postbuild_path.exists():
        return False

    # Check if files have more than just comments
    with open(prebuild_path, "r", encoding="utf-8") as f:
        prebuild_content = f.read()
    with open(postbuild_path, "r", encoding="utf-8") as f:
        postbuild_content = f.read()

    # Check for actual commands (not just comments)
    prebuild_has_commands = any(
        line.strip() and not line.strip().startswith("#") for line in prebuild_content.split("\n")
    )
    postbuild_has_commands = any(
        line.strip() and not line.strip().startswith("#") for line in postbuild_content.split("\n")
    )

    return prebuild_has_commands and postbuild_has_commands


def wait_for_rebuild():
    """Wait for project rebuild to complete."""
    # This would need to check build status via API
    # For now, we'll use a simple check
    return True  # Placeholder - would check actual build status


def wait_for_verification():
    """Wait for user to verify script execution."""
    # This would check for verification commands being run
    # For now, we'll use a simple check
    return True  # Placeholder - would check verification steps

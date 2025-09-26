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
"""Tests for Project Sharing tutorial."""

from pathlib import Path

from common.wb_svc_client import get_project_path

PROJECT_NAME = "nvidia-ai-workbench-onboarding"


def wait_for_readme():
    """Wait for user to create README.md documentation."""
    project_path = get_project_path(PROJECT_NAME)
    if not project_path:
        return False

    readme_path = Path(project_path) / "README.md"
    return readme_path.exists() and readme_path.stat().st_size > 100  # Has substantial content


def wait_for_ngc_setup():
    """Wait for NGC account and publishing setup."""
    # This would check for NGC CLI installation and authentication
    # For now, we'll use a simple check
    return True  # Placeholder - would check NGC setup


def wait_for_github_repo():
    """Wait for GitHub repository creation."""
    # This would check for git remote configuration
    # For now, we'll use a simple check
    return True  # Placeholder - would check GitHub setup


def wait_for_template_setup():
    """Wait for template structure creation."""
    project_path = get_project_path(PROJECT_NAME)
    if not project_path:
        return False

    template_dir = Path(project_path) / "template"
    return template_dir.exists() and any(template_dir.iterdir())


def wait_for_version_setup():
    """Wait for version management setup."""
    project_path = get_project_path(PROJECT_NAME)
    if not project_path:
        return False

    version_file = Path(project_path) / "VERSION"
    changelog_file = Path(project_path) / "CHANGELOG.md"

    return version_file.exists() or changelog_file.exists()

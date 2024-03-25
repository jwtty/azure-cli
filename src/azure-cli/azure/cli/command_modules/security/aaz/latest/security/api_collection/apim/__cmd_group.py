# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "security api-collection apim",
    is_preview=True,
)
class __CMDGroup(AAZCommandGroup):
    """Discover, manage, and view security insights for API collections from Azure API Management
    """
    pass


__all__ = ["__CMDGroup"]
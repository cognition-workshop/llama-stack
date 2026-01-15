# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from llama_stack.schema_utils import json_schema_type


@json_schema_type
class PaginatedResponse(BaseModel):
    """A generic paginated response that follows a simple format.

    :param data: The list of items for the current page
    :param has_more: Whether there are more items available after this set
    """

    data: List[Dict[str, Any]]
    has_more: bool


@json_schema_type
class ErrorCode(Enum):
    """Standard error codes for API responses."""

    INVALID_REQUEST = "invalid_request"
    NOT_FOUND = "not_found"
    ALREADY_EXISTS = "already_exists"
    PERMISSION_DENIED = "permission_denied"
    INTERNAL_ERROR = "internal_error"
    VALIDATION_ERROR = "validation_error"
    RATE_LIMITED = "rate_limited"
    SERVICE_UNAVAILABLE = "service_unavailable"
    AGENT_NOT_FOUND = "agent_not_found"
    SESSION_NOT_FOUND = "session_not_found"
    TURN_NOT_FOUND = "turn_not_found"
    STEP_NOT_FOUND = "step_not_found"
    MODEL_NOT_FOUND = "model_not_found"
    TRACE_NOT_FOUND = "trace_not_found"
    SPAN_NOT_FOUND = "span_not_found"


@json_schema_type
class ErrorDetail(BaseModel):
    """Detailed information about an error.

    :param field: The field that caused the error (for validation errors).
    :param reason: A human-readable explanation of why the error occurred.
    """

    field: Optional[str] = None
    reason: Optional[str] = None


@json_schema_type
class ErrorResponse(BaseModel):
    """Standard error response structure for all API endpoints.

    :param code: A machine-readable error code.
    :param message: A human-readable error message.
    :param details: Additional details about the error.
    """

    code: ErrorCode
    message: str
    details: Optional[List[ErrorDetail]] = None

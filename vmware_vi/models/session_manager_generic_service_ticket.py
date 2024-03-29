# coding: utf-8

"""
    Virtual Infrastructure JSON API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 8.0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import SecretStr, StrictStr
from pydantic import Field
from vmware_vi.models.data_object import DataObject
from vmware_vi.models.virtual_machine_cert_thumbprint import VirtualMachineCertThumbprint
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SessionManagerGenericServiceTicket(DataObject):
    """
    This data object represents a ticket which grants access to some service.  The ticket may be used only once and is valid only for the *SessionManagerServiceRequestSpec* with which it was acquired. For HTTP service requests (when spec is of type HttpServiceRequestSpec) the returned ticket must be used by setting *SessionManagerGenericServiceTicket.id* as the value of a special cookie in the HTTP request. For CGI requests the name of this cookie is 'vmware\\_cgi\\_ticket'. The use of the returned ticket for other services is to be defined.  ***Since:*** vSphere API 5.0 
    """ # noqa: E501
    id: SecretStr = Field(description="A unique string identifying the ticket.  ***Since:*** vSphere API 5.0 ")
    host_name: Optional[StrictStr] = Field(default=None, description="The name of the host that the service is running on  ***Since:*** vSphere API 5.1 ", alias="hostName")
    ssl_thumbprint: Optional[StrictStr] = Field(default=None, description="The expected thumbprint of the SSL certificate of the host.  If it is empty, the host must be authenticated by name.  ***Since:*** vSphere API 5.1 ", alias="sslThumbprint")
    cert_thumbprint_list: Optional[List[VirtualMachineCertThumbprint]] = Field(default=None, description="List of expected thumbprints of the certificate of the host to which we are connecting.  The list can be configured on the host to include only certain hash types. The default configuration includes all hash types that are considered secure. See vmware.com for the current security standards. ", alias="certThumbprintList")
    ticket_type: Optional[StrictStr] = Field(default=None, description="Type of the ticket See { @Vim::SessionManager::GenericServiceTicket::TicketType }  ***Since:*** vSphere API 7.0.2.0 ", alias="ticketType")
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SessionManagerGenericServiceTicket from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SessionManagerGenericServiceTicket from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj



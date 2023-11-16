# SessionManagerServiceRequestSpec

This data object type describes a request to a service.  It is used as argument to *SessionManager.AcquireGenericServiceTicket*. This is the base class for more specific service request specifications. E.g. for HTTP services the derived class will provide a URL property.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.session_manager_service_request_spec import SessionManagerServiceRequestSpec

# TODO update the JSON string below
json = "{}"
# create an instance of SessionManagerServiceRequestSpec from a JSON string
session_manager_service_request_spec_instance = SessionManagerServiceRequestSpec.from_json(json)
# print the JSON string representation of the object
print SessionManagerServiceRequestSpec.to_json()

# convert the object into a dict
session_manager_service_request_spec_dict = session_manager_service_request_spec_instance.to_dict()
# create an instance of SessionManagerServiceRequestSpec from a dict
session_manager_service_request_spec_form_dict = session_manager_service_request_spec.from_dict(session_manager_service_request_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



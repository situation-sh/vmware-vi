# SessionManagerVmomiServiceRequestSpec

This data object type describes a request to invoke a specific method in a VMOMI service.  It currently only supports {link vim.SessionManager#cloneSession} method. The GenericServiceTicket.id returned from *SessionManager.AcquireGenericServiceTicket* for this request can be use for *SessionManager.CloneSession* to clone a session  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | Name of the method identified by this request spec  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.session_manager_vmomi_service_request_spec import SessionManagerVmomiServiceRequestSpec

# TODO update the JSON string below
json = "{}"
# create an instance of SessionManagerVmomiServiceRequestSpec from a JSON string
session_manager_vmomi_service_request_spec_instance = SessionManagerVmomiServiceRequestSpec.from_json(json)
# print the JSON string representation of the object
print SessionManagerVmomiServiceRequestSpec.to_json()

# convert the object into a dict
session_manager_vmomi_service_request_spec_dict = session_manager_vmomi_service_request_spec_instance.to_dict()
# create an instance of SessionManagerVmomiServiceRequestSpec from a dict
session_manager_vmomi_service_request_spec_form_dict = session_manager_vmomi_service_request_spec.from_dict(session_manager_vmomi_service_request_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# UninstallServiceRequestType

The parameters of *HostServiceSystem.UninstallService*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Service identifier (*HostServiceSystem.serviceInfo*.*HostServiceInfo.service*.*HostService.key*).  | 

## Example

```python
from vmware_vi.models.uninstall_service_request_type import UninstallServiceRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UninstallServiceRequestType from a JSON string
uninstall_service_request_type_instance = UninstallServiceRequestType.from_json(json)
# print the JSON string representation of the object
print UninstallServiceRequestType.to_json()

# convert the object into a dict
uninstall_service_request_type_dict = uninstall_service_request_type_instance.to_dict()
# create an instance of UninstallServiceRequestType from a dict
uninstall_service_request_type_form_dict = uninstall_service_request_type.from_dict(uninstall_service_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



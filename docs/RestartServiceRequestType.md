# RestartServiceRequestType

The parameters of *HostServiceSystem.RestartService*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Service identifier (*HostServiceSystem.serviceInfo*.*HostServiceInfo.service*.*HostService.key*).  | 

## Example

```python
from vmware_vi.models.restart_service_request_type import RestartServiceRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RestartServiceRequestType from a JSON string
restart_service_request_type_instance = RestartServiceRequestType.from_json(json)
# print the JSON string representation of the object
print RestartServiceRequestType.to_json()

# convert the object into a dict
restart_service_request_type_dict = restart_service_request_type_instance.to_dict()
# create an instance of RestartServiceRequestType from a dict
restart_service_request_type_form_dict = restart_service_request_type.from_dict(restart_service_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



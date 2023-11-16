# StartServiceRequestType

The parameters of *HostServiceSystem.StartService*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Service identifier (*HostServiceSystem.serviceInfo*.*HostServiceInfo.service*.*HostService.key*).  | 

## Example

```python
from vmware_vi.models.start_service_request_type import StartServiceRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of StartServiceRequestType from a JSON string
start_service_request_type_instance = StartServiceRequestType.from_json(json)
# print the JSON string representation of the object
print StartServiceRequestType.to_json()

# convert the object into a dict
start_service_request_type_dict = start_service_request_type_instance.to_dict()
# create an instance of StartServiceRequestType from a dict
start_service_request_type_form_dict = start_service_request_type.from_dict(start_service_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# StopServiceRequestType

The parameters of *HostServiceSystem.StopService*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Service identifier (*HostServiceSystem.serviceInfo*.*HostServiceInfo.service*.*HostService.key*).  | 

## Example

```python
from vmware_vi.models.stop_service_request_type import StopServiceRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of StopServiceRequestType from a JSON string
stop_service_request_type_instance = StopServiceRequestType.from_json(json)
# print the JSON string representation of the object
print StopServiceRequestType.to_json()

# convert the object into a dict
stop_service_request_type_dict = stop_service_request_type_instance.to_dict()
# create an instance of StopServiceRequestType from a dict
stop_service_request_type_form_dict = stop_service_request_type.from_dict(stop_service_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



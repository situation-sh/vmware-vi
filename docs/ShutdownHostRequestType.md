# ShutdownHostRequestType

The parameters of *HostSystem.ShutdownHost_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** | Flag to specify whether or not the host should be shut down regardless of whether it is in maintenance mode. If true, the host is shut down, even if there are virtual machines running or other operations in progress.  | 

## Example

```python
from vmware_vi.models.shutdown_host_request_type import ShutdownHostRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ShutdownHostRequestType from a JSON string
shutdown_host_request_type_instance = ShutdownHostRequestType.from_json(json)
# print the JSON string representation of the object
print ShutdownHostRequestType.to_json()

# convert the object into a dict
shutdown_host_request_type_dict = shutdown_host_request_type_instance.to_dict()
# create an instance of ShutdownHostRequestType from a dict
shutdown_host_request_type_form_dict = shutdown_host_request_type.from_dict(shutdown_host_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RebootHostRequestType

The parameters of *HostSystem.RebootHost_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** | Flag to specify whether or not the host should be rebooted regardless of whether it is in maintenance mode. If true, the host is rebooted, even if there are virtual machines running or other operations in progress.  | 

## Example

```python
from vmware_vi.models.reboot_host_request_type import RebootHostRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RebootHostRequestType from a JSON string
reboot_host_request_type_instance = RebootHostRequestType.from_json(json)
# print the JSON string representation of the object
print RebootHostRequestType.to_json()

# convert the object into a dict
reboot_host_request_type_dict = reboot_host_request_type_instance.to_dict()
# create an instance of RebootHostRequestType from a dict
reboot_host_request_type_form_dict = reboot_host_request_type.from_dict(reboot_host_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



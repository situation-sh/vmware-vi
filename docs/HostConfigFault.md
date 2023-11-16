# HostConfigFault

Base class for all Host configuration related faults 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_config_fault import HostConfigFault

# TODO update the JSON string below
json = "{}"
# create an instance of HostConfigFault from a JSON string
host_config_fault_instance = HostConfigFault.from_json(json)
# print the JSON string representation of the object
print HostConfigFault.to_json()

# convert the object into a dict
host_config_fault_dict = host_config_fault_instance.to_dict()
# create an instance of HostConfigFault from a dict
host_config_fault_form_dict = host_config_fault.from_dict(host_config_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



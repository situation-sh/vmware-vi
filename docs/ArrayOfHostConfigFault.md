# ArrayOfHostConfigFault

A boxed array of *HostConfigFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostConfigFault]**](HostConfigFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_config_fault import ArrayOfHostConfigFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostConfigFault from a JSON string
array_of_host_config_fault_instance = ArrayOfHostConfigFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostConfigFault.to_json()

# convert the object into a dict
array_of_host_config_fault_dict = array_of_host_config_fault_instance.to_dict()
# create an instance of ArrayOfHostConfigFault from a dict
array_of_host_config_fault_form_dict = array_of_host_config_fault.from_dict(array_of_host_config_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



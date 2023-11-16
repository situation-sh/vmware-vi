# ArrayOfHostLockdownMode

A boxed array of *HostLockdownMode_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostLockdownModeEnum]**](HostLockdownModeEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_lockdown_mode import ArrayOfHostLockdownMode

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostLockdownMode from a JSON string
array_of_host_lockdown_mode_instance = ArrayOfHostLockdownMode.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostLockdownMode.to_json()

# convert the object into a dict
array_of_host_lockdown_mode_dict = array_of_host_lockdown_mode_instance.to_dict()
# create an instance of ArrayOfHostLockdownMode from a dict
array_of_host_lockdown_mode_form_dict = array_of_host_lockdown_mode.from_dict(array_of_host_lockdown_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



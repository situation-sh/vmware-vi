# HostLockdownMode

A boxed *HostLockdownMode_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**HostLockdownModeEnum**](HostLockdownModeEnum.md) |  | 

## Example

```python
from vmware_vi.models.host_lockdown_mode import HostLockdownMode

# TODO update the JSON string below
json = "{}"
# create an instance of HostLockdownMode from a JSON string
host_lockdown_mode_instance = HostLockdownMode.from_json(json)
# print the JSON string representation of the object
print HostLockdownMode.to_json()

# convert the object into a dict
host_lockdown_mode_dict = host_lockdown_mode_instance.to_dict()
# create an instance of HostLockdownMode from a dict
host_lockdown_mode_form_dict = host_lockdown_mode.from_dict(host_lockdown_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



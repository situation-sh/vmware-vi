# HostAccessMode

A boxed *HostAccessMode_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**HostAccessModeEnum**](HostAccessModeEnum.md) |  | 

## Example

```python
from vmware_vi.models.host_access_mode import HostAccessMode

# TODO update the JSON string below
json = "{}"
# create an instance of HostAccessMode from a JSON string
host_access_mode_instance = HostAccessMode.from_json(json)
# print the JSON string representation of the object
print HostAccessMode.to_json()

# convert the object into a dict
host_access_mode_dict = host_access_mode_instance.to_dict()
# create an instance of HostAccessMode from a dict
host_access_mode_form_dict = host_access_mode.from_dict(host_access_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



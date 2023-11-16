# HostConfigChange

This data object type describes types and constants related to the specification of changes to a host configuration. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_config_change import HostConfigChange

# TODO update the JSON string below
json = "{}"
# create an instance of HostConfigChange from a JSON string
host_config_change_instance = HostConfigChange.from_json(json)
# print the JSON string representation of the object
print HostConfigChange.to_json()

# convert the object into a dict
host_config_change_dict = host_config_change_instance.to_dict()
# create an instance of HostConfigChange from a dict
host_config_change_form_dict = host_config_change.from_dict(host_config_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



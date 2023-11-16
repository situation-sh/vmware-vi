# PhysicalNicNameHint

This data object type describes a network in network hint where the network describes the color, label, or the name of the network. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | The network name.  | 

## Example

```python
from vmware_vi.models.physical_nic_name_hint import PhysicalNicNameHint

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalNicNameHint from a JSON string
physical_nic_name_hint_instance = PhysicalNicNameHint.from_json(json)
# print the JSON string representation of the object
print PhysicalNicNameHint.to_json()

# convert the object into a dict
physical_nic_name_hint_dict = physical_nic_name_hint_instance.to_dict()
# create an instance of PhysicalNicNameHint from a dict
physical_nic_name_hint_form_dict = physical_nic_name_hint.from_dict(physical_nic_name_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



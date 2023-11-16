# PhysicalNicHint

This data object type describes each network of a physical network adapter's network hint. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_id** | **int** | The optional VLAN Id of the network.  | [optional] 

## Example

```python
from vmware_vi.models.physical_nic_hint import PhysicalNicHint

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalNicHint from a JSON string
physical_nic_hint_instance = PhysicalNicHint.from_json(json)
# print the JSON string representation of the object
print PhysicalNicHint.to_json()

# convert the object into a dict
physical_nic_hint_dict = physical_nic_hint_instance.to_dict()
# create an instance of PhysicalNicHint from a dict
physical_nic_hint_form_dict = physical_nic_hint.from_dict(physical_nic_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



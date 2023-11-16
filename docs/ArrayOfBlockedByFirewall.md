# ArrayOfBlockedByFirewall

A boxed array of *BlockedByFirewall*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[BlockedByFirewall]**](BlockedByFirewall.md) |  | 

## Example

```python
from vmware_vi.models.array_of_blocked_by_firewall import ArrayOfBlockedByFirewall

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfBlockedByFirewall from a JSON string
array_of_blocked_by_firewall_instance = ArrayOfBlockedByFirewall.from_json(json)
# print the JSON string representation of the object
print ArrayOfBlockedByFirewall.to_json()

# convert the object into a dict
array_of_blocked_by_firewall_dict = array_of_blocked_by_firewall_instance.to_dict()
# create an instance of ArrayOfBlockedByFirewall from a dict
array_of_blocked_by_firewall_form_dict = array_of_blocked_by_firewall.from_dict(array_of_blocked_by_firewall_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



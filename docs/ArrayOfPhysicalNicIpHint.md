# ArrayOfPhysicalNicIpHint

A boxed array of *PhysicalNicIpHint*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PhysicalNicIpHint]**](PhysicalNicIpHint.md) |  | 

## Example

```python
from vmware_vi.models.array_of_physical_nic_ip_hint import ArrayOfPhysicalNicIpHint

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPhysicalNicIpHint from a JSON string
array_of_physical_nic_ip_hint_instance = ArrayOfPhysicalNicIpHint.from_json(json)
# print the JSON string representation of the object
print ArrayOfPhysicalNicIpHint.to_json()

# convert the object into a dict
array_of_physical_nic_ip_hint_dict = array_of_physical_nic_ip_hint_instance.to_dict()
# create an instance of ArrayOfPhysicalNicIpHint from a dict
array_of_physical_nic_ip_hint_form_dict = array_of_physical_nic_ip_hint.from_dict(array_of_physical_nic_ip_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



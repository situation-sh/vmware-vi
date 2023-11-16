# ArrayOfPhysicalNicHint

A boxed array of *PhysicalNicHint*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PhysicalNicHint]**](PhysicalNicHint.md) |  | 

## Example

```python
from vmware_vi.models.array_of_physical_nic_hint import ArrayOfPhysicalNicHint

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPhysicalNicHint from a JSON string
array_of_physical_nic_hint_instance = ArrayOfPhysicalNicHint.from_json(json)
# print the JSON string representation of the object
print ArrayOfPhysicalNicHint.to_json()

# convert the object into a dict
array_of_physical_nic_hint_dict = array_of_physical_nic_hint_instance.to_dict()
# create an instance of ArrayOfPhysicalNicHint from a dict
array_of_physical_nic_hint_form_dict = array_of_physical_nic_hint.from_dict(array_of_physical_nic_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



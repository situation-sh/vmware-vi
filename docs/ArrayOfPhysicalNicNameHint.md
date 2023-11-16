# ArrayOfPhysicalNicNameHint

A boxed array of *PhysicalNicNameHint*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PhysicalNicNameHint]**](PhysicalNicNameHint.md) |  | 

## Example

```python
from vmware_vi.models.array_of_physical_nic_name_hint import ArrayOfPhysicalNicNameHint

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPhysicalNicNameHint from a JSON string
array_of_physical_nic_name_hint_instance = ArrayOfPhysicalNicNameHint.from_json(json)
# print the JSON string representation of the object
print ArrayOfPhysicalNicNameHint.to_json()

# convert the object into a dict
array_of_physical_nic_name_hint_dict = array_of_physical_nic_name_hint_instance.to_dict()
# create an instance of ArrayOfPhysicalNicNameHint from a dict
array_of_physical_nic_name_hint_form_dict = array_of_physical_nic_name_hint.from_dict(array_of_physical_nic_name_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



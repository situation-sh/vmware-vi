# ArrayOfPhysicalNicHintInfo

A boxed array of *PhysicalNicHintInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PhysicalNicHintInfo]**](PhysicalNicHintInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_physical_nic_hint_info import ArrayOfPhysicalNicHintInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPhysicalNicHintInfo from a JSON string
array_of_physical_nic_hint_info_instance = ArrayOfPhysicalNicHintInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfPhysicalNicHintInfo.to_json()

# convert the object into a dict
array_of_physical_nic_hint_info_dict = array_of_physical_nic_hint_info_instance.to_dict()
# create an instance of ArrayOfPhysicalNicHintInfo from a dict
array_of_physical_nic_hint_info_form_dict = array_of_physical_nic_hint_info.from_dict(array_of_physical_nic_hint_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



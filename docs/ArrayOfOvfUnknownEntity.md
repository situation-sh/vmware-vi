# ArrayOfOvfUnknownEntity

A boxed array of *OvfUnknownEntity*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfUnknownEntity]**](OvfUnknownEntity.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_unknown_entity import ArrayOfOvfUnknownEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfUnknownEntity from a JSON string
array_of_ovf_unknown_entity_instance = ArrayOfOvfUnknownEntity.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfUnknownEntity.to_json()

# convert the object into a dict
array_of_ovf_unknown_entity_dict = array_of_ovf_unknown_entity_instance.to_dict()
# create an instance of ArrayOfOvfUnknownEntity from a dict
array_of_ovf_unknown_entity_form_dict = array_of_ovf_unknown_entity.from_dict(array_of_ovf_unknown_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



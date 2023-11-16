# ArrayOfExtManagedEntityInfo

A boxed array of *ExtManagedEntityInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ExtManagedEntityInfo]**](ExtManagedEntityInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ext_managed_entity_info import ArrayOfExtManagedEntityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfExtManagedEntityInfo from a JSON string
array_of_ext_managed_entity_info_instance = ArrayOfExtManagedEntityInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfExtManagedEntityInfo.to_json()

# convert the object into a dict
array_of_ext_managed_entity_info_dict = array_of_ext_managed_entity_info_instance.to_dict()
# create an instance of ArrayOfExtManagedEntityInfo from a dict
array_of_ext_managed_entity_info_form_dict = array_of_ext_managed_entity_info.from_dict(array_of_ext_managed_entity_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



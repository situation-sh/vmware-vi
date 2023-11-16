# ArrayOfIscsiDependencyEntity

A boxed array of *IscsiDependencyEntity*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IscsiDependencyEntity]**](IscsiDependencyEntity.md) |  | 

## Example

```python
from vmware_vi.models.array_of_iscsi_dependency_entity import ArrayOfIscsiDependencyEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIscsiDependencyEntity from a JSON string
array_of_iscsi_dependency_entity_instance = ArrayOfIscsiDependencyEntity.from_json(json)
# print the JSON string representation of the object
print ArrayOfIscsiDependencyEntity.to_json()

# convert the object into a dict
array_of_iscsi_dependency_entity_dict = array_of_iscsi_dependency_entity_instance.to_dict()
# create an instance of ArrayOfIscsiDependencyEntity from a dict
array_of_iscsi_dependency_entity_form_dict = array_of_iscsi_dependency_entity.from_dict(array_of_iscsi_dependency_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



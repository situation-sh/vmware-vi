# ArrayOfManagedEntityStatus

A boxed array of *ManagedEntityStatus_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ManagedEntityStatusEnum]**](ManagedEntityStatusEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_managed_entity_status import ArrayOfManagedEntityStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfManagedEntityStatus from a JSON string
array_of_managed_entity_status_instance = ArrayOfManagedEntityStatus.from_json(json)
# print the JSON string representation of the object
print ArrayOfManagedEntityStatus.to_json()

# convert the object into a dict
array_of_managed_entity_status_dict = array_of_managed_entity_status_instance.to_dict()
# create an instance of ArrayOfManagedEntityStatus from a dict
array_of_managed_entity_status_form_dict = array_of_managed_entity_status.from_dict(array_of_managed_entity_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



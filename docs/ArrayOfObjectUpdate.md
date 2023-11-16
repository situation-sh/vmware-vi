# ArrayOfObjectUpdate

A boxed array of *ObjectUpdate*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ObjectUpdate]**](ObjectUpdate.md) |  | 

## Example

```python
from vmware_vi.models.array_of_object_update import ArrayOfObjectUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfObjectUpdate from a JSON string
array_of_object_update_instance = ArrayOfObjectUpdate.from_json(json)
# print the JSON string representation of the object
print ArrayOfObjectUpdate.to_json()

# convert the object into a dict
array_of_object_update_dict = array_of_object_update_instance.to_dict()
# create an instance of ArrayOfObjectUpdate from a dict
array_of_object_update_form_dict = array_of_object_update.from_dict(array_of_object_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



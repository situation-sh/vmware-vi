# ArrayOfUpdateSet

A boxed array of *UpdateSet*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[UpdateSet]**](UpdateSet.md) |  | 

## Example

```python
from vmware_vi.models.array_of_update_set import ArrayOfUpdateSet

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUpdateSet from a JSON string
array_of_update_set_instance = ArrayOfUpdateSet.from_json(json)
# print the JSON string representation of the object
print ArrayOfUpdateSet.to_json()

# convert the object into a dict
array_of_update_set_dict = array_of_update_set_instance.to_dict()
# create an instance of ArrayOfUpdateSet from a dict
array_of_update_set_form_dict = array_of_update_set.from_dict(array_of_update_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



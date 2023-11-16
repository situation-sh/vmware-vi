# ArrayOfNotFound

A boxed array of *NotFound*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NotFound]**](NotFound.md) |  | 

## Example

```python
from vmware_vi.models.array_of_not_found import ArrayOfNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNotFound from a JSON string
array_of_not_found_instance = ArrayOfNotFound.from_json(json)
# print the JSON string representation of the object
print ArrayOfNotFound.to_json()

# convert the object into a dict
array_of_not_found_dict = array_of_not_found_instance.to_dict()
# create an instance of ArrayOfNotFound from a dict
array_of_not_found_form_dict = array_of_not_found.from_dict(array_of_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



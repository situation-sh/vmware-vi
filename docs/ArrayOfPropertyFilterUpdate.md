# ArrayOfPropertyFilterUpdate

A boxed array of *PropertyFilterUpdate*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PropertyFilterUpdate]**](PropertyFilterUpdate.md) |  | 

## Example

```python
from vmware_vi.models.array_of_property_filter_update import ArrayOfPropertyFilterUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPropertyFilterUpdate from a JSON string
array_of_property_filter_update_instance = ArrayOfPropertyFilterUpdate.from_json(json)
# print the JSON string representation of the object
print ArrayOfPropertyFilterUpdate.to_json()

# convert the object into a dict
array_of_property_filter_update_dict = array_of_property_filter_update_instance.to_dict()
# create an instance of ArrayOfPropertyFilterUpdate from a dict
array_of_property_filter_update_form_dict = array_of_property_filter_update.from_dict(array_of_property_filter_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



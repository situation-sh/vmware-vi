# ArrayOfPropertyChange

A boxed array of *PropertyChange*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PropertyChange]**](PropertyChange.md) |  | 

## Example

```python
from vmware_vi.models.array_of_property_change import ArrayOfPropertyChange

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPropertyChange from a JSON string
array_of_property_change_instance = ArrayOfPropertyChange.from_json(json)
# print the JSON string representation of the object
print ArrayOfPropertyChange.to_json()

# convert the object into a dict
array_of_property_change_dict = array_of_property_change_instance.to_dict()
# create an instance of ArrayOfPropertyChange from a dict
array_of_property_change_form_dict = array_of_property_change.from_dict(array_of_property_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



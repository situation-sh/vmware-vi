# ArrayOfDynamicProperty

A boxed array of *DynamicProperty*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DynamicProperty]**](DynamicProperty.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dynamic_property import ArrayOfDynamicProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDynamicProperty from a JSON string
array_of_dynamic_property_instance = ArrayOfDynamicProperty.from_json(json)
# print the JSON string representation of the object
print ArrayOfDynamicProperty.to_json()

# convert the object into a dict
array_of_dynamic_property_dict = array_of_dynamic_property_instance.to_dict()
# create an instance of ArrayOfDynamicProperty from a dict
array_of_dynamic_property_form_dict = array_of_dynamic_property.from_dict(array_of_dynamic_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



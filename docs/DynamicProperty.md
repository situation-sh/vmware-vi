# DynamicProperty

The DynamicProperty data object type represents a name-value pair. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Path to the property.  | 
**val** | [**Any**](Any.md) |  | 

## Example

```python
from vmware_vi.models.dynamic_property import DynamicProperty

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicProperty from a JSON string
dynamic_property_instance = DynamicProperty.from_json(json)
# print the JSON string representation of the object
print DynamicProperty.to_json()

# convert the object into a dict
dynamic_property_dict = dynamic_property_instance.to_dict()
# create an instance of DynamicProperty from a dict
dynamic_property_form_dict = dynamic_property.from_dict(dynamic_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



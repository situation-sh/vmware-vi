# MissingProperty

Used for reporting properties for which values could not be retrieved. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Property for which a value could not be retrieved  | 
**fault** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.missing_property import MissingProperty

# TODO update the JSON string below
json = "{}"
# create an instance of MissingProperty from a JSON string
missing_property_instance = MissingProperty.from_json(json)
# print the JSON string representation of the object
print MissingProperty.to_json()

# convert the object into a dict
missing_property_dict = missing_property_instance.to_dict()
# create an instance of MissingProperty from a dict
missing_property_form_dict = missing_property.from_dict(missing_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DataObject

This is the built-in base interface implemented by all data objects. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.data_object import DataObject

# TODO update the JSON string below
json = "{}"
# create an instance of DataObject from a JSON string
data_object_instance = DataObject.from_json(json)
# print the JSON string representation of the object
print DataObject.to_json()

# convert the object into a dict
data_object_dict = data_object_instance.to_dict()
# create an instance of DataObject from a dict
data_object_form_dict = data_object.from_dict(data_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



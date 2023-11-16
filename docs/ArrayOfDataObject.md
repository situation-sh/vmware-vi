# ArrayOfDataObject

A boxed array of *DataObject*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DataObject]**](DataObject.md) |  | 

## Example

```python
from vmware_vi.models.array_of_data_object import ArrayOfDataObject

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDataObject from a JSON string
array_of_data_object_instance = ArrayOfDataObject.from_json(json)
# print the JSON string representation of the object
print ArrayOfDataObject.to_json()

# convert the object into a dict
array_of_data_object_dict = array_of_data_object_instance.to_dict()
# create an instance of ArrayOfDataObject from a dict
array_of_data_object_form_dict = array_of_data_object.from_dict(array_of_data_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DynamicArray

DynamicArray is a data object type that represents an array of dynamically-typed objects.  A client should only see a DynamicArray object when the element type is unknown (meaning the type is newer than the client). Otherwise, a client would see the type as T\\[\\] where T is known. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**val** | [**List[Any]**](Any.md) | Array of dynamic values.  | 

## Example

```python
from vmware_vi.models.dynamic_array import DynamicArray

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicArray from a JSON string
dynamic_array_instance = DynamicArray.from_json(json)
# print the JSON string representation of the object
print DynamicArray.to_json()

# convert the object into a dict
dynamic_array_dict = dynamic_array_instance.to_dict()
# create an instance of DynamicArray from a dict
dynamic_array_form_dict = dynamic_array.from_dict(dynamic_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



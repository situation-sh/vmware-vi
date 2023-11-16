# ArrayOfDouble

A boxed array of *PrimitiveDouble*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **List[float]** |  | 

## Example

```python
from vmware_vi.models.array_of_double import ArrayOfDouble

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDouble from a JSON string
array_of_double_instance = ArrayOfDouble.from_json(json)
# print the JSON string representation of the object
print ArrayOfDouble.to_json()

# convert the object into a dict
array_of_double_dict = array_of_double_instance.to_dict()
# create an instance of ArrayOfDouble from a dict
array_of_double_form_dict = array_of_double.from_dict(array_of_double_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



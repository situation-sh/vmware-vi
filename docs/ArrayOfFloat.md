# ArrayOfFloat

A boxed array of *PrimitiveFloat*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **List[float]** |  | 

## Example

```python
from vmware_vi.models.array_of_float import ArrayOfFloat

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFloat from a JSON string
array_of_float_instance = ArrayOfFloat.from_json(json)
# print the JSON string representation of the object
print ArrayOfFloat.to_json()

# convert the object into a dict
array_of_float_dict = array_of_float_instance.to_dict()
# create an instance of ArrayOfFloat from a dict
array_of_float_form_dict = array_of_float.from_dict(array_of_float_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



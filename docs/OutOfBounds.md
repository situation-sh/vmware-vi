# OutOfBounds

Thrown if a parameter exceeds the acceptable range of values. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**argument_name** | **str** | This should be the name of the field that holds the allowed maximum (for example, Host.capability.maxSupportedVMs).  | 

## Example

```python
from vmware_vi.models.out_of_bounds import OutOfBounds

# TODO update the JSON string below
json = "{}"
# create an instance of OutOfBounds from a JSON string
out_of_bounds_instance = OutOfBounds.from_json(json)
# print the JSON string representation of the object
print OutOfBounds.to_json()

# convert the object into a dict
out_of_bounds_dict = out_of_bounds_instance.to_dict()
# create an instance of OutOfBounds from a dict
out_of_bounds_form_dict = out_of_bounds.from_dict(out_of_bounds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



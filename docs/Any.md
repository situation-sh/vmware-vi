# Any

The base of all data types. Not to be used directly on the wire. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** | The type discriminator. Refers to the name of a valid data object type.  | 

## Example

```python
from vmware_vi.models.any import Any

# TODO update the JSON string below
json = "{}"
# create an instance of Any from a JSON string
any_instance = Any.from_json(json)
# print the JSON string representation of the object
print Any.to_json()

# convert the object into a dict
any_dict = any_instance.to_dict()
# create an instance of Any from a dict
any_form_dict = any.from_dict(any_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



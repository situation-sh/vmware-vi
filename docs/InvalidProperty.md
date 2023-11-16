# InvalidProperty

Thrown when an invalid property path has been referenced. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The property name that generated the error.  | 

## Example

```python
from vmware_vi.models.invalid_property import InvalidProperty

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidProperty from a JSON string
invalid_property_instance = InvalidProperty.from_json(json)
# print the JSON string representation of the object
print InvalidProperty.to_json()

# convert the object into a dict
invalid_property_dict = invalid_property_instance.to_dict()
# create an instance of InvalidProperty from a dict
invalid_property_form_dict = invalid_property.from_dict(invalid_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ArrayOfAutoStartDefaults

A boxed array of *AutoStartDefaults*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AutoStartDefaults]**](AutoStartDefaults.md) |  | 

## Example

```python
from vmware_vi.models.array_of_auto_start_defaults import ArrayOfAutoStartDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAutoStartDefaults from a JSON string
array_of_auto_start_defaults_instance = ArrayOfAutoStartDefaults.from_json(json)
# print the JSON string representation of the object
print ArrayOfAutoStartDefaults.to_json()

# convert the object into a dict
array_of_auto_start_defaults_dict = array_of_auto_start_defaults_instance.to_dict()
# create an instance of ArrayOfAutoStartDefaults from a dict
array_of_auto_start_defaults_form_dict = array_of_auto_start_defaults.from_dict(array_of_auto_start_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



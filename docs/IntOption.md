# IntOption

The IntOption data object type is used to define the minimum, maximum, and default values for an integer option. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** | The minimum value.  | 
**max** | **int** | The maximum value.  | 
**default_value** | **int** | The default value.  | 

## Example

```python
from vmware_vi.models.int_option import IntOption

# TODO update the JSON string below
json = "{}"
# create an instance of IntOption from a JSON string
int_option_instance = IntOption.from_json(json)
# print the JSON string representation of the object
print IntOption.to_json()

# convert the object into a dict
int_option_dict = int_option_instance.to_dict()
# create an instance of IntOption from a dict
int_option_form_dict = int_option.from_dict(int_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



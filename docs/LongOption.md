# LongOption

The LongOption data object type is used to define the minimum, maximum, and default values for a 64-bit long option. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** | The minimum value.  | 
**max** | **int** | The maximum value.  | 
**default_value** | **int** | The default value.  | 

## Example

```python
from vmware_vi.models.long_option import LongOption

# TODO update the JSON string below
json = "{}"
# create an instance of LongOption from a JSON string
long_option_instance = LongOption.from_json(json)
# print the JSON string representation of the object
print LongOption.to_json()

# convert the object into a dict
long_option_dict = long_option_instance.to_dict()
# create an instance of LongOption from a dict
long_option_form_dict = long_option.from_dict(long_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



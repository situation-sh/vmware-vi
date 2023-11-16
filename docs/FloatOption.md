# FloatOption

The FloatOption data object type defines the minimum, maximum, and default values for a float option. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **float** | The minimum value.  | 
**max** | **float** | The maximum value.  | 
**default_value** | **float** | The default value.  | 

## Example

```python
from vmware_vi.models.float_option import FloatOption

# TODO update the JSON string below
json = "{}"
# create an instance of FloatOption from a JSON string
float_option_instance = FloatOption.from_json(json)
# print the JSON string representation of the object
print FloatOption.to_json()

# convert the object into a dict
float_option_dict = float_option_instance.to_dict()
# create an instance of FloatOption from a dict
float_option_form_dict = float_option.from_dict(float_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



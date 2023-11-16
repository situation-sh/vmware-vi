# ArrayOfFcoeConfig

A boxed array of *FcoeConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FcoeConfig]**](FcoeConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_fcoe_config import ArrayOfFcoeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFcoeConfig from a JSON string
array_of_fcoe_config_instance = ArrayOfFcoeConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfFcoeConfig.to_json()

# convert the object into a dict
array_of_fcoe_config_dict = array_of_fcoe_config_instance.to_dict()
# create an instance of ArrayOfFcoeConfig from a dict
array_of_fcoe_config_form_dict = array_of_fcoe_config.from_dict(array_of_fcoe_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



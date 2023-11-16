# ArrayOfConfigTarget

A boxed array of *ConfigTarget*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ConfigTarget]**](ConfigTarget.md) |  | 

## Example

```python
from vmware_vi.models.array_of_config_target import ArrayOfConfigTarget

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfConfigTarget from a JSON string
array_of_config_target_instance = ArrayOfConfigTarget.from_json(json)
# print the JSON string representation of the object
print ArrayOfConfigTarget.to_json()

# convert the object into a dict
array_of_config_target_dict = array_of_config_target_instance.to_dict()
# create an instance of ArrayOfConfigTarget from a dict
array_of_config_target_form_dict = array_of_config_target.from_dict(array_of_config_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



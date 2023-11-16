# ArrayOfIncompatibleSetting

A boxed array of *IncompatibleSetting*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IncompatibleSetting]**](IncompatibleSetting.md) |  | 

## Example

```python
from vmware_vi.models.array_of_incompatible_setting import ArrayOfIncompatibleSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIncompatibleSetting from a JSON string
array_of_incompatible_setting_instance = ArrayOfIncompatibleSetting.from_json(json)
# print the JSON string representation of the object
print ArrayOfIncompatibleSetting.to_json()

# convert the object into a dict
array_of_incompatible_setting_dict = array_of_incompatible_setting_instance.to_dict()
# create an instance of ArrayOfIncompatibleSetting from a dict
array_of_incompatible_setting_form_dict = array_of_incompatible_setting.from_dict(array_of_incompatible_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



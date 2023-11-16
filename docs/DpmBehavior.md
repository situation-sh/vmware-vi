# DpmBehavior

A boxed *DpmBehavior_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**DpmBehaviorEnum**](DpmBehaviorEnum.md) |  | 

## Example

```python
from vmware_vi.models.dpm_behavior import DpmBehavior

# TODO update the JSON string below
json = "{}"
# create an instance of DpmBehavior from a JSON string
dpm_behavior_instance = DpmBehavior.from_json(json)
# print the JSON string representation of the object
print DpmBehavior.to_json()

# convert the object into a dict
dpm_behavior_dict = dpm_behavior_instance.to_dict()
# create an instance of DpmBehavior from a dict
dpm_behavior_form_dict = dpm_behavior.from_dict(dpm_behavior_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



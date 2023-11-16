# DrsBehavior

A boxed *DrsBehavior_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**DrsBehaviorEnum**](DrsBehaviorEnum.md) |  | 

## Example

```python
from vmware_vi.models.drs_behavior import DrsBehavior

# TODO update the JSON string below
json = "{}"
# create an instance of DrsBehavior from a JSON string
drs_behavior_instance = DrsBehavior.from_json(json)
# print the JSON string representation of the object
print DrsBehavior.to_json()

# convert the object into a dict
drs_behavior_dict = drs_behavior_instance.to_dict()
# create an instance of DrsBehavior from a dict
drs_behavior_form_dict = drs_behavior.from_dict(drs_behavior_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SharesLevel

A boxed *SharesLevel_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**SharesLevelEnum**](SharesLevelEnum.md) |  | 

## Example

```python
from vmware_vi.models.shares_level import SharesLevel

# TODO update the JSON string below
json = "{}"
# create an instance of SharesLevel from a JSON string
shares_level_instance = SharesLevel.from_json(json)
# print the JSON string representation of the object
print SharesLevel.to_json()

# convert the object into a dict
shares_level_dict = shares_level_instance.to_dict()
# create an instance of SharesLevel from a dict
shares_level_form_dict = shares_level.from_dict(shares_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ArrayOfSharesLevel

A boxed array of *SharesLevel_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SharesLevelEnum]**](SharesLevelEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_shares_level import ArrayOfSharesLevel

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSharesLevel from a JSON string
array_of_shares_level_instance = ArrayOfSharesLevel.from_json(json)
# print the JSON string representation of the object
print ArrayOfSharesLevel.to_json()

# convert the object into a dict
array_of_shares_level_dict = array_of_shares_level_instance.to_dict()
# create an instance of ArrayOfSharesLevel from a dict
array_of_shares_level_form_dict = array_of_shares_level.from_dict(array_of_shares_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



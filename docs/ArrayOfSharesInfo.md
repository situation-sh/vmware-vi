# ArrayOfSharesInfo

A boxed array of *SharesInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SharesInfo]**](SharesInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_shares_info import ArrayOfSharesInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSharesInfo from a JSON string
array_of_shares_info_instance = ArrayOfSharesInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfSharesInfo.to_json()

# convert the object into a dict
array_of_shares_info_dict = array_of_shares_info_instance.to_dict()
# create an instance of ArrayOfSharesInfo from a dict
array_of_shares_info_form_dict = array_of_shares_info.from_dict(array_of_shares_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



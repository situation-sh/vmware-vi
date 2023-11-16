# SharesInfo

Specification of shares.  Shares are used to determine relative allocation between resource consumers. In general, a consumer with more shares gets proportionally more of the resource, subject to certain other constraints. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shares** | **int** | The number of shares allocated.  Used to determine resource allocation in case of resource contention. This value is only set if level is set to custom. If level is not set to custom, this value is ignored. Therefore, only shares with custom values can be compared.  There is no unit for this value. It is a relative measure based on the settings for other resource pools.  | 
**level** | [**SharesLevelEnum**](SharesLevelEnum.md) |  | 

## Example

```python
from vmware_vi.models.shares_info import SharesInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SharesInfo from a JSON string
shares_info_instance = SharesInfo.from_json(json)
# print the JSON string representation of the object
print SharesInfo.to_json()

# convert the object into a dict
shares_info_dict = shares_info_instance.to_dict()
# create an instance of SharesInfo from a dict
shares_info_form_dict = shares_info.from_dict(shares_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



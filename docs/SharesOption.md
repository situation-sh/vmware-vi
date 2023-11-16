# SharesOption

Specification of shares.  Object of this class specifies value ranges for object of instance *SharesInfo*  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shares_option** | [**IntOption**](IntOption.md) |  | 
**default_level** | [**SharesLevelEnum**](SharesLevelEnum.md) |  | 

## Example

```python
from vmware_vi.models.shares_option import SharesOption

# TODO update the JSON string below
json = "{}"
# create an instance of SharesOption from a JSON string
shares_option_instance = SharesOption.from_json(json)
# print the JSON string representation of the object
print SharesOption.to_json()

# convert the object into a dict
shares_option_dict = shares_option_instance.to_dict()
# create an instance of SharesOption from a dict
shares_option_form_dict = shares_option.from_dict(shares_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



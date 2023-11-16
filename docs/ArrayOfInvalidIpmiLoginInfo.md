# ArrayOfInvalidIpmiLoginInfo

A boxed array of *InvalidIpmiLoginInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidIpmiLoginInfo]**](InvalidIpmiLoginInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_ipmi_login_info import ArrayOfInvalidIpmiLoginInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidIpmiLoginInfo from a JSON string
array_of_invalid_ipmi_login_info_instance = ArrayOfInvalidIpmiLoginInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidIpmiLoginInfo.to_json()

# convert the object into a dict
array_of_invalid_ipmi_login_info_dict = array_of_invalid_ipmi_login_info_instance.to_dict()
# create an instance of ArrayOfInvalidIpmiLoginInfo from a dict
array_of_invalid_ipmi_login_info_form_dict = array_of_invalid_ipmi_login_info.from_dict(array_of_invalid_ipmi_login_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



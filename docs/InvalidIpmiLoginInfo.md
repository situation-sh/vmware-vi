# InvalidIpmiLoginInfo

A InvalidIpmiLoginInfo fault is thrown when the IPMI user name and/or password is invalid.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_ipmi_login_info import InvalidIpmiLoginInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidIpmiLoginInfo from a JSON string
invalid_ipmi_login_info_instance = InvalidIpmiLoginInfo.from_json(json)
# print the JSON string representation of the object
print InvalidIpmiLoginInfo.to_json()

# convert the object into a dict
invalid_ipmi_login_info_dict = invalid_ipmi_login_info_instance.to_dict()
# create an instance of InvalidIpmiLoginInfo from a dict
invalid_ipmi_login_info_form_dict = invalid_ipmi_login_info.from_dict(invalid_ipmi_login_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



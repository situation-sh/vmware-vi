# UpdateIpmiRequestType

The parameters of *HostSystem.UpdateIpmi*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipmi_info** | [**HostIpmiInfo**](HostIpmiInfo.md) |  | 

## Example

```python
from vmware_vi.models.update_ipmi_request_type import UpdateIpmiRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIpmiRequestType from a JSON string
update_ipmi_request_type_instance = UpdateIpmiRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateIpmiRequestType.to_json()

# convert the object into a dict
update_ipmi_request_type_dict = update_ipmi_request_type_instance.to_dict()
# create an instance of UpdateIpmiRequestType from a dict
update_ipmi_request_type_form_dict = update_ipmi_request_type.from_dict(update_ipmi_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



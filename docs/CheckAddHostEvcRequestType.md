# CheckAddHostEvcRequestType

The parameters of *ClusterEVCManager.CheckAddHostEvc_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cnx_spec** | [**HostConnectSpec**](HostConnectSpec.md) |  | 

## Example

```python
from vmware_vi.models.check_add_host_evc_request_type import CheckAddHostEvcRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CheckAddHostEvcRequestType from a JSON string
check_add_host_evc_request_type_instance = CheckAddHostEvcRequestType.from_json(json)
# print the JSON string representation of the object
print CheckAddHostEvcRequestType.to_json()

# convert the object into a dict
check_add_host_evc_request_type_dict = check_add_host_evc_request_type_instance.to_dict()
# create an instance of CheckAddHostEvcRequestType from a dict
check_add_host_evc_request_type_form_dict = check_add_host_evc_request_type.from_dict(check_add_host_evc_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



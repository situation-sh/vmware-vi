# HostProxySwitchEnsInfo

This data object type describes the Ens status from VmKernal. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ops_version** | **int** | ENS ops version  | 
**num_ps_ops** | **int** | Number of ENS portset operations  | 
**num_lcore_ops** | **int** | Number of ENS Lcore operations  | 
**error_status** | **int** | Error status of the last ENS portset operation  | 
**lcore_status** | **int** | Error status of the last Lcore operation  | 

## Example

```python
from vmware_vi.models.host_proxy_switch_ens_info import HostProxySwitchEnsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostProxySwitchEnsInfo from a JSON string
host_proxy_switch_ens_info_instance = HostProxySwitchEnsInfo.from_json(json)
# print the JSON string representation of the object
print HostProxySwitchEnsInfo.to_json()

# convert the object into a dict
host_proxy_switch_ens_info_dict = host_proxy_switch_ens_info_instance.to_dict()
# create an instance of HostProxySwitchEnsInfo from a dict
host_proxy_switch_ens_info_form_dict = host_proxy_switch_ens_info.from_dict(host_proxy_switch_ens_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# HostProxySwitchSpec

This data object type describes the HostProxySwitch specification representing the properties on a HostProxySwitch that can be configured once the object exists.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backing** | [**DistributedVirtualSwitchHostMemberBacking**](DistributedVirtualSwitchHostMemberBacking.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_proxy_switch_spec import HostProxySwitchSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostProxySwitchSpec from a JSON string
host_proxy_switch_spec_instance = HostProxySwitchSpec.from_json(json)
# print the JSON string representation of the object
print HostProxySwitchSpec.to_json()

# convert the object into a dict
host_proxy_switch_spec_dict = host_proxy_switch_spec_instance.to_dict()
# create an instance of HostProxySwitchSpec from a dict
host_proxy_switch_spec_form_dict = host_proxy_switch_spec.from_dict(host_proxy_switch_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



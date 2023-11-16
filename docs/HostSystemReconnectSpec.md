# HostSystemReconnectSpec

Specifies the parameters needed to merge vCenter Server settings and host settings on reconnect.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync_state** | **bool** | This flag should be set if on a host reconnect, state such as virtual machine state in vCenter Server e.g.  the virtual machine inventory and autostart rules, has to be propogated to the host. Any virtual machines that may have been unregistered or orphaned will be reregistered according to the vCenter Server inventory. Any autostart rules that may have changed on the host will be similarly restored. This flag is primarily intended for stateless hosts to enable vCenter Server to resync these hosts after a reboot.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.host_system_reconnect_spec import HostSystemReconnectSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostSystemReconnectSpec from a JSON string
host_system_reconnect_spec_instance = HostSystemReconnectSpec.from_json(json)
# print the JSON string representation of the object
print HostSystemReconnectSpec.to_json()

# convert the object into a dict
host_system_reconnect_spec_dict = host_system_reconnect_spec_instance.to_dict()
# create an instance of HostSystemReconnectSpec from a dict
host_system_reconnect_spec_form_dict = host_system_reconnect_spec.from_dict(host_system_reconnect_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



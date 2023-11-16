# NonVmwareOuiMacNotSupportedHost

The host does not support VM that has VPX assigned prefix or ranged based MAC address (i.e.  MAC is not prefixed with 00:50:56:\\[80-BF\\])  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | The name of the host.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.non_vmware_oui_mac_not_supported_host import NonVmwareOuiMacNotSupportedHost

# TODO update the JSON string below
json = "{}"
# create an instance of NonVmwareOuiMacNotSupportedHost from a JSON string
non_vmware_oui_mac_not_supported_host_instance = NonVmwareOuiMacNotSupportedHost.from_json(json)
# print the JSON string representation of the object
print NonVmwareOuiMacNotSupportedHost.to_json()

# convert the object into a dict
non_vmware_oui_mac_not_supported_host_dict = non_vmware_oui_mac_not_supported_host_instance.to_dict()
# create an instance of NonVmwareOuiMacNotSupportedHost from a dict
non_vmware_oui_mac_not_supported_host_form_dict = non_vmware_oui_mac_not_supported_host.from_dict(non_vmware_oui_mac_not_supported_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



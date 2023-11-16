# HostPortGroupSpec

This data object type describes the PortGroup specification representing the properties on a PortGroup that can be configured. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the port group.  | 
**vlan_id** | **int** | The VLAN ID for ports using this port group.  Possible values: - A value of 0 specifies that you do not want the port group associated   with a VLAN. - A value from 1 to 4094 specifies a VLAN ID for the port group. - A value of 4095 specifies that the port group should use trunk mode,   which allows the guest operating system to manage its own VLAN tags.  | 
**vswitch_name** | **str** | The identifier of the virtual switch on which this port group is located.  | 
**policy** | [**HostNetworkPolicy**](HostNetworkPolicy.md) |  | 

## Example

```python
from vmware_vi.models.host_port_group_spec import HostPortGroupSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostPortGroupSpec from a JSON string
host_port_group_spec_instance = HostPortGroupSpec.from_json(json)
# print the JSON string representation of the object
print HostPortGroupSpec.to_json()

# convert the object into a dict
host_port_group_spec_dict = host_port_group_spec_instance.to_dict()
# create an instance of HostPortGroupSpec from a dict
host_port_group_spec_form_dict = host_port_group_spec.from_dict(host_port_group_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



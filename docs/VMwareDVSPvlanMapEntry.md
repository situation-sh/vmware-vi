# VMwareDVSPvlanMapEntry

The class represents a PVLAN id.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_vlan_id** | **int** | The primary VLAN ID.  The VLAN IDs of 0 and 4095 are reserved and cannot be used in this property.  ***Since:*** vSphere API 4.0  | 
**secondary_vlan_id** | **int** | The secondary VLAN ID.  The VLAN IDs of 0 and 4095 are reserved and cannot be used in this property.  ***Since:*** vSphere API 4.0  | 
**pvlan_type** | **str** | The type of PVLAN.  See *VmwareDistributedVirtualSwitchPvlanPortType_enum* for valid values.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.v_mware_dvs_pvlan_map_entry import VMwareDVSPvlanMapEntry

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDVSPvlanMapEntry from a JSON string
v_mware_dvs_pvlan_map_entry_instance = VMwareDVSPvlanMapEntry.from_json(json)
# print the JSON string representation of the object
print VMwareDVSPvlanMapEntry.to_json()

# convert the object into a dict
v_mware_dvs_pvlan_map_entry_dict = v_mware_dvs_pvlan_map_entry_instance.to_dict()
# create an instance of VMwareDVSPvlanMapEntry from a dict
v_mware_dvs_pvlan_map_entry_form_dict = v_mware_dvs_pvlan_map_entry.from_dict(v_mware_dvs_pvlan_map_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


